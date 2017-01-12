#!/bin/sh

# This script will create the necessary local ODBC directory in the home folder
#   and download via curl the odbc.ini and odbcinst.ini files from the GitHub repo.
# 
# It'll be like magic!
#
# RMF, 1/12/17

target=~/ODBC
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
curl "https://raw.githubusercontent.com/IQSS/datafest/master/multiple_approaches_combining_data/installers/mac/odbcinst.ini" \
  > $target/$driverfile

# if odbc.ini exists, rename it to odbc.ini.bak for safe keeping

if [ -f $target/$dsnfile ]
then
    mv $target/$dsnfile $target/$dsnfile.bak
    echo 
    echo "A $dsnfile was found at $target. It was renamed to $dsnfile.bak for safe keeping!"
    echo
fi

# bring in class file
curl "https://raw.githubusercontent.com/IQSS/datafest/master/multiple_approaches_combining_data/installers/mac/odbc.ini" \
  > $target/$dsnfile

echo
echo "Done! You may now close this window."