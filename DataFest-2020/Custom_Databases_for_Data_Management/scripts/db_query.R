script_dir <- dirname(sys.frame(1)$ofile)
library(RSQLite)
connection <- dbConnect(SQLite(), paste(script_dir, "survey.db", sep = "/"))
results <- dbGetQuery(connection, "SELECT Site.lat, Site.long FROM Site;")
print(results)
dbDisconnect(connection)

