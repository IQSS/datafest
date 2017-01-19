## ----attach R http client package----------------------------------------
library(httr) # for sending GET and POST requests, useful for API's
library(purrr) # for iteration a list manipulation

## ----calling the federal register API with default parameters------------
fr.url <- "https://www.federalregister.gov"
fr.doc.api <- "api/v1"

fr.monthly <- GET(fr.url,
                path = c(fr.doc.api,
                         "documents",
                         "facets",
                         "monthly"))

## ----examining the generated URL-----------------------------------------
modify_url(fr.url,
                path = c(fr.doc.api,
                         "documents",
                         "facets",
                         "monthly"))
## looks good, so

fr.monthly <- GET(fr.url,
                path = c(fr.doc.api,
                         "documents",
                         "facets",
                         "monthly"))

## ----checking the status of the response---------------------------------
http_status(fr.monthly)

## ----examine the headers of the response---------------------------------
headers(fr.monthly)

## ----use the jsonlite package to convert json to R lists-----------------
library(jsonlite)

## ----working with the contents of the response---------------------------
## extract and examine content from the response
fr.monthly.content <- content(fr.monthly, as = "text")
cat(str_sub(fr.monthly.content, 1, 100), "\n")

## convert the content to native R list
fr.monthly.content <- fromJSON(fr.monthly.content)
## inspect the result
str(head(fr.monthly.content))

## ------------------------------------------------------------------------
fr.monthly.content <- content(fr.monthly)

## ----arranging the data for analysis-------------------------------------
fr.monthly.content <- as.data.frame(
  do.call(rbind, map(fr.monthly.content, unlist)), 
  stringsAsFactors = FALSE)

str(fr.monthly.content)

library(lubridate)
library(stringr)

fr.monthly.content$name <- dmy(str_c("01", fr.monthly.content$name, sep = " "))
fr.monthly.content$count <- as.integer(as.character(fr.monthly.content$count))
str(fr.monthly.content)

## ----ploting retrieved values--------------------------------------------
library(ggplot2)
ggplot(fr.monthly.content, aes(x = name, y = count)) +
    geom_line() +
    scale_x_date(date_breaks = "1 year") +
    theme(axis.text.x = element_text(angle = 60, hjust = 1))

## ----passing parameters in the query string------------------------------
## first check the url our settings will construct
modify_url(fr.url,
           path = c(fr.doc.api,
                    "documents",
                    "facets",
                    "agency"),
           query = "conditions[publication_date][year]=2015&conditions[type][]=NOTICE")

## looks good, so
fr.agency.2015 <- GET(fr.url,
                path = c(fr.doc.api,
                         "documents",
                         "facets",
                         "agency"),
                query = "conditions[publication_date][year]=2015&conditions[type][]=NOTICE")

## combine the results into a data.frame
fr.agency.2015.content <- as.data.frame(do.call(rbind, map(content(fr.agency.2015), unlist)))

## cleanup and format
fr.agency.2015.content$count <- as.integer(as.character(fr.agency.2015.content$count))
fr.agency.2015.content$name <- reorder(fr.agency.2015.content$name, fr.agency.2015.content$count)
fr.agency.2015.content <- fr.agency.2015.content[order(fr.agency.2015.content$count, decreasing = TRUE), ]

## ------------------------------------------------------------------------

ggplot(head(fr.agency.2015.content, 20), aes(x = name, y = count)) +
    geom_bar(stat = "identity") +
    coord_flip()

## ----use the rvest package for reading and processing html---------------
library(rvest)

## ----read the starting page and parse it into a form R can work with-----
data.page <- read_html("https://www.gpo.gov/fdsys/bulkdata/FR")

## ----extract links from the bulkdata node--------------------------------
links.table <- html_nodes(data.page, css = "#bulkdata > table")
links <- html_nodes(links.table, css = "a")

## ----extract all the href attributes from the list of anchor nodes-------
links <- map_chr(links, html_attr, name = "href")

## ----filter the strings to retain only data links------------------------
library(stringr)
links <- str_subset(links, "[0-9]$")
links

## ----prepend the base url to the extracted (relative) links--------------
links <- str_c("https://www.gpo.gov/fdsys", links, sep = "/")

## ----follow each page link and extract the download link-----------------
getDataLink <- function(url) {
    page <- read_html(url)
    anchor <- html_nodes(page, css = "#bulkdata > table > tr:nth-child(3) > td:nth-child(1) > a")
    html_attr(anchor, "href")
}

getDataLink(links[[1]])

## ----extract all the links and prepend the base URL----------------------
allDataLinks <- str_c("https://www.gpo.gov/fdsys", map_chr(links, getDataLink), sep = "/")

