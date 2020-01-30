## Goal: display storm name counts in a shiny app.

library(shiny)
library(dplyr)

data(storms)

stormNames <- storms %>%
  select(name, year) %>%
  distinct() %>%
  group_by(name) %>%
  summarize(count = n()) %>%
  arrange(desc(count))

ui <- fluidPage(
  "The most common storm name is",
  textOutput("topNameText", inline = TRUE),
  
  p("The table below shows the most common storm names."),
  tableOutput("topNamesTable"),
  
  "The plot below shows the distribution of storm name use.",
  plotOutput("nameDist")
)

server <- function(input, output, session) {
  
  output$topNameText <- renderText({
    slice(stormNames, 1)$name
    })
  
  output$topNamesTable <- renderTable({
    slice(stormNames, 1:5)
  })
  
  
  output$nameDist <- renderPlot({
    hist(stormNames$count)
  })
  
}

shinyApp(ui, server)