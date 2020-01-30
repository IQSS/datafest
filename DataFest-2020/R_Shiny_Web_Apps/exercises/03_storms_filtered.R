## Exercise 3: Enable user input to select a year

## 1. Add a sliderInput element to the ui .

## 2. Modify the renderTable expression to filter the year displayed to the one selected by the user.

library(shiny)
library(dplyr)

data(storms)
storms_by_year <- storms %>%
  group_by(year) %>%
  summarize(n = n_distinct(name))

ui <- fluidPage(
  
  ## add code to create sliderInput here to filter by year.
  ## see ?sliderInput
  
  tableOutput("byYearTable")
  
  )

server <- function(input, output, session) {
  
  output$byYearTable <- renderTable({
    storms_filtered <- ## add code to filter by input here 
    storms_filtered
  })
  
}

shinyApp(ui, server)