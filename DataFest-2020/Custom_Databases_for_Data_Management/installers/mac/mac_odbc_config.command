#!/bin/sh

# This script will create the necessary local ODBC directory in the home folder
#   and download via curl the odbc.ini and odbcinst.ini files from the GitHub repo.
# 
# It'll be like magic!
#
# RMF, 1/12/17

echo "This bash (terminal) script will make the necessary ODBC folder in your invisible"
echo "home Library folder and download the odbc configuration files for this workshop."
echo "If any config files are already present, these will be renamed with the suffix *.bak."
echo
echo

target=$HOME/Library/ODBC
driverfile=odbcinst.ini
dsnfile=odbc.ini

mkdir -p $target

# if odbcinst.ini exists, rename it to odbcinst.ini.bak for safe keeping
#   and notify user
if [ -f $target/$driverfile ]
then
    mv $target/$driverfile $target/$driverfile.bak
    echo 
    echo "A $driverfile was found at $target. It was renamed to $driverfile.bak for safe keeping!"
    echo
fi

# bring in class file
echo "Downloading $driverfile..."
curl -o $target/$driverfile "https://raw.githubusercontent.com/hbs-rcs/datafest/master/DataFest-2020/Custom_Databases_for_Data_Management/installers/mac/odbcinst.ini"

# if odbc.ini exists, rename it to odbc.ini.bak for safe keeping

if [ -f $target/$dsnfile ]
then
    mv $target/$dsnfile $target/$dsnfile.bak
    echo 
    echo "A $dsnfile was found at $target. It was renamed to $dsnfile.bak for safe keeping!"
    echo
fi

# bring in class file
echo "Downloading $dsnfile..."
curl -o $target/$dsnfile "https://raw.githubusercontent.com/hbs-rcs/datafest/master/DataFest-2020/Custom_Databases_for_Data_Management/installers/mac/odbc.ini"

if [ -f ~/Library/ODBC/odbc.ini ] && [ -f ~/Library/ODBC/odbcinst.ini ]
then 
  echo
  echo "Files are present and installed OK. You may now close this window."
  echo 
else
  echo
  echo "Files were not installed OK. Please download $driverfile and $dsnfile from the Github"
  echo "site at 'installers > mac' and manually place inside the folder $target."
  echo "If any major problems, show this window to the HelpDesk volunteers at the DataFest concourse."
  echo
fi
