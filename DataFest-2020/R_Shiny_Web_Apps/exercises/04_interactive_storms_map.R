
## Exercise 5: Interactive Storms Map

## 1. Run the app and click on the blue markers. Examine the output in 
##    the console to determin the input corresponding to the row number 
###   of the clicked observation.

## 2. Use the slice function to select the row corresponding
##    to the clicked marker from the storms data frame and return
##    this row to the stormDetails output on line 65.


library(shiny)
library(dplyr)
library(leaflet)
library(DT)

data(storms)
storms <- storms %>% 
  mutate(ID = 1:nrow(storms))

stormsUnique <-  storms %>%
  select(name, year) %>%
  distinct()

ui <- fluidPage(
  
  titlePanel("Storm Paths"),
  
  sidebarLayout(
    
    sidebarPanel(
      dataTableOutput("nameTable")
    ),
    
  mainPanel(
  
  leafletOutput("stormMap"),
  
  dataTableOutput('stormDetails')
  
  )))

server <- function(input, output, session) {
  
  output$nameTable <- renderDataTable({
    stormsUnique
  },
  selection = "single")
  
  output$stormMap <- renderLeaflet({
    req(input$nameTable_row_last_clicked)
    
    stormRow <- slice(stormsUnique, as.integer(input$nameTable_row_last_clicked))
    
    mapData <- storms %>%
      filter(name == stormRow$name & year == stormRow$year)
    
    leaflet(mapData) %>%
      addCircleMarkers(lat = ~lat, lng = ~long,
                       radius = ~hu_diameter*.2,layerId = ~ID) %>%
      addTiles()
  })
  
  output$stormDetails <- renderDataTable({
    
    ## This prints the current input values to the consule.
    ## Run the app and interact with it to determin which input 
    ## gives you the row number of the last clicked marker on
    ## the map.
    str(reactiveValuesToList(input))
    
    ## Use the slice function to select the row corresponding
    ## to the clicked marker from the storms data frame.

    
  })
  
}

shinyApp(ui, server)