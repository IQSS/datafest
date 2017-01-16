---
layout: default
title: "Multiple Approaches to Combining Data"
author: "Radhika Khetani, Bob Freeman"
output:
  html_document: 
    toc: true
---

# Multiple Approaches to Combining Data

Welcome
Goals of the Hands-on
Assumptions
Agenda
For further reading...

## Section 1: Intro/Review (10 min)

---
title: "Intro to Structured Data/Review"
teaching: 10
exercises: 5
questions:
- "How can I get data from a database?"
objectives:
- "Explain the difference between a table, a record, and a field."
- "Explain the difference between a database and a database manager."
keypoints:
- "A relational database stores information in tables, each of which has a fixed set of columns and a variable number of records."
- "A database manager is a program that manipulates information stored in a database."
---

### Review of structured data and advantage of database systems

Three common options for storage are text files, spreadsheets, and databases. Text files are easiest to create, and work well with version control, but then we would have to build search and analysis tools ourselves. Spreadsheets are good for doing simple analyses, but they don’t handle large or complex data sets well. Databases, however, include powerful tools for search and analysis, and can handle large, complex data sets. These lessons will show how to use a database to explore the expeditions’ data.

A [relational database]({{ site.github.url }}/reference/#relational-database)
is a way to store and manipulate information.
Databases are arranged as [tables]({{ site.github.url }}/reference/#table).
Each table has columns (also known as [fields]({{ site.github.url }}/reference/#field)) that describe the data,
and rows (also known as [records]({{ site.github.url }}/reference/#record)) which contain the data.

 
When we are using a spreadsheet,
we put formulas into cells to calculate new values based on old ones.
When we are using a database,
we send commands
(usually called [queries]({{ site.github.url }}/reference/#query))
to a [database manager]({{ site.github.url }}/reference/#database-manager):
a program that manipulates the database for us.
The database manager does whatever lookups and calculations the query specifies,
returning the results in a tabular form
that we can then use as a starting point for further queries.



#### Why would we want to do this?


 * It keeps your data separate from your analysis. * This means there’s no risk of accidentally changing data when you analyze it. * If we get new data we can just rerun the query. * It’s fast, even for large amounts of data. * It improves quality control of data entry (type constraints and use of forms in Access, Filemaker, etc.) * The concepts of relational database querying are core to understanding how to do similar things using programming languages such as R or Python.


#### What are some of the struggles of doing so?

If coming from spreadsheets or flatfiles (e.g. csv, Excel spreadsheets), there are a number of struggles that one will go through. Specifically:

- programmatic interrogation of data goes through a text language (SQL) and not through an visual interface. But both can be used!
- Spreadsheets are typically used for data collection & entry, formatting, analysis, and presentation. This mixed mode of use can cause problems at various points along the data lifecycle. In general, it is better to separate the various stages so that changes in one stage do not adversely affect the other

- often we use a spreadsheet to convey additional information, metadata, on the data itself. For example, notes about data collection, units, validity of measurements, etc. These should be explicitly coded in your data, or kept as a separate metadata table for your work.


#### Moving towards structured Data

Key points when moving towards structured data that you wish to move into a database system:

Exercise:

Let's look at a few rows of the data that we're collecting:

Turn to your neighbor, and talk about how you can break up this data into groups, and how would you represent the data within those groups?





## Section 2: Basic SQLite (30 min incl. exercises)

Assume prior (very basic!) knowledge of SQL; perhaps 1 to 2 slides on basic functionality

---
title: "Selecting Data"
teaching: 10
exercises: 5
questions:
- "How can I get data from a database?"
- "What are various options I can use to manipulate my data (e.g. sort, remove dupes, aggregate)?
- "How can I select subsets of data?"
- "How can I calculate new values on the fly?"
- "How can I combine data from multiple tables?"

objectives:
- "Explain the difference between a table, a record, and a field."
- "Explain the difference between a database and a database manager."

keypoints:
- "A relational database stores information in tables, each of which has a fixed set of columns and a variable number of records."
- "A database manager is a program that manipulates information stored in a database."
---
### Brief (!) review of SQL

Our data: In the late 1920s and early 1930s, William Dyer, Frank Pabodie, and Valentina Roerich led expeditions to the Pole of Inaccessibility in the South Pacific, and then onward to Antarctica. Two years ago, their expeditions were found in a storage locker at Miskatonic University. We have scanned and OCR the data they contain, and we now want to store that information in a way that will make search and analysis easy.

Before we get into the data and using SQLite to select the data,

The tables below show the database we will use in our examples:

<div class="row">
  <div class="col-md-6" markdown="1">

**Person**: people who took readings.

|id      |personal |family
|--------|---------|----------
|dyer    |William  |Dyer
|pb      |Frank    |Pabodie
|lake    |Anderson |Lake
|roe     |Valentina|Roerich
|danforth|Frank    |Danforth

**Site**: locations where readings were taken.

|name |lat   |long   |
|-----|------|-------|
|DR-1 |-49.85|-128.57|
|DR-3 |-47.15|-126.72|
|MSK-4|-48.87|-123.4 |

**Visited**: when readings were taken at specific sites.

|id   |site |dated     |
|-----|-----|----------|
|619  |DR-1 |1927-02-08|
|622  |DR-1 |1927-02-10|
|734  |DR-3 |1930-01-07|
|735  |DR-3 |1930-01-12|
|751  |DR-3 |1930-02-26|
|752  |DR-3 |-null-    |
|837  |MSK-4|1932-01-14|
|844  |DR-1 |1932-03-22|

  </div>
  <div class="col-md-6" markdown="1">

**Survey**: the actual readings.

|taken|person|quant|reading|
|-----|------|-----|-------|
|619  |dyer  |rad  |9.82   |
|619  |dyer  |sal  |0.13   |
|622  |dyer  |rad  |7.8    |
|622  |dyer  |sal  |0.09   |
|734  |pb    |rad  |8.41   |
|734  |lake  |sal  |0.05   |
|734  |pb    |temp |-21.5  |
|735  |pb    |rad  |7.22   |
|735  |-null-|sal  |0.06   |
|735  |-null-|temp |-26.0  |
|751  |pb    |rad  |4.35   |
|751  |pb    |temp |-18.5  |
|751  |lake  |sal  |0.1    |
|752  |lake  |rad  |2.19   |
|752  |lake  |sal  |0.09   |
|752  |lake  |temp |-16.0  |
|752  |roe   |sal  |41.6   |
|837  |lake  |rad  |1.46   |
|837  |lake  |sal  |0.21   |
|837  |roe   |sal  |22.5   |
|844  |roe   |rad  |11.25  |

  </div>
</div>

Notice that three entries --- one in the `Visited` table,
and two in the `Survey` table --- don't contain any actual
data, but instead have a special `-null-` entry:
we'll return to these missing values [later]({{ site.github.url }}/05-null/).

Let's begin by opening up our SQLite database and interrogating our data!

> ## Getting Into and Out Of SQLite
>
> In order to use the SQLite commands *interactively*, we need to
> enter into the SQLite console. 


Open a shell or Terminal window and move to the location where our data is:

Mac: Command-space to open up Spotlight search, type `Terminal`, and when the Terminal application appears, press Enter. Then enter the command `cd /Users/Shared/datafest_2017/`.
PC: Go to your Windows/Start menu search, type `cmd`, and when the Windows Shell option appears, press Enter. Then enter the command `cd C:\Users\Public\datafest_2017\`.

This folder should have your csv and sqlite3 database files in there. Now enter `sqlite3 survey.db`

> The SQLite command is `sqlite3` and you are telling SQLite to open up
> the `survey.db`.  You need to specify the `.db` file otherwise, SQLite
> will open up a temporary, empty database.
>
> To get out of SQLite, type out `.exit` or `.quit`.  For some
> terminals, `Ctrl-D` can also work.  If you forget any SQLite `.` (dot)
> command, type `.help`.
{: .callout}

Let's turn on two options in our console to make working with SQL and SQLite more user-friendly:
```sql
.mode column
.header on
```

> All SQLite-specific commands are prefixed with a `.` to distinguish them from SQL commands.
> Type `.tables` to list the tables in the database.
>
> ```sql
> .tables
> 
> Person   Site     Survey   Visited
> ```
>
> For a full list of commands, type `.help` and see the [SQLIte CLI page](https://sqlite.org/cli.html)

#### Selecting data

For now,
let's write an SQL query that displays scientists' names.
We do this using the SQL command `SELECT`,
giving it the names of the columns we want and the table we want them from.
Our query and its output look like this:

```sql
SELECT family, personal FROM Person;
```

|family  |personal |
|--------|---------|
|Dyer    |William  |
|Pabodie |Frank    |
|Lake    |Anderson |
|Roerich |Valentina|
|Danforth|Frank    |

Case does not matter, the columns names are separated by commands, and a semicolon is used to terminal the statement. If you forget the semicolon, SQL will prompt you with additional `>` on a new line. 

To select all columns use `*`:
```sql
SELECT * FROM Person;
```

|id      |personal |family  |
|--------|---------|--------|
|dyer    |William  |Dyer    |
|pb      |Frank    |Pabodie |
|lake    |Anderson |Lake    |
|roe     |Valentina|Roerich |
|danforth|Frank    |Danforth|

Our next task is to identify the scientists on the expedition by looking at the `Person` table.
As we mentioned earlier,
database records are not stored in any particular order.
This means that query results aren't necessarily sorted,
and even if they are,
we often want to sort them in a different way,
e.g., by their identifier instead of by their personal name.
We can do this in SQL by adding an `ORDER BY` clause to our query:

```sql
SELECT * FROM Person ORDER BY id;
```

|id     |personal |family  |
|-------|---------|--------|
|danfort|Frank    |Danforth|
|dyer   |William  |Dyer    |
|lake   |Anderson |Lake    |
|pb     |Frank    |Pabodie |
|roe    |Valentina|Roerich |

By default,
results are sorted in ascending order
(i.e.,
from least to greatest).
We can sort in the opposite order using `DESC` (for "descending"):

~~~
SELECT * FROM person ORDER BY id DESC;
~~~
{: .sql}

|id     |personal |family  |
|-------|---------|--------|
|roe    |Valentina|Roerich |
|pb     |Frank    |Pabodie |
|lake   |Anderson |Lake    |
|dyer   |William  |Dyer    |
|danfort|Frank    |Danforth|

(And if we want to make it clear that we're sorting in ascending order,
we can use `ASC` instead of `DESC`.)



The `Person` table is not too interesting. So let's switch to our quantitative data:

To determine which measurements were taken at each site,
we can examine the `Survey` table.
Data is often redundant,
so queries often return redundant information.
For example,
if we select the quantities that have been measured
from the `Survey` table,
we get this:

~~~
SELECT quant FROM Survey;
~~~
{: .sql}

|quant|
|-----|
|rad  |
|sal  |
|rad  |
|sal  |
|rad  |
|sal  |
|temp |
|rad  |
|sal  |
|temp |
|rad  |
|temp |
|sal  |
|rad  |
|sal  |
|temp |
|sal  |
|rad  |
|sal  |
|sal  |
|rad  |

We can eliminate the redundant output to
make the result more readable by adding the `DISTINCT` keyword to our
query:

~~~
SELECT DISTINCT quant FROM Survey;
~~~
{: .sql}

|quant|
|-----|
|rad  |
|sal  |
|temp |

We can use the `DISTINCT` keyword on multiple columns.
If we select more than one column,
the distinct *pairs* of values are returned:

~~~
SELECT DISTINCT taken, quant FROM Survey;
~~~
{: .sql}

|taken|quant|
|-----|-----|
|619  |rad  |
|619  |sal  |
|622  |rad  |
|622  |sal  |
|734  |rad  |
|734  |sal  |
|734  |temp |
|735  |rad  |
|735  |sal  |
|735  |temp |
|751  |rad  |
|751  |temp |
|751  |sal  |
|752  |rad  |
|752  |sal  |
|752  |temp |
|837  |rad  |
|837  |sal  |
|844  |rad  |

In order to look at which scientist measured quantities at each site,
we can look again at the `Survey` table, sorting results first in ascending order by `taken`,
and then in descending order by `person`
within each group of equal `taken` values:

```sql
SELECT taken, person, quant FROM Survey ORDER BY taken ASC, person DESC;
```

|taken|person|quant|
|-----|------|-----|
|619  |dyer  |rad  |
|619  |dyer  |sal  |
|622  |dyer  |rad  |
|622  |dyer  |sal  |
|734  |pb    |rad  |
|734  |pb    |temp |
|734  |lake  |sal  |
|735  |pb    |rad  |
|735  |-null-|sal  |
|735  |-null-|temp |
|751  |pb    |rad  |
|751  |pb    |temp |
|751  |lake  |sal  |
|752  |roe   |sal  |
|752  |lake  |rad  |
|752  |lake  |sal  |
|752  |lake  |temp |
|837  |roe   |sal  |
|837  |lake  |rad  |
|837  |lake  |sal  |
|844  |roe   |rad  |

This query gives us a good idea of which scientist was at which site,
and what measurements they performed while they were there. We can examine which scientists
performed which measurements by selecting the appropriate columns and
removing duplicates:

```sql
SELECT DISTINCT quant, person FROM Survey ORDER BY quant ASC;
```

|quant|person|
|-----|------|
|rad  |dyer  |
|rad  |pb    |
|rad  |lake  |
|rad  |roe   |
|sal  |dyer  |
|sal  |lake  |
|sal  |-null-|
|sal  |roe   |
|temp |pb    |
|temp |-null-|
|temp |lake  |


We can get unique data 
#### Filtering data

#### Aggregating data

### Show how to import data, assuring unique IDs


### Show approach at doing joins with SQL

Matching



## Section 3: Using the Database within R, Python, & Stata

---
| title: | teaching:  | exercises: |
| -- | --- | --- |
| 20 minutes |  10 minutes |
---

> Questions:
> - "How can I access databases from scripts and programs written in Python, R, Stata, or other languages?"
> objectives:
> - "Write short programs that execute SQL queries."
> - "Trace the execution of a program that contains an SQL query."
> Keypoints:
> - "General-purpose languages have libraries for accessing databases."
> - "To connect to a database, a program must use a library specific to that database manager."
> - "These libraries use a connection-and-cursor model."
> What we won't cover:
> - "Programs can read query results in batches or all at once."
> - "Queries should be written using parameter substitution, not string formatting."


### Moving to R (dplyr), Python, and Stata for accessing local/remote DB

One real value in using databases is that this data is accessible from multiple analysis and visualization environments, like R, Python, Stata, and Tableau. The real win is that these environments request the data, and all the heavy computation is done on the back end. This allow greater amount of flexibility in scripting, the data is managed uniformly, and the processing is offloaded to the database backend (SQLite). Let's look at one example:

??Briefly discuss ODBC & how to configure
??Direct access from R/Python using local shared libraries/language bindings

![ODBC Concepts](https://github.com/IQSS/datafest/blob/master/multiple_approaches_combining_data/images/udapcategoryodbc.png "Conceptual Overview of ODBC")
*Image from [OpenLink Software](https://uda.openlinksw.com/odbc/)*

TODO: general outline or figure on how languages access databases. This should show direct access via connectors; and also via ODBC Manager and Drivers

#### Accessing our data: A pseudocode example

All scripts and programs (we'll use the word 'script' to mean both of these) written in whatever language you choose will follow a standard pattern of steps. We'll write this pattern in pseudocode -- steps that outline code but are not specific to a particular language. These steaps are as follows:

```
01: load necessary libraries for database
02: create and open the database connection
03: initialize the pointer (cursor) into the database system
04: execute the SQL query
05: fetch the query results
06: iterate over the data and print the results
07: close the database connection
```

Let's go through these in more detail...

```
01: load necessary libraries for database
```
The script starts by importing the library, package, or extension needed to access the database. Often, to make the scripting language flexible, these are add-ons that 'extend' the functionality of the language. Sometimes these are built-in (as in Python) or sometimes these must be downloaded separately (as in R).
If we were connecting to MySQL, DB2, or some other database,
we would import a different library,
but all of them provide the same functions,
so that the rest of our program does not have to change
(at least, not much)
if we switch from one database to another.

```
02: create and open the database connection
```
Line 2 establishes a connection to the database.
The way we open the connection will differ among database systems, but they usually follow a similar format. This is typically database server hostname, communication port, username, password, etc. Since we're using SQLite, which is local to our computer,
all we need to specify is the name of the database file.

```
03: initialize the pointer (cursor) into the database system
```
This step then uses the open connection to create a [cursor]({{ site.github.url }}/reference/#cursor).
Just like the cursor in an editor,
its role is to keep track of where we are in the database.

```
04: execute the SQL query
```
Next, with this cursor (pointer) we ask the database to execute a query for us. The query is written in SQL , and passed as a string. It's our job to make sure that SQL is properly formatted; if it isn't, or if something goes wrong when it is being executed, the database will report an error.

The one exception to that is with the package dplyr in R, which turns R-like expressions into the required SQL behind-the-scenes, and executes that SQL on our behalf. We'll see an example of this shortly.

```
05: fetch the query results
```
The database returns the results of the query to us in response to a fetch call, which we capture in a temporary variable.

```
06: iterate over the fetched data and do something with the results
```
The format of this data will vary from language to language, and even within languages, may be represented by different data structures depending on what module/package/extension you use to interrogate the database. You'll need to read the documentation or look at example code to get exact details. Most commonly, in the result set one record (line) in the variable represents one record in the database. 

We can loop over each of the lines/records and process each one. This might be printing each, further breaking down each line into their individual fields (columns), or whatever your needs require. 

```
07: close the database connection
```
Finally, when we're done, we need to tidy up. This almost always means closing the connection to the database. Depending on the analysis environment, you might need to do additional work. For example, in Python, you also need to close the cursor before closing the database connection.

Why do this? Well, since the database can only keep a limited number of these open at one time.
Since establishing a connection takes time, though, we shouldn't open a connection, do one operation, then close the connection, only to reopen it a few microseconds later to do another operation. Instead, it's normal to create one connection that stays open for the lifetime of the program.

**One final note:** We did not talk about error checking. This should be done after each step, as you never know what might go wrong. For simplicity sake, we left these steps out. (But you won't, will you?)

#### Language-specific Examples for Using Databases

So let's see how we would implement this pseudocode in R, Python, and Stata!

**R (standard)**
```r
# import our required packages
library('RSQLite')

# open the database connection
connection <- dbConnect(SQLite(), "survey.db")

# execute and fetch the results
results <- dbGetQuery(connection, "SELECT Site.lat, Site.long FROM Site;")

# print 'em out
print(results)

# close the connection
dbDisconnect(connection)
```

**R with dplyr**
```r
# import our required packages
library('RSQLite')
library('dplyr')

# open the database connection
connection <- dbConnect(SQLite(), "survey.db")

***
# execute and fetch the results
results <- dbGetQuery(connection, "SELECT Site.lat, Site.long FROM Site;")
***

# print 'em out
print(results)

# close the connection
dbDisconnect(connection)

```

**Python**

The python code is slightly more verbose than that for R, but is still very easy to understand:

```python
# import our python3-print-in-python2 and SQLite modules
from __future__ import print_function
import sqlite3

# Open the connection, create a cursor, & use the cursor to execute the query
connection = sqlite3.connect("survey.db")
cursor = connection.cursor()
cursor.execute("SELECT Site.lat, Site.long FROM Site;")

# fetch the results as a python list, and print 'em
results = cursor.fetchall()
for r in results:
    print(r)

# clean up by closing our cursor & connection
cursor.close()
connection.close()
```

**Brief notes:** We import the modules for our database backend sqlite3 and a print function that works for both Python2 and Python3. 
If we were connecting to MySQL, DB2, or some other database,
we would import a different library. We then establish a connection, create our cursor, execute the SQL query, and fetch the results.
This result is a list with one entry for each record in the result set;
if we loop over that list and print those list entries,
we can see that each one is a tuple
with one element for each field we asked for. We finally close our cursor and our database connection.


**Stata**

```stata
???
```

### Exercises:
> 
> We've shown how to execute the SQL code for a one table query in pseudocode. Modify your code and query for a two table join? 
> 
> ??Show approach at doing join inside R, Python, Stata
> 
