## Goal: Add client-side interactivity using htmlwidgets.


library(shiny)
library(DT)
library(plotly)
library(dplyr)

data(storms)

storms <- storms %>%
  mutate(time = as.POSIXct(paste(year, month, day, hour, sep = "-"),
                           format = "%Y-%m-%d-%H"))

stormsUnique <-  storms %>%
  select(name, year) %>%
  distinct()

ui <- fluidPage(
  
  titlePanel("Storm Wind Speed"),
  
  sidebarLayout(

    sidebarPanel(
      dataTableOutput("nameTable")
    ),
    
    mainPanel(
      p("The plot below shows windspeed for the selected storm."),
      plotlyOutput("windSpeed")
    )
  )
)

server <- function(input, output, session) {
  
  output$nameTable <- renderDataTable({
    stormsUnique
    },
    selection = "single")
  
 
  output$windSpeed <- renderPlotly({
    
    str(reactiveValuesToList(input))
    
    req(input$nameTable_row_last_clicked)
    
    stormRow <- slice(stormsUnique, as.integer(input$nameTable_row_last_clicked))
    
    storms_filtered <- storms %>%
      filter(name == stormRow$name & year == stormRow$year) %>%
      select(time, wind)
  
    plot_ly(storms_filtered, x = ~time, y = ~wind) %>%
      add_markers() %>%
      add_lines()
  })
  
}

shinyApp(ui, server)