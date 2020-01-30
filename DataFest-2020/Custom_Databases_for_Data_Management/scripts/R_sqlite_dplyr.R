#
# R and dplyr for use with SQLite databases
#

install.packages(c('RSQLite','dplyr','dbplyr'))

#library('RSQLite')
#library('dplyr')
#library('dbplyr')

#connection <- DBI::dbConnect(RSQLite::SQLite(), "/Users/Shared/datafest/survey.db")




### Standard SQL
# import our required packages
library('RSQLite')

# open the database connection
connection <- dbConnect(SQLite(), "/Users/Shared/datafest/survey.db")

# execute and fetch the results
results <- dbGetQuery(connection, "SELECT Site.lat, Site.long FROM Site;")

# print 'em out
print(results)

# close the connection
dbDisconnect(connection)



### Somewhat using dplyr
# import our required packages
#
# HAS PROBLEMS!!
#
#library('RSQLite')
library('dplyr')

connection <- DBI::dbConnect(RSQLite::SQLite(), "/Users/Shared/datafest/survey.db")
#connection <- src_sqlite("/Users/Shared/datafest/survey.db")

# execute and fetch the results
results <- tbl(connection, sql("SELECT Site.lat, Site.long FROM Site"))

# print 'em out
print(results)

# close the connection
dbDisconnect(connection)
dbDisconnect(connection)
detach(name = package:dplyr)


# real dplyr with dbplyr
#
library(dplyr)
#library(dbplyr)

connection <- DBI::dbConnect(RSQLite::SQLite(), "/Users/Shared/datafest/survey.db")
src_dbi(connection)
# sql
results <- tbl(connection, sql("SELECT Site.lat, Site.long FROM Site"))
results
str(results)
# dplyr
sites <- tbl(connection, "Site")
str(sites)
sites %>% 
  select(lat, long)
dbDisconnect(connection)


# Simple query and filter
# find readings out of range:
# SELECT * FROM Survey WHERE quant = 'sal' AND ((reading > 1.0) OR (reading < 0.0));
connection <- DBI::dbConnect(RSQLite::SQLite(), "/Users/Shared/datafest/survey.db")
src_dbi(connection)
survey <- tbl(connection, "Survey")
survey %>% 
  select(person, quant, reading) %>% 
  filter(quant == 'sal',
         reading > 1 | reading < 0)

# what did it do?
survey %>% 
  select(person, quant, reading) %>% 
  filter(quant == 'sal',
         reading > 1 | reading < 0) %>% 
  show_query()

# collect data
salinity_readings <- survey %>% 
  select(person, quant, reading) %>% 
  filter(quant == 'sal',
         reading > 1 | reading < 0)
salinity_readings

dbDisconnect(connection)


# do a join
# SELECT * FROM Visited JOIN Survey ON Survey.taken = Visited.id and person = "lake" ORDER BY quant ASC;

library(dplyr)
library(dbplyr)

connection <- DBI::dbConnect(RSQLite::SQLite(), "/Users/Shared/datafest/survey.db")
src_dbi(connection)
survey <- tbl(connection, "Survey")

both <- left_join(survey, tbl(connection, "Visited"),
                   by = c("taken" = "id")) %>% 
  filter(person == "lake") %>%
  arrange(quant)
both
explain(both)

dbDisconnect(connection)
