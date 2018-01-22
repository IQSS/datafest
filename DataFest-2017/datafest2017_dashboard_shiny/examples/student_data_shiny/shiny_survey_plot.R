# ----------------------------------
# R code for survey shiny simple example
# MIT License
# ----------------------------------

# Global set up chunk ---------------
# Load packages
library(gsheet)
library(dplyr)
library(plotly)

# Download survey data
# Download data
URL <- 'https://docs.google.com/spreadsheets/d/1QQkVYYdAPYjCQRO1Oupqze7Q8WULkfJ_cmDvJERumU4/edit#gid=317007960'
student_data <- gsheet2tbl(URL)

# Simplify variable names
names(student_data) <- c('timestamp', 'position', 'r_experience',
                         'dashboard_experience', 'hometown',
                         'rmarkdown_experience')

# Relevel factors
positions <- c("Undergraduate student", "Graduate student",
               "Harvard staff", "Harvard faculty")

student_data$position <- factor(student_data$position, levels = positions)

r_skills <- c("Basic", "Intermediate", "Advanced")
student_data$r_experience <- factor(student_data$r_experience, levels = r_skills)



# Input chunk ---------------------
selectInput("position", label = "Select Particpants' Position",
            choices = positions, selected = 'Harvard faculty')


# Output chunk ---------------------
renderPlot({
    # Subset data
    data_sub <- subset(student_data, position == input$position)

    # Find position counts
    r_exp <- table(data_sub$r_experience)

    # Bar plot
    barplot(r_exp)

})
