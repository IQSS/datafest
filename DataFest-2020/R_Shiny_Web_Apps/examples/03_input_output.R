## Goal: Enable filtering by storm status.

library(shiny)
library(dplyr)

data(storms)

stormNames <- storms %>%
  select(name, year, status) %>%
  distinct() %>%
  group_by(name, status) %>%
  summarize(count = n()) %>%
  arrange(desc(count))

ui <- fluidPage(
  
  "The plot below shows the distribution of storm name use.",
  plotOutput("nameDist")
)

server <- function(input, output, session) {
  
  output$nameDist <- renderPlot({
    hist(stormNames$count)
  })
  
}

shinyApp(ui, server)