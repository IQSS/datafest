#' ---
#' title: "Cleaning up messy data"
#' author: "Ista Zahn, Daina Bouquin"
#' output: 
#'   html_document:
#'     highlight: tango
#'     toc: true
#'     toc_float:
#'       collapsed: true
#' ---
#' 
#' 
#' Workshop overview and materials
#' ===============================
#' 
#' Workshop description
#' --------------------
#' 
#' Data scientists are known and celebrated for modeling and visually
#' displaying information, but down in the data science engine room there
#' is a lot of less glamorous work to be done. Before data can be used
#' effectively it must often be cleaned, corrected, and reformatted. This
#' workshop introduces the basic tools needed to make your data behave,
#' including data reshaping, regular expressions and other text
#' manipulation tools.
#' 
#' Prerequisites and Preparation
#' -----------------------------
#' 
#' Prior to the workshop you should:
#' 
#' - install R from <https://cran.r-project.org/>
#' - install RStudio from <https://www.rstudio.com/products/rstudio/download/#download>
#' - install the tidyverse package in R with `install.packages("tidyverse")`
#' - download and extract the workshop materials from 
#'   <https://github.com/izahn/R-data-cleaning/archive/messy_data_v1.zip>
#' 
#' The lesson notes are included in the download link above. You can also
#' view the lesson notes at
#' <https://rawgit.com/izahn/R-data-cleaning/master/dataCleaning.html>
#' 
#' A github repository containing the workshop materials is
#' available <https://github.com/izahn/R-data-cleaning>.
#' 
#' This is an intermediate/advanced R course appropriate for those with
#' basic knowledge of R. If you need a refresher we recommend the
#' [Software Carpentry Introductory R material](https://swcarpentry.github.io/r-novice-gapminder/01-rstudio-intro/).
#' 
#' Example project overview
#' ------------------------
#' 
#' It is common for data to be made available on a website somewhere, either by a
#' government agency, research group, or other organizations and entities. Often
#' the data you want is spread over many files, and retrieving it all one file at a
#' time is tedious and time consuming. Such is the case with the baby names data we
#' will be using today.
#' 
#' The UK [Office for National Statistics](https://www.ons.gov.uk) provides yearly
#' data on the most popular baby names going back to 1996. The data is provided
#' separately for boys and girls and is stored in Excel spreadsheets.
#' 
#' I have downloaded all the excel files containing boys names data from https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/datasets/babynamesenglandandwalesbabynamesstatisticsboys. Our mission is
#' to extract and graph the top 100 boys names in England and Wales for every year
#' since 1996. There are several things that make this challenging:
#' 
#' 1. The worksheet containing the data of interest is in different
#'    positions and has different names from one year to the next. However,
#'    it always includes "Table 1" in the worksheet name.
#' 2. The data does not start on row one. Headers are on row 7, followed by a blank
#'    line, followed by the actual data.
#' 3. The data is stored in an inconvenient way, with ranks 1-50 in the first set
#'    of columns and ranks 51-100 in a separate set of columns.
#' 4. Some years include columns for "changes in rank", others do not.
#' 5. There are notes below the data.
#' 
#' As you can see, we have a lot of work to do. Let's get started by attaching some useful R packages.
#' 
## ------------------------------------------------------------------------
library(tidyverse)
library(stringr)
library(readxl)
library(purrr)

#' 
#' Iterating over a directory of files
#' ================================================
#' 
#' Our first task is to iterate over all the data files and read the appropriate
#' sheet from each one. As noted above, the appropriate sheet differs from year to
#' year, but always has "Table 1" in the sheet name.
#' 
#' The first step is to get a vector of file names.
#' 
## ------------------------------------------------------------------------
boy.file.names <- list.files("babyNamesData/boys", full.names = TRUE)

#' 
#' Now we can iterate over the file names and get the names of each worksheet. We
#' could use a `for` loop, or `sapply`, but the `map` family of functions from the *purrr*
#' package gives us a more consistent alternative, so we'll use that.
#' 
## ------------------------------------------------------------------------
map(boy.file.names, excel_sheets)

#' 
#' Filtering strings using regular expressions
#' ===========================================================
#' 
#' In order extract the correct worksheet names we will use functions for
#' manipulating strings. Base R provides some string manipulation
#' capabilities (see `?regex`, `?sub` and `?grep`), but we will use the
#' *stringr* package because it is more user-friendly.
#' 
#' The *stringr* package provides functions to *detect*, *locate*,
#' *extract*, *match*, *replace*, *combine* and *split* strings (among
#' other things). 
#' 
#' Here we want to detect the pattern "Table 1", and only
#' return elements with this pattern. We can do that using the
#' `str_subset` function. The first argument to `str_subset` is character
#' vector we want to search in. The second argument is a *regular
#' expression* matching the pattern we want to retain.
#' 
#' If you are not familiar with regular expressions, <http://www.regexr.com/> is a
#' good place to start.
#' 
#' Now that we know how to filter character vectors using `str_subset` we can
#' identify the correct sheets for each year.
#' 
## ------------------------------------------------------------------------
findTable1 <- function(x) {
  str_subset(excel_sheets(x), "Table 1")
}

map(boy.file.names, findTable1)

#' 
#' Reading all the files
#' =============================
#' 
#' Next we want to read the correct worksheet from each file. We already know how
#' to iterate over a vector of file names with `map`, and we know how to identify
#' the correct sheet. All we need to do next is read that sheet into R. We can do
#' that using the `read_excel` function.
#' 
#' Recall that the actual data starts on row 7, so we want to skip the first 6
#' rows.
#' 
## ------------------------------------------------------------------------
readTable1 <- function(file) {
  read_excel(file, sheet = findTable1(file), skip = 6)
}

boysNames <- map(boy.file.names, readTable1)
glimpse(boysNames[[1]])

#' 
#' 
#' Data cleanup
#' ================
#' 
#' Now that we've read in the data we still have some cleanup to do. Specifically, we need
#' to:
#' 
#' 1. fix column names
#' 2. get rid of blank row and the top and the notes at the bottom
#' 3. get rid of extraneous "changes in rank" columns if they exist
#' 4. transform the side-by-side tables layout to a single table.
#' 
#' In short, we want to go from this:
#' 
#' ![messy](images/messy.png)
#' 
#' to this:
#' 
#' ![tidy](images/clean.png)
#' 
#' There are many ways to do this kind of data manipulation in R. We're going to
#' use the *dplyr* and *tidyr* packages to make our lives easier. Both packages
#' were attached along with the *tidyverse* package.
#' 
#' Fixing column names
#' -------------------------
#' The column names are in bad shape. In R we need column names to a) start with a
#' letter, b) contain only letters, numbers, underscores and periods, and c)
#' uniquely identify each column.
#' 
#' The actual column names look like this:
## ------------------------------------------------------------------------
names(boysNames[[1]])

#' 
#' So we need to a) make sure each column has a name, and b) distinguish between
#' the first and second occurrences of "Name" and "Count". We could do this
#' step-by-step, but there is a handy function in R called `make.names` that will
#' do it for us.
#' 
## ------------------------------------------------------------------------
names(boysNames[[1]])
make.names(names(boysNames[[1]]), unique = TRUE)
setNames(boysNames[[1]], make.names(names(boysNames[[1]]), unique = TRUE))
names(boysNames[[1]])

#' 
#' Of course we need to iterate over each data.frame in the `boysNames` list and to
#' this for each one. Fortunately the `map` function makes this easy.
#' 
## ------------------------------------------------------------------------
boysNames <- map(boysNames,
                 function(x) {
                     setNames(x, make.names(names(x), unique = TRUE))
                 })

#' 
#' Filtering rows
#' ------------------
#' 
#' Next we want to remove blank rows and rows used for notes. An easy way to do
#' that is to remove rows that don't have a name. We can filter on some condition
#' using the `filter` function, like this:
#' 
## ------------------------------------------------------------------------
boysNames[[1]]
boysNames[[1]] <- filter(boysNames[[1]], !is.na(Name))
boysNames[[1]]

#' 
#' Of course we need to do that for every data set in the `boysNames` list, but
#' I'll leave that to you.
#' 
#' Selecting columns
#' ----------------------
#' 
#' Next we want to retain just the `Name`, `Name.1` and `Count`, `Count.1` columns.
#' We can do that using the `select` function:
#' 
#' 
## ------------------------------------------------------------------------
boysNames[[1]]
boysNames[[1]] <- select(boysNames[[1]], Name, Name.1, Count, Count.1)
boysNames[[1]]

#' 
#' Again we will want to do this for all the elements in `boysNames`, a task I
#' leave to you.
#' 
#' Re-arranging into a single table
#' -----------------------------------------
#' 
#' Our final task is to re-arrange to data so that it is all in a single table
#' instead of in two side-by-side tables. For many similar tasks the `gather`
#' function in the *tidyr* package is useful, but in this case we will be better
#' off using a combination of `select` and `bind_rows`.
#' 
## ------------------------------------------------------------------------
boysNames[[1]]
bind_rows(select(boysNames[[1]], Name, Count),
          select(boysNames[[1]], Name = Name.1, Count = Count.1))

#' 
#' Exercise: Cleanup all the data
#' =========================================
#' 
#' In the previous examples we learned how to drop empty rows with `filter`, select
#' only relevant columns with `select`, and re-arrange our data with `select` and
#' `bind_rows`. In each case we applied the changes only to the first element of
#' our `boysNames` list. Your task now is to use the `map` function to apply each
#' of these transformations to all the elements in `boysNames`.
