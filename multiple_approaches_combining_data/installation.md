## Installation Instructions for *Multiple Approaches to Combining Data*

Our hands-on session will be focusing on using SQLite3 as a lightweight, local database engine. We will primarily use materials and software from the Software Carpentry's [Databases & SQL lesson](http://swcarpentry.github.io/sql-novice-survey/). And we will extend these to include demonstrating the use of SQLite from within Stata via an ODBC connection. Although there are multiple layers to this hands-on, the installation per platform is rather straightforward. Let's dig in!

### Data Files

1. Create a folder at the following location:

    Mac:    `/Macintosh HD/Users/Shared/df2017_merging_data`
    PC :    `C:\Users\Public\df2017_merging_data`
    
2. Download the following files into that folder:

    [survey.db sqlite3 database](gihub/data/raw/survey.db)
    [Person csv file](gihub/data/raw/person.csv)
    [Site csv file](gihub/data/raw/site.csv)
    [Survey csv file](gihub/data/raw/survey.csv)
    [Visited csv file](gihub/data/raw/visited.csv)

### SQLite3

#### Mac

No need to do anything here! SQLite3 is pre-installed on Mac systems on Mac OS X 10.4 and later.

#### Windows

Although these instructions were written for Window 7 SP1, they may vary slightly for v8.1, or v10. Please adjust accordingly, or see the HelpDesk volunteers in the DataFest concourse.

1. Please create a folder called `Installers` inside your `df2017_merging_data` folder, and download the following Zip archives to that location:

    [32-bit DLL (x86) for SQLite version 3.16.2](github\installers\sqlite-dll-win32-x86-3160200.zip)
    [SQLite command-line tools, shell, sqldiff, and sqlite3_analyzer programs](github\installers\sqlite-tools-win32-x86-3160200.zip)

2. Unzip each archive by a right-mouse click on each archive, select `Extract All...`, and in the dialog that appears, navigate to the folder `Computer > C:\Windows\System32`. Uncheck the `Show Extracted Files When Complete` checkbox. Click on the Enter button.

3. To test the success of your installation, go to Windows Start menu, end `cmd` and press Enter. When a (black) shell window appears, type `sqlite3` and press Enter. You are successful if the prompt changes to `sqlite> `. Type `.quit` and Enter to exit. If you did not get this prompt, please see the HelpDesk volunteers at DataFest concourse.

    
### Analysis Environments

You do not need to install these three analysis environments. We are going to demonstrate how to use SQLite from each of them. Only install the one(s) that you are most interested in. Also note that you might be required to install these for other Datafest Hands-on sessions.

### Python + SQLite module

1. For both Mac and PC, please download to your `Installers` folder the appropriate installer from [Continuum Analytics](https://www.continuum.io/) Anaconda Python v2.7 installer and run it to start the installation process. If you don't know which PC installer to use, please use the 32-bit one.

    Mac 64-bit: https://repo.continuum.io/archive/Anaconda2-4.2.0-MacOSX-x86_64.pkg
    PC 32-bit : https://repo.continuum.io/archive/Anaconda2-4.2.0-Windows-x86.exe
    PC 64-bit : https://repo.continuum.io/archive/Anaconda2-4.2.0-Windows-x86_64.exe
    
2. To test the success of your installation, open up a Terminal or cmd shell window, type in `python` and press Enter. You are successful if the prompt changes to `>>> ` and 'Continuum Analytics' is mentioned in the text above. Type `quit()` and Enter to exit. If you did not get this prompt, please see the HelpDesk volunteers at DataFest concourse.
    
### R + RStudio + RSQLite + dplyr packages

1. For both Mac and PC, please download to your `Installers` folder the R installer from the [CRAN](https://cran.r-project.org/) site and run it to start the installation process:

    Mac: https://cran.r-project.org/bin/macosx/R-3.3.2.pkg        
    PC : https://cran.r-project.org/bin/windows/base/R-3.3.2-win.exe

2. For both Mac and PC, please download to your `Installers` folder the RStudio installer from the [RStudio](https://www.rstudio.com/) site and run it to start the installation process:

    Mac: https://download1.rstudio.org/RStudio-1.0.136.dmg     
    PC : https://download1.rstudio.org/RStudio-1.0.136.exe


3. Final step is to install the R packages needed for the workshop. Open up the RStudio program. In the console window that appears in the left pane, please enter the following commands one-at-a-time, noting that there may be long pauses as RStudio processes and installs all the dependent packages:

    install.packages('RSQLite')
    install.packages('dplyr')

Red text may appear and scroll by. For the most part, that should be fine. But the final message should be something like...

The downloaded binary packages are in
	C:\Users\myuser\AppData\Local\Temp\RtmpusjIjg\downloaded_packages


4. To test the success of your installation, enter the following commands:

    library('RSQLite')
    library('dplyr')
    
For RSQLite, there should be nothing printed. For dplyr, you may get someting like the following:

`Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union`

If you receive any error (not warning) messages, please see the HelpDesk volunteers at DataFest concourse.


### Stata + ODBC drivers

This is perhaps the most complex of the three analysis environments, as the ODBC (Open DataBase Connectivity) installation can be complex and/or difficult. We have provided preset configuration files & images that will only work if you've followed the instructions above. 

#### Stata

You must have a licensed copy of [Stata](http://www.stata.com) pre-installed. We will not provide it for your for this workshop.

#### ODBC Manager

The ODBC Manager software acts as a broker between your front-end program (R, Python, Stata) and the backend database, allowing you to slot in any database. 

1a. For the PC, this step is not needed as it is built into the Windows operating system.

1b. For both Mac, please download to your `Installers` folder the [iODBC Manager 3.52.12 disk image](http://opldownload.s3.amazonaws.com/uda/components/7.0/universal-apple-macosx10.7-32/mxkozzzz.dmg). Open the disk image file, and double-click the installer package to start the installation process.


#### ODBC Drivers

For each backend database or data source, you need software (a driver) to communicate between it and the ODBC Manager. We will use open source drivers from [http://www.ch-werner.de/sqliteodbc/](http://www.ch-werner.de/sqliteodbc/), which work well-enough for our purposes. Know that these can cost anywhere from $20 to $200!

1. For both Mac and PC, please download to your `Installers` folder the appropriate installer and run it to start the installation process. PC users: please download and install BOTH sets of drivers.

    Mac: [v0.9994 with full-text search support](http://www.ch-werner.de/sqliteodbc/sqliteodbc-0.9994.dmg)
    PC : [v0.9995 Win32](http://www.ch-werner.de/sqliteodbc/sqliteodbc.exe)
    PC : [v0.9995 Win64](http://www.ch-werner.de/sqliteodbc/sqliteodbc_w64.exe)

#### ODBC Configuration

**PC**

Unfortunately, this must be done by hand via the Windows GUI interface. Although these instructions were written for Window 7 SP1, they may vary slightly for v8.1, or v10. Please adjust accordingly. If really stuck, see the HelpDesk volunteers in the DataFest concourse.

1. From your Start / Search menu, look for 'ODBC', and run a program similar to "Data Sources (ODBC)" or the Control Panel "Set up data sources (ODBC)"

2. Click on the Drivers tab. You should see "SQLite3 ODBC Driver" listed here, among others:

[image = odbc_data_source_admin_drivers.png]

 If you do not, please retry the ODBC Manager and ODBC Driver PC installation steps. If you still do not see it here, please see the HelpDesk volunteers at DataFest concourse.

3. Click on the User DNS tab. Click on the Add button. Select the SQLite3 ODBC Driver". 

[image = odbc_create_new_data_source.png]

PLEASE verify that you select SQLite3, not the other choices. Click on the Finish button.

4. In the new window that appears, enter "DF_Survey_DB" as the Data Source Name. For Database Name, enter "C:\Users\Public\datafest_2017\survey.db" or use the Browse button to navigate to the `survey.db` file in your `datafest_2017` folder. 

[image=odbc_sqlite3_odbc_dsn_config.png]

You should have this window configured as such. Click on OK to close this window, and OK again to close the ODBC Manager.


**Mac**

1. In your Applications folder, open the iODBC folder. 

SQLite3_Driver
/usr/local/lib/libsqlite3odbc.dylib

DF_Survey_DB
/Users/Shared/datafest_2017/survey.db

2. 

