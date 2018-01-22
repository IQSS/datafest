# script info: https://towardsdatascience.com/using-r-to-merge-the-csv-files-in-code-point-open-into-one-massive-file-933b1808106
wd <- "C:/R_TEMP/data/concat"
setwd(wd)
filenames <- list.files(full.names=TRUE)
All <- lapply(filenames,function(i){
read.csv(i, header=TRUE, skip=0)
})
df <- do.call(rbind.data.frame, All)
head(df)
write.csv(df,"../merge_states.csv", row.names=FALSE)