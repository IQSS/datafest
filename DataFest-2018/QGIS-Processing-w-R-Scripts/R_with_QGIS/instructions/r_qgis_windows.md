## Data Fest 2018   

### QGIS Processing with R Scripts

#### Windows Version

[Data and Instructions](https://github.com/vajlex/R_with_QGIS)

Instructor:  [Lex Berman](http://www.iq.harvard.edu/people/lex-berman)

**Overview:  This session will introduce setup and use of R within QGIS.**

*NOTE:*  We will start in RStudio, then use QGIS (for Windows to show integration of R Scripts within QGIS Processing Toolbox).   For Mac OSX users, the R Scripts may not function (depending on your installation and "System Integrity Protection"), but all R scripts can be run in RStudio and the outputs loaded into QGIS to achieve the same results.


### setup options

1.  Install the software:  R, RStudio, QGIS

2.  Open RStudio to verify that the R installation is working

3.  In RStudio install these packages:
```
data.table
sp   
ggplot2   
ggmap
```
3.  Open QGIS Desktop 2.18

4.  Under the main menu: Processing > Options > Providers > R

5.  Note path of "R folder"  and verify this is correct on your system

6.  Make sure the Activate box is CHECKED for R

7.  Click OK for the options settings

8.  Note warnings, such as "Wrong Parameter for MSYS folder"

9.  In the settings for Processing > Options > Providers > GRASS commands  (not GRASS GIS 7 commands)  delete any paths under the *Msys folder, GRASS folder, Location of GRASS docs* options.  Make sure the GRASS Commands Activate box is UNCHECKED, then hit OK

10.  If you do not receive warnings, we are ready to test R!

### processing toolbox

1.  Open the main menu item Processing > Toolbox

2.  In the Toolbox Panel, expand the R Scripts > Tools menu tree,  you should see items for *Create new R script* and *Get R Scripts from on-line*...

3.  click on  *Get R Scripts from on-line* then *Not installed* tree.  You should see many functions and scripts that you can simply check to add to your R scripts locally.  For example, lets CHECK *Scatterplot types* and OK

4.  now you should have a new branch under R Scripts > Tools  called *Vector Processing* and under this branch you will find the function *Scatterplot types*.  If you right-click on a tool, you have opttions to EDIT, EXECUTE and DELETE the script.

5.  Now let's try the *Create new R script* tool, which opens an editor. 

6.  Go to our sample script and view the [raw content](https://github.com/vajlex/R_with_QGIS/blob/master/r_script/bird_data.rsx) then COPY the script and PASTE it into the QGIS R Script Editor

7.  Click Save As and note that the default folder is the location that is currently defined under Processing > Options > Providers > R > R User Library Folder.  give your script a filename, such as *test_script* and hit SAVE

8.  If you CLOSE the Script Editor, you will now see a new branch in the Toolbox under R Scripts called "User R Scripts" and this should contain your "test_script"

9.  Right click on the *test_script* tool and you can EDIT, EXECUTE or DELETE.  We will click on EDIT to examine the script.

10. Note that the first line in the script calls the library "data.table" and we have not INSTALLED that library in our local R instance.   Therefore we should keep in mind that you must first install any dependencies and libraries in R (or RStudio) BEFORE attempting to run the R Script in QGIS.   QGIS does not have the ability to install libraries, so we will first launch RStudio.

11.  In RStudio console, run  
```
  test.data.table  
```
In a fresh install, you will probably get "Error:  object 'test.data.table' not found

12.  In RStudio console, run 
```
    install.packages("data.table")
```
13.  Then run
```
    require(data.table)
    test.data.table
```
Now you should get some output about the data.table package

14.  Having installed our main package, return to QGIS R Script Editor.  the next issue to sort out is the location and path to our data file.   IN the sample script, the command is to set the working directory here:
```
    wd <- "C:/R_TEMP/data"
```    
Therefore, the easiest way to proceed is to create the folder at the root of C: drive called R_TEMP and move our data folder there.  At this point you should simply grab the complete .zip archive to download from github repo, [R_with_QGIS](https://github.com/vajlex/R_with_QGIS).   Once you have the .zip uncompressed, move the "data" folder to R_TEMP.  Then the path to your data should exist.

15.  Review the test_script to understand the functions that we will run in R, then note that the final line is to write the manipulated and selected data into a new .txt file.   

16.  While in the script editor, click on the gear button to EXECUTE the script.  A console window will open.  Click RUN on the lower right to execute.   The progress of the algorithm will be noted on the console.  After running, the window will close.  Go to the working directory to see if the designated output file *fixed_birds* has been generated.

17.  If you find the *fixed_birds_data* file with content, then R has successfully run within QGIS!


### Bringing R analytical results into QGIS

1.  Now that we have generated a new .txt file using R, let's add the file to QGIS with the https://github.com/vajlex/R_with_QGIS

2.  Use the Add Delimited Text Layer button and browse to the *fixed_birds_data.txt* file.  Set the File Format to CUSTOM DELIMITERS.   Click COMMA, then TAB, then SPACE, until you find the delimiter that correctly separates the content into columns (as shown in the live PREVIEW at the bottom of the form).  In our case, it should be SPACE that correctly delimits the content. 

3.  Make sure the box for *First record has field names* is checked

4.  Next we must make sure that the correct fields have been used for the X Field and Y Field values.  In this case, QGIS has guessed that X Field = "LONGITUDE"  and Y Field = "LATITUDE".  Take a visual look at the data in the PREVIEW area to see if this looks correct.  Those values should be numbers in decimal degrees.

5.  Now we can hit OK and we will be prompted to specify the Coordinate Reference System (CRS) or Projection definition.  We can accept the default global projection in decimal degrees:  WGS 84.  Then hit OK and the data should be imported as points into QGIS

6.  In the LAYERS PANEL, right click on the layer we have imported, called "fixed_birds_data"  then ZOOM TO LAYER.   The Map View will recenter on the extent containing all the imported data.   Note that our original R Script (which eliminated any data with the STATE VALUE of OHIO) has worked properly in filtering the data, and putting the x, y values in the proper fields.

7.  In order to run further spatial analysis tasks on our data, right click on the layer *fixed_birds_data*  and SAVE AS a new ESRI SHAPEFILE, for example:   C:\R_TEMP\shape\fixed_birds.shp

8.  The new Shapefile layer will be added to the QGIS project.   Right-click on the original fixed_birds_data.txt layer and REMOVE it from the project.  Now we have brought our working data into QGIS and left the original R analysis .txt file untouched.

### Spatial Analysis in QGIS

1.  There are many geoalgorithms and cartographic tools available in QGIS.  For this case, we will just use a quick Selection and Heatmap to show you some of the potential.

2. Right-click on *fixed_birds* shapefile layer and OPEN ATTRIBUTE TABLE.  Note that we can sort and filter on the content of these columns, such as "COMMON.NAM"
Click on the E "expression" button to open the SQL Expression window.  First enlarge this window horizontally (so we will be able to see all three vertical panels).  Then expand the options in the center panel for "Fields and Values."   In this tree DOUBLE-CLICK on the field:  *COMMON.NAM* and it will appear in our Expression form on the left.   

3. Next we go to the OPERATORS options tree in the center panel and expand it.  Double-click on the LIKE operator and it will appear afer "COMMON.NAM" in the Expression form.

4. Now return to the Fields and values section to click ONCE on the *COMMON.NAM* item.  After the *COMMON.NAM* item is highlighted, click ALL UNIQUE at the lower right.  This should load all the distinct values that occur in the highlight field:  *COMMON.NAM*  Then double-click on one of the values shown in the list on the lower right, for example:  'GREAT BLUE HERON'   Now this Value should be added to the Expression form for a complete SQL Query Expression:
```
    "COMMON.NAM" LIKE 'Great Blue Heron'
```    
5.  Click the SELECT button lower right to run the query.  Close the Expression Window, and examine the ATTRIBUTE TABLE.  The top line should indicate that out of the total number of point features 126136, the Query has selected 42455  which are matching 'Great Blue Heron' in the COMMON.NAM field.   Now CLOSE the Attribute Table.  You should see a scattering of the selected features on the Map View.
_[NOTE: Because more than one feature can occur at the SAME x, y coordinates, seeing the distribution and density from the initial selection is not going to give an accurate impression of the real spatial phenomenon.]_

6. Now right-click on the Fixed_birds layer and SAVE AS a new Esri Shapefile, called "blue_heron.shp" which will open a dialog window.   In this SAVE AS window be SURE to CHECK the "save only selected features" checkbox!  Otherwise you will end up saving the entired layer of 126136 features into a new file.   Having entered the file name and checked Save Only Selected hit OK.   The new layer should appear in the Layer List and be added to the Map View.

7.  Turn off the rendering of the original data layer, fixed_birds, by UNCHECKING it in the Layers Panel.  Now you should be viewing only the Blue Heron features, which you can check by right-clicking to OPEN ATTRIBUTE TABLE and see number of features.

8.  Now we will use the built-in Kernel Density function, or HEATMAP.  Go to the PLUGINS > Manage and Install Plugins menu, which loads all available plugins.  type HEATMAP in the Search box, and then CHECK the Heatmap item shown in the results to install the plugin.  Close the Plugins window.   

9. Having installed the plugin, we can now go to the menu Raster > Heatmap > Heatmap  which will open a window for kernel density options.  Note the default distance in the Radius field will be in map layer units!  Since our layer is in a plain decimal degree projection (WGS 84), the radius of 20000 degrees is extremely large.  This is deceptive, because the value is actually going to be calculated as 20000 meters (approximately 12 miles).  In any case, let us accept the default value and choose a filename, like "heat1" then hit OK to run our kernel density algorithm.

10.  The result will load into the Layers Panel and map view.  Now we can see that, purely as a function of the number of bird observations that are closer to one another, where are the most common places to see the Great Blue Heron!


### Comparison with other spatial data

1.  Although we have run some spatial analysis on the occurrence of sightings for the Great Blue Heron, let us introduce another dataset for the purposes of comparison.

2.  For example we could examine the locations of State Parks in the area of study, to see if the areas where sightings are most frequest occur in a designated park, or just for convenience in labeling the parks for cartography.

3. In our _data_ folder that we downloaded and moved to C:\R_TEMP\data  we should have a sub-folder called _concat_.   In this folder there are four files containing parks information for the states:  NH, MA, ME, VT.   Now we want to merge (or concatenate) these files into a single .csv file.

4.  NOTE:  this data was extracted from the USGS Board of Geographich Names, GNIS Features, available here:  https://geonames.usgs.gov/domestic/download_data.htm   After downloading and unzipping the data, each state is imported to QGIS using the "add delimited text" tool.   The selection for each state is made to find only the features designated as "parks" using the EXPRESSION Query:  
```
"FEATURE_CLASS" LIKE 'parks'
```
The selected rows were then exported to .csv files, separately.

5. Now we can run the "concat_states.rsx" script, or create a new script in our QGIS R Scripts tools, then paste the contents of the script located here:
https://github.com/vajlex/R_with_QGIS/blob/master/r_script/concat_states.rsx

6. Once we have the R script created and saved, we can EXECUTE the script, then in the console click RUN.

7. When the script is finished, the console will close.  Check the list of files in the folder:  C:\R_TEMP\data\concat   where we should have a new file:  merge_states.csv

8. If we open the merge_states.csv we'll see that the Field Names were lost in the merge function, we can add them back (see the field_names.csv file in the Concat folder).

8.  In QGIS we can use the "add delimited text" tool to import merge_states.csv into our map project.   Note that the field containing X Coordinate (Longitude) is called LONG_DD,  and the field containing Y Coordinate (Latitute) is called LAT_DD. 

9.  Having added the .csv layer, we can see that there are some points included that are clearly NOT in New England states.   First let's right click on the layer and SAVE AS a new shapefile (which gives us full editing and analysis abilities).  Once the new Shapefile Layer is added to our project, right click on the .csv layer and REMOVE it from the layers list.

10. We can click on the PENCIL icon (Edit Layer tool) to make the active layer editable.  Then using the SELECT by rectangle tool, we can easily select the points that are outside of New England, CUT them, and click the PENCIL icon to accept the changes.  Now, right-click and Zoom to Layer should bring us back to New England.

11.  From here we can place the parks over our Herons heatmap and zoom in to an area of interest.   By selecting a few parks that overlap the highest frequency areas of blue heron sightings, we can SAVE AS (selected features only) to a new layer.  Then, in the PROPERTIES > Labels menu for the parks we have selected, we can Label them to provide contextual info about the areas of highest frequency.

12.  Finally, we could go to Project > New Print Composer to set up a map layout for printing, or exporting at high resolution (for publication).



