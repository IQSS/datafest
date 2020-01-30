
## Exercise 4: Layout and themes

## 1. Lay out this application using `navbarPage` and `tabPanel`
## See https://shiny.rstudio.com/articles/layout-guide.html#navbar-pages
## for examples.

## 2. Use html tags (e.g., `h2()`, `p()`, `a()`) to add some descriptive text to your application.

## 3. Use the `shinythemes` package (install if needed) to change the theme used by your app.
## See https://rstudio.github.io/shinythemes/ for examples.


library(shiny)
library(dplyr)
library(leaflet)

data(storms)
storms_by_year <- storms %>%
  group_by(year) %>%
  summarize(n = n_distinct(name))

## Change fluidPage to navbarPage
ui <- fluidPage(
  title = "Storms", 
  
  ## add tabPanel elements to layout this application
  sliderInput("year", "Select year to display",
              value = c(1995, 2000),
              min = min(storms_by_year$year),
              max = max(storms_by_year$year), 
              step = 1,
              sep = ""),
  
  tableOutput("byYearTable"),
  
  selectInput("storm",
              label = "Choose a storm",
              choices = unique(storms$name)),
  
  leafletOutput("stormMap")
  
  )

server <- function(input, output, session) {
  
  output$byYearTable <- renderTable({
    #str(input$year)
    storms_filtered <- filter(storms_by_year, year >= input$year[1] & year <= input$year[2]) 
    storms_filtered
  },
  digits = 0)
  
  output$stormMap <- renderLeaflet({
    mapData <- filter(storms, name == input$storm)
    leaflet(mapData) %>%
      addCircleMarkers(lat = ~lat, lng = ~long,
                       radius = ~hu_diameter*.1) %>%
      addTiles()
  })
  
}

shinyApp(ui, server)