---
layout: default
title: "Introduction to Versioning"
author: "Daniel van Strien, Radhika Khetani, Bob Freeman, Meeta Mistry, Kathleen Keating, Amir Karger"
---

#  Versioning your Data and Scripts

***
Previous: [README](README.md)

***

## Setting up for today's class

For this quick hands-on session we will be using a Graphical User Interface (GUI) to work with Git. Let's start by:
1. [Downloading and installing GitKraken](https://gitkraken.com/download). 
2. Creating an account for yourself on [GitHub](http://github.com). Please **select the free/academic account**, as this option has more long-term flexibility.
3. Downloading the [workshop sample files zipped folder](https://github.com/hbctraining/versioning_data_scripts/raw/master/data/example_files.zip) and unzip it.

## What is Version Control?

Version control can be used to keep track of versions of a piece of work that either a single person is working on, or a shared document. It is designed to avoid a situation like noted below.

```
mydocument.txt
mydocument_v2.txt
mydocument_v3_rev-BHP.txt
mydocument_v8_Final?.txt
```

Some tools let us deal with this a bit better without creating a new file for every "save", such as Microsoft Word's "Track Changes" or DropBox's and Google Docs' "version history" feature.

Version control systems start with a base version of the document and then save just the changes you made at each step of the way by taking a so-called "snapshot". A snapshot records information about when a doc was saved, and all the changes between the current document and the previous version. The user (you) decides when these snapshots are collected, and this allows one to ‘rewind’ your file to an older version. 

<img src="img/play-changes.png" width="600" align="center">

For example, two users can make independent sets of changes based on the same document and have 2 separate snapshots documenting the changes.

<img src="img/versions.png" width="400" align="center">

If there aren't conflicts (i.e updates to the same line), the two sets of changes can be "merged" back into the same base document.

<img src="img/merged_example.png" width="400" align="center">

### Version Control Systems and Hosts

There are a lot of [different version control systems available](https://en.wikipedia.org/wiki/List_of_version_control_software). These systems enable you to track changes locally or remotely (easy for collaborations), and there are hosts available for remote management of your "[repositories](https://en.wikipedia.org/wiki/Repository_(version_control))".

In this class we will be focusing on [Git](https://git-scm.com/). Git is usually used for version control on a local computer and you do not need internet access to use it (internet access will be needed to download Git). The local version control setup with Git (or other version control systems) can be connected to an online setup that hosts repositories for sharing and collaboration. 

GitHub is currently the most popular host of open source projects by [number of projects and number of users](https://en.wikipedia.org/wiki/Comparison_of_source_code_hosting_facilities#Popularity). But other hosts exist, including [SourceForge](https://sourceforge.net/), [BitBucket](https://bitbucket.org/), and [Gitlab](https://about.gitlab.com/), to name a few.

## Why use Version Control?

The two main reasons to use version control are to:

* Manage text/data/code effectively 
* Collaborate efficiently

Though version control was originally designed for dealing with code for large collaborative projects, there are many benefits to using it in other projects with ***text files*** too (`.txt`, `.csv`, `.tsv`). Some examples of projects making use of version control systems like Git: writing manuscripts, books or dissertations, and for collaboratively developing as well as distributing teaching materials ([e.g. the Github repository for this class](https://github.com/hbctraining/versioning_data_scripts/)).

> Note: Different Version Control systems handle different *non-text files* differently. 
> In most cases Word documents, graphics files, data objects from R or STATA, etc., can be included but most tools have limited capabilities for saving version information for these. 

**Why Not use Dropbox or Google Drive?**

Dropbox, Google Drive and other services offer some form of version control in their systems. There are times when this may be sufficient for your needs. However there are a number of advantages to using a version control system like Git, e.g. facilitating sharing/reproducibility and collaborations. Benefits of collaborating with Version Control include:

* Supports both text and programming languages, and gives the user much more control over how code is represented and disseminated
* Allows comments on every modification making it easier to revert to older version
* Allows you and others to navigate the history of a document readily
* Ensures that changes across multiple documents are coordinated and saved together (easy conflict resolution) 

***
Next: [Getting Started with Git using GitKraken](02_GitKraken.md)

***

* Materials used in these lessons are derived from Daniel van Strien's ["An Introduction to Version Control Using GitHub Desktop,"](http://programminghistorian.org/lessons/getting-started-with-github-desktop), Programming Historian, (17 June 2016). [The Programming Historian ISSN 2397-2068](http://programminghistorian.org/), is released under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*

* Materials are also derived from [Software Carpentry instructional material](https://swcarpentry.github.io/git-novice/). These materials are also licensed under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*
