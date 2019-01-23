---
layout: default
title: "Discussion of Structured Data & Database Systems"
author: "Radhika Khetani, Bob Freeman"
teaching: 10
exercises: 5
---

> questions:
> - "How can I get data from a database?"
> objectives:
> - "Explain the difference between a table, a record, and a field."
> - "Explain the difference between a database and a database manager."
> keypoints:
> - "A relational database stores information in tables, each of which has a fixed set of columns and a variable number of records."
> - "A database manager is a program that manipulates information stored in a database."


## Review of structured data and advantage of database systems

A database is a construct for data storage; it can be specifically designed for a certain data type, or it can be more generic. We don't see these as often, but library indices and telephone directories are some examples of databases we can hold. Computer-based databases are more of the norm now, and are also what we will be discussing today.

Three common options for data storage are text files, spreadsheets, and databases. Text files are easiest to create, and work well with version control, but then we would have to build search and analysis tools ourselves. Spreadsheets are good for doing simple analyses, but they don’t handle large or complex data sets well. Databases, however, include powerful tools for search and analysis, and can handle large, complex data sets.

When we are using a spreadsheet, we put formulas into cells to calculate new values based on old ones. When we are using a database, we send commands (usually called [queries]({{ site.github.url }}/reference/#query)) to a [database manager]({{ site.github.url }}/reference/#database-manager): a program that manipulates the database for us. The database manager does whatever lookups and calculations the query specifies, returning the results in a tabular form that we can then use as a starting point for further queries.

The three major ways to model databases are [*relational*](https://en.wikipedia.org/wiki/Relational_model), [*heirarchical*](https://en.wikipedia.org/wiki/Hierarchical_database_model) and [*network*](https://en.wikipedia.org/wiki/Network_model). The Relational model is the one that is most commonly employed and the resulting database is appropriately called a **Relational Database**.

Within a [relational database]({{ site.github.url }}/reference/#relational-database) the data is arranged into [tables]({{ site.github.url }}/reference/#table). Each table has columns (also known as [fields]({{ site.github.url }}/reference/#field)) that describe the data, and rows (also known as [records]({{ site.github.url }}/reference/#record)) which contain the data.

The Database engine we will be using today is **[SQLite](https://sqlite.org/about.html)**. SQLite attempts to provide a Structured Language Query (SQL) engine intended for data analysis/management "locally"; it is good at reading from, and writing directly to local files. Unlike other SQL engines like MySQL, Oracle, SQL server, etc., SQLite is not intended for high-volume websites or in the case where many "connections" need to be maintained simultaneously. [Here is a detailed overview of when it is appropriate to use SQLite](https://sqlite.org/whentouse.html). 

## Why would we want to use databases?

* It keeps data separate from your analysis
* This means there’s no risk of accidentally changing data when you analyze it
* If we get new data we can just rerun the query 
* It’s fast, even for large amounts of data
* It improves quality control of data entry (type constraints and use of forms in Access, Filemaker, etc.) 
* A lot of these database managers can be used to access stored data easily with programming languages like R or Python

## What are some of the struggles of doing so?

If coming from spreadsheets or flatfiles (e.g. csv, Excel spreadsheets), there are a number of struggles that one will go through. Specifically:

* programmatic interrogation of data goes through a text language (SQL) and not through an visual interface. But both can be used!
* Spreadsheets are typically used for data collection & entry, formatting, analysis, and presentation. This mixed mode of use can cause problems at various points along the data lifecycle. In general, it is better to separate the various stages so that changes in one stage do not adversely affect the other
* often we use a spreadsheet to convey additional information, metadata, on the data itself. For example, notes about data collection, units, validity of measurements, etc. These should be explicitly coded in your data, or kept as a separate metadata table for your work.

## Moving towards structured Data

Key points when moving towards structured data that you wish to move into a database system:

- Generate and use unique values (primary keys) for data in a given table. This primary key allows you to unique identify that row of data. This can be a unique, serial number (e.g. 1, 2, etc), a static # that is the row # upon data import, another value in a field (column), or a new field that is a combination of two values or fields that now creates a new value across all the table data.
- Follow the data normalization rules as best as possible to create modular, non-redundant data. A good, lay discussion can be found at Software Carpentry's [Data Hygiene lesson](http://swcarpentry.github.io/sql-novice-survey/08-hygiene/).

## Exercise:

> Let's look at a few rows of the data that we're collecting:
> 
> |site|dated|lat|long|personal|family|quant|reading|
> |---|---|---|---|---|---|---|---|
> |DR-1|1927-02-08|-49.85|-128.57|William|Dyer|rad|9.82|
> |DR-1|1927-02-08|-49.85|-128.57|William|Dyer|sal|0.13|
> |DR-1|1927-02-10|-49.85|-128.57|William|Dyer|rad|7.8|
> |DR-1|1927-02-10|-49.85|-128.57|William|Dyer|sal|0.09|
> |DR-1|1932-03-22|-49.85|-128.57|Valentina|Roerich|rad|11.25|
> |DR-3|1930-01-07|-47.15|-126.72|Anderson|Lake|sal|0.05|
> |DR-3|1930-01-07|-47.15|-126.72|Frank|Pabodie|rad|8.41|
> |DR-3|1930-01-07|-47.15|-126.72|Frank|Pabodie|temp|-21.5|
> |DR-3|1930-01-12|-47.15|-126.72|Frank|Pabodie|rad|7.22|
> |DR-3|1930-01-12|-47.15|-126.72|||sal|0.06|
> |DR-3|1930-01-12|-47.15|-126.72|||temp|-26.0|
> |DR-3|1930-02-26|-47.15|-126.72|Anderson|Lake|sal|0.1|
> |DR-3|1930-02-26|-47.15|-126.72|Frank|Pabodie|rad|4.35|
> |DR-3|1930-02-26|-47.15|-126.72|Frank|Pabodie|temp|-18.5|
> |DR-3||-47.15|-126.72|Anderson|Lake|rad|2.19|
> |DR-3||-47.15|-126.72|Anderson|Lake|sal|0.09|
> |DR-3||-47.15|-126.72|Anderson|Lake|temp|-16.0|
> |DR-3||-47.15|-126.72|Valentina|Roerich|sal|41.6|
> |MSK-4|1932-01-14|-48.87|-123.4|Anderson|Lake|rad|1.46|
> |MSK-4|1932-01-14|-48.87|-123.4|Anderson|Lake|sal|0.21|
> |MSK-4|1932-01-14|-48.87|-123.4|Valentina|Roerich|sal|22.5|
> 
> Turn to your neighbor, and talk about how you can break up this data into groups, and how would you represent the data within those groups?

***

[Next Lesson](02_combining_data.md)

***
*Materials used in these lessons are derived predominantly from Software Carpentry's Databases and SQL lessons, which have been released under the Creative Commons Attribution license (CC BY 4.0). Small portions were also derived from Data Carpentry's SQL for Ecology lessons, which have been released under the Creative Commons Attribution license (CC BY 4.0).*
