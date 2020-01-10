## Goal: Layout the application elements in a more appealing way.


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
  
  selectInput("stormStatus",
              label = "Filter by storm type: ",
              choices = unique(stormNames$status)),
  
  "The plot below shows the distribution of storm name use.",
  plotOutput("nameDist")
)

server <- function(input, output, session) {
  
  
  output$nameDist <- renderPlot({
    
    str(input$stormStatus)
    
    names_filtered <- filter(stormNames, status == input$stormStatus)
    hist(names_filtered$count)

  },
  width = 400, height = 300)
  
}

shinyApp(ui, server)