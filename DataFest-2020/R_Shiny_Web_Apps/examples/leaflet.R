library(shiny)
library(leaflet)
library(dplyr)

data(storms)
hurricanes <- filter(storms, year >= 2000 & status == "hurricane") %>%
  mutate(ID = n())
ui <- fluidPage(
  
)

server <- function(input, output, session) {
  
}

shinyApp(ui, server)





