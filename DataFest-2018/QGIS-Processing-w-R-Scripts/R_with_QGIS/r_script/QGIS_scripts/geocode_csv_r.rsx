
# Geocoding a csv column of "addresses" in R
# Source:  https://gist.github.com/aleszu/04a486ec0c3f61a8e7ce8f9b37d9e986#file-geocode-csv-r

#load ggmap
library(ggmap)

# Select the file from the file chooser
fileToLoad <- file.choose(new = TRUE)


# Read in the CSV data and store it in a variable 
origAddress <- read.csv(fileToLoad, stringsAsFactors = FALSE)

# Initialize the data frame
geocoded <- data.frame(stringsAsFactors = FALSE)

# Loop through the addresses to get the latitude and longitude of each address and add it to the
# origAddress data frame in new columns lat and lon
for(i in 1:nrow(origAddress))
{
  # Print("Working...")
  result <- geocode(origAddress$addresses[i], output = "latlona", source = "google")
  origAddress$lon[i] <- as.numeric(result[1])
  origAddress$lat[i] <- as.numeric(result[2])
  origAddress$geoAddress[i] <- as.character(result[3])
}
# Write a CSV file containing origAddress to the working directory
# path is set to Windows directory   remove escapes for Mac
write.csv(origAddress, "C:\\R_TEMP\\geocode\\geocoded.csv", row.names=FALSE)
