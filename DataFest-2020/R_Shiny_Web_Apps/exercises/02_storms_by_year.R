
## Exercise 2: Display number of storms by year.

## 1. Add a table output element to the ui and a corresponding renderer to the server.
##    The table should display the number of named storms in each year.

## 2. Add a plot output element to the ui, and a corresponding renderer to the server.
##    The plot should display the number of named storms in each year.


library(shiny)
library(dplyr)

data(storms)
storms_by_year <- storms %>%
  group_by(year) %>%
  summarize(n = n_distinct(name))

ui <- fluidPage(

  )

server <- function(input, output, session) {
  
}

shinyApp(ui, server)