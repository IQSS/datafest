## ----attach packages-----------------------------------------------------
library(tidyverse)
library(stringr)
library(readxl)
library(purrr)

## ----get list of data file names-----------------------------------------
boy.file.names <- list.files("babyNamesData/boys", full.names = TRUE)

## ----iterate over file names using map-----------------------------------
map(boy.file.names, excel_sheets)

## ----function to identify sheet with table 1 in the name-----------------
findTable1 <- function(x) {
  str_subset(excel_sheets(x), "Table 1")
}

map(boy.file.names, findTable1)

## ----function to read table one from excel file--------------------------
readTable1 <- function(file) {
  read_excel(file, sheet = findTable1(file), skip = 6)
}

boysNames <- map(boy.file.names, readTable1)
glimpse(boysNames[[1]])

## ----examine the names from the excel sheet------------------------------
names(boysNames[[1]])

## ----cleanup the names---------------------------------------------------
names(boysNames[[1]])
make.names(names(boysNames[[1]]), unique = TRUE)
setNames(boysNames[[1]], make.names(names(boysNames[[1]]), unique = TRUE))
names(boysNames[[1]])

## ----use map to cleanup all the names------------------------------------
boysNames <- map(boysNames,
                 function(x) {
                     setNames(x, make.names(names(x), unique = TRUE))
                 })

## ----remove empty rows---------------------------------------------------
boysNames[[1]]
boysNames[[1]] <- filter(boysNames[[1]], !is.na(Name))
boysNames[[1]]

## ----select just the columns of interest---------------------------------
boysNames[[1]]
boysNames[[1]] <- select(boysNames[[1]], Name, Name.1, Count, Count.1)
boysNames[[1]]

## ----stack to two halves of the data-------------------------------------
boysNames[[1]]
bind_rows(select(boysNames[[1]], Name, Count),
          select(boysNames[[1]], Name = Name.1, Count = Count.1))


## ---- exercise solution -------------------------------------------------

boysNames <- map(boysNames, function(x) {
    filtered <- filter(x, !is.na(Name)) # drop rows with no Name value
    selected <- select(filtered, Name, Count, Name.1, Count.1) # select just Name and Count columns
    bind_rows(select(selected, Name,  Count), # re-arrange into two columns
              select(selected, Name = Name.1, Count = Count.1))
})

## Add year column
boysNames <- map2(boysNames,
                  1996:2015,
                  function(df, year) {
                      mutate(df, Year = year)
                  })

## combind into a single data.frame
boysNames <- bind_rows(boysNames)

## order names by frequency

boysNames <- mutate(boysNames,
                    Name = factor(Name, levels = unique(Name), labels = tolower(unique(Name))),
                    Name = reorder(Name, Count)
                    )

## plot
library(ggplot2)

ggplot(boysNames, aes(x = Name, y = Count, color = factor(Year), fill = factor(Year))) +
    geom_bar(stat = "identity") +
    theme(axis.text.x = element_text(size = 7, angle = 90),
          legend.position = "top")
