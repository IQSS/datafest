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

A database is a construct for data storage; it can be specifically designed for a certain data type, or it can be more generic. We don't see these as often, but library indices and telephone directories are some examples of databases we can hold. Computer-based databases are more of the norm now, and are also what we will be discussing today.

Three common options for data storage are text files, spreadsheets, and databases. Text files are easiest to create, and work well with version control, but then we would have to build search and analysis tools ourselves. Spreadsheets are good for doing simple analyses, but they don’t handle large or complex data sets well. Databases, however, include powerful tools for search and analysis, and can handle large, complex data sets. These lessons will show how to use a database to explore the expeditions’ data.

The three major ways to model databases are [*relational*](https://en.wikipedia.org/wiki/Relational_model), [*heirarchical*](https://en.wikipedia.org/wiki/Hierarchical_database_model) and [*network*](https://en.wikipedia.org/wiki/Network_model). The Relational model is the one that is most commonly employed and the resulting database is appropriately called a **Relational Database**.

Within a [relational database]({{ site.github.url }}/reference/#relational-database) the data is arranged into [tables]({{ site.github.url }}/reference/#table). Each table has columns (also known as [fields]({{ site.github.url }}/reference/#field)) that describe the data, and rows (also known as [records]({{ site.github.url }}/reference/#record)) which contain the data.

When we are using a spreadsheet, we put formulas into cells to calculate new values based on old ones. When we are using a database,
we send commands (usually called [queries]({{ site.github.url }}/reference/#query)) to a [database manager]({{ site.github.url }}/reference/#database-manager): a program that manipulates the database for us. The database manager does whatever lookups and calculations the query specifies, returning the results in a tabular form that we can then use as a starting point for further queries.

#### Why would we want to do this?

* It keeps data separate from your analysis
* This means there’s no risk of accidentally changing data when you analyze it
* If we get new data we can just rerun the query 
* It’s fast, even for large amounts of data
* It improves quality control of data entry (type constraints and use of forms in Access, Filemaker, etc.) 
* A lot of these database managers can be used to access stored data easily with programming languages like R or Python

#### What are some of the struggles of doing so?

If coming from spreadsheets or flatfiles (e.g. csv, Excel spreadsheets), there are a number of struggles that one will go through. Specifically:

* programmatic interrogation of data goes through a text language (SQL) and not through an visual interface. But both can be used!
* Spreadsheets are typically used for data collection & entry, formatting, analysis, and presentation. This mixed mode of use can cause problems at various points along the data lifecycle. In general, it is better to separate the various stages so that changes in one stage do not adversely affect the other
* often we use a spreadsheet to convey additional information, metadata, on the data itself. For example, notes about data collection, units, validity of measurements, etc. These should be explicitly coded in your data, or kept as a separate metadata table for your work.

#### Moving towards structured Data

Key points when moving towards structured data that you wish to move into a database system:

Exercise:

Let's look at a few rows of the data that we're collecting:

Turn to your neighbor, and talk about how you can break up this data into groups, and how would you represent the data within those groups?
