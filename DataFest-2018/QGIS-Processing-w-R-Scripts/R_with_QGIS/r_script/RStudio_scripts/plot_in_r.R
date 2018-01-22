# plot_in_R
# see complete tutorial:  https://github.com/tacormier/FOSS4G_Boston2017/blob/master/Workshop_rstats/Part3_VectorData
# be sure the libraries are installed first
##
library(data.table) 
library(ggplot2) 
##
wd <- "C:/R_TEMP/data"
setwd(wd)

# Re-open cleaned birds txt file
birds <- fread("fixed_birds_data.txt", sep=" ")
# Convert to spatial points df
# Although we've plotted the points, we haven't yet defined our birds data table as
# a spatial object. First, which columns are the coordinates?
birds.xy <- birds[,c("LONGITUDE", "LATITUDE")]
birds.sp <- SpatialPointsDataFrame(coords=birds.xy, data=birds, proj4string = CRS("+proj=longlat +datum=WGS84 +ellps=WGS84 +towgs84=0,0,0"))
birds.sp

# Visualize
plot(birds.sp)

# We could write this out to a shapefile if we want to now:
# shapefile(birds.sp, "fixed_birds_sp.shp", overwrite=T)
# Thanks ESRI - cut our field names. How about a geojson file instead?
# writeOGR(birds.sp, "fixed_birds_geojson.geojson", layer="birds", driver="GeoJSON")

# to plot maps with color ramps, scalebars, etc see full tutorial above