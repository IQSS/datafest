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

```sql
SELECT * FROM Visited WHERE site = 'DR-1' AND dated < '1930-01-01';
```

```sql
SELECT * FROM Visited WHERE site LIKE 'DR%';
```

#### Calculatint new values
```sql
SELECT 1.05 * reading FROM Survey WHERE quant='rad';
```

```sql
SELECT personal || ' ' || family FROM Person;
```
#### Aggregating data
```sql
SELECT person, count(reading), round(avg(reading), 2)
FROM  Survey
WHERE quant='rad'
AND   person='dyer';
```

```sql
SELECT   person, count(reading), round(avg(reading), 2)
FROM     Survey
WHERE    quant='rad'
GROUP BY person;
`
### Show how to import data, assuring unique IDs


### Show approach at doing joins with SQL

Matching