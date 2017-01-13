---
layout: default
title: "Multiple Approaches to Combining Data"
author: "Radhika Khetani, Bob Freeman"
output: html_document
---

#Multiple Approaches to Combining Data


## Section 1: Intro/Review (10 min)

### Review of structured data and advantage of database systems

#### Why would we want to do this?

#### What are some of the struggles of doing so?

Assume prior (very basic!) knowledge of SQL; perhaps 1 to 2 slides on basic functionality



## Section 2: Basic SQLite (30 min incl. exercises)

### Show how to import data, assuring unique IDs

### Show approach at doing joins with SQL

## Section 3: ODBC & Using DBs within R, Python, & Stata (30 min inc. exercises)
??Briefly discuss ODBC & how to configure
??Direct access from R/Python using local shared libraries/language bindings

### Moving to R (dplyr), Python, and Stata for accessing local/remote DB

#### Show connect, select, & print example using pseudocode

#### Show specific example in R, Python, & Stata

---
title: "Programming with Databases - Python"
teaching: 20
exercises: 15
questions:
- "How can I access databases from programs written in Python?"
objectives:
- "Write short programs that execute SQL queries."
- "Trace the execution of a program that contains an SQL query."
- "Explain why most database applications are written in a general-purpose language rather than in SQL."
keypoints:
- "General-purpose languages have libraries for accessing databases."
- "To connect to a database, a program must use a library specific to that database manager."
- "These libraries use a connection-and-cursor model."
- "Programs can read query results in batches or all at once."
- "Queries should be written using parameter substitution, not string formatting."
---
To close,
let's have a look at how to access a database from
a general-purpose programming language like Python.
Other languages use almost exactly the same model:
library and function names may differ,
but the concepts are the same.

Here's a short Python program that selects latitudes and longitudes
from an SQLite database stored in a file called `survey.db`:

~~~
import sqlite3
connection = sqlite3.connect("survey.db")
cursor = connection.cursor()
cursor.execute("SELECT Site.lat, Site.long FROM Site;")
results = cursor.fetchall()
for r in results:
    print r
cursor.close()
connection.close()
~~~
{: .python}
~~~
(-49.85, -128.57)
(-47.15, -126.72)
(-48.87, -123.4)
~~~
{: .output}

The program starts by importing the `sqlite3` library.
If we were connecting to MySQL, DB2, or some other database,
we would import a different library,
but all of them provide the same functions,
so that the rest of our program does not have to change
(at least, not much)
if we switch from one database to another.

Line 2 establishes a connection to the database.
Since we're using SQLite,
all we need to specify is the name of the database file.
Other systems may require us to provide a username and password as well.
Line 3 then uses this connection to create a [cursor]({{ site.github.url }}/reference/#cursor).
Just like the cursor in an editor,
its role is to keep track of where we are in the database.

On line 4, we use that cursor to ask the database to execute a query for us.
The query is written in SQL,
and passed to `cursor.execute` as a string.
It's our job to make sure that SQL is properly formatted;
if it isn't,
or if something goes wrong when it is being executed,
the database will report an error.

The database returns the results of the query to us
in response to the `cursor.fetchall` call on line 5.
This result is a list with one entry for each record in the result set;
if we loop over that list (line 6) and print those list entries (line 7),
we can see that each one is a tuple
with one element for each field we asked for.

Finally, lines 8 and 9 close our cursor and our connection,
since the database can only keep a limited number of these open at one time.
Since establishing a connection takes time,
though,
we shouldn't open a connection,
do one operation,
then close the connection,
only to reopen it a few microseconds later to do another operation.
Instead,
it's normal to create one connection that stays open for the lifetime of the program.


### Exercises:

We've shown how to execute the SQL code for a one table query in pseudocode. Modify your code and query for a two table join? 

??Show approach at doing join inside R, Python, Stata

