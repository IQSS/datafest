# Plot session participant dashboard experience
# Find exerpience
dash_exp <- table(student_data$dashboard_experience) %>% data.frame

# Plot
plot_ly(data = dash_exp, x = ~Var1, y = ~Freq) %>%
    layout(xaxis = list(title = ''),
           yaxis = list(title = 'Frequency'))
