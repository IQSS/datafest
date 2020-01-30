
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
  
  ## add code to create sliderInput to select a year.
  ## see ?sliderInput
  sliderInput("year", "Select year to display",
              value = 1990,
              min = min(storms_by_year$year),
              max = max(storms_by_year$year), 
              step = 1,
              sep = ""),
  
  tableOutput("byYearTable")
  
  )

server <- function(input, output, session) {
  
  output$byYearTable <- renderTable({
    #str(input$year)
    storms_filtered <- filter(storms_by_year, year == input$year) 
    storms_filtered
  },
  digits = 0)
  
}

shinyApp(ui, server)