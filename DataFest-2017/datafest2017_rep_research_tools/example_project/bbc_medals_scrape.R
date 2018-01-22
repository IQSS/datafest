#################
# Scrape BBC Sochi Olympics Medals Table
# Christopher Gandrud
# MIT License
#################

# Load packages
library(rvest)
library(dplyr)
library(knitr)

# URL with the medals table
URL <- 'http://www.bbc.com/sport/winter-olympics/2014/medals/countries'

#### Gather content and parse the table, note there is only one table ####
table <- URL %>% read_html() %>%
    html_nodes('table') %>%
    html_table() %>% 
    as.data.frame

#### Clean ####
# Drop unwanted variables
medals <- select(table, Country, Var.3, Var.4, Var.5, Total)

# Give new variable names
names(medals) <- c('country', 'gold', 'silver', 'bronze', 'total')

# Sort by total medals in descending order
medals <- arrange(medals, desc(total))
