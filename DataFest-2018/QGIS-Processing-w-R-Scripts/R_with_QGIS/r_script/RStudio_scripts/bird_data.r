library(data.table)
wd <- "C:/R_TEMP/data"
setwd(wd)
system.time(birds <- fread("ebd_NE_4spp_workshopData.txt", sep=" "))
#swap the values x y in your columns in place rather
# than creating new columns.  the values were in the wrong columns.
birds[ , c("LATITUDE", "LONGITUDE")] <- birds[ , c("LONGITUDE","LATITUDE")]
#trim OHIO out of the sample
birds <- birds[birds$STATE_PROVINCE != 'Ohio',]
unique(birds$STATE_PROVINCE)
# fix count field to be numeric (instead of string)
birds$OBSERVATION.COUNT <- as.numeric(birds$OBSERVATION.COUNT)
# write out table
write.table(birds, "fixed_birds_data.txt", row.names=F)
