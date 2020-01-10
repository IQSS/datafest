library(shiny)
library(leaflet)
library(dplyr)

data(storms)
hurricanes <- filter(storms, year >= 2000 & status == "hurricane") %>%
  mutate(ID = n())

ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      selectInput("storm", label = "Choose a storm:", choices = sort(unique(hurricanes$name)))
    ),
    mainPanel(
      leafletOutput("stormMap")
    )
  )
)

server <- function(input, output, session) {
  output$stormMap <- renderLeaflet({
    mapData <- filter(hurricanes, name == input$storm)
    str(input$stormMap_marker_click)
    leaflet(mapData) %>%
    addCircleMarkers(lat = ~lat, lng = ~long,
                     layerId = ~ID,
                     radius = ~hu_diameter*.1) %>%
    addTiles()
  })
}

shinyApp(ui, server)





