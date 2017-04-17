---
layout: default
title: "Introduction to Versioning"
author: "Daniel van Strien, Radhika Khetani, Bob Freeman, Amir Karger"
output: html_document
---

#  Versioning your Data and Scripts

## Setting up for today's class

For this quick hands-on session we will be using a Graphical User Interface (GUI) to work with Git. **Let's start by downloading and installing [GitKraken](https://www.gitkraken.com/download)**.

## What is Version Control?

Version control can be used to keep track of versions of a piece of work that either a single person is working on, or a shared document. It is designed to avoid a situation like noted below.

```
mydocument.txt
mydocument_v2.txt
mydocument_v3_rev-BHP.txt
mydocument_v8_Final?.txt
```
Some word processors let us deal with this a little better, without creating a new file for every "save", such as Microsoft Word's "Track Changes" or Google Docs' [version history](https://support.google.com/docs/answer/190843?hl=en).

Version control systems start with a base version of the document and then save just the changes you made at each step of the way by taking a so-called "snapshot". A snapshot records information about when it was taken, and all the changes between the current document and the previous version. The user (you) decides when these snapshots are collected, and this allows one to ‘rewind’ your file to an older version. 

<img src="img/play-changes.png" width="600" align="center">

For example, two users can make independent sets of changes based on the same document and have 2 separate snapshots documenting the changes.

<img src="img/versions.png" width="400" align="center">

If there aren't conflicts, you can "merge" two sets of changes onto the same base document.

<img src="img/merged_example.png" width="400" align="center">

## Why use Version Control?

The 2 main reasons to use version control are to:

* Manage text/data/code effectively 
* Collaborate efficiently

Version control is particularly useful for facilitating collaboration. One of the original motivations behind version control systems was to allow different people to work on large projects together, and in the case of Git, to manage the Linux kernel source code. 

Though version control was originally designed for dealing with code there are many benefits to using it to with ***text files*** too (`.txt`, `.csv`, `.tsv`). Some examples of projects making use of version control systems like GitHub include: writing manuscripts, books or dissertations, and for collaboratively developing as well as distributing teaching materials (like for this class).

> Note: Different Version Control systems handle different *non-text files* differently. 
> In most cases Word documents, graphics files, data objects from R or STATA, etc., can be included but most tools have limited capabilities for these.

Benefits of collaborating with Version Control include:

* Flexibility and control
* Multiple people can simultaneously work on a document
* Easy conflict resolution 
* Easy to revert to an older version

## Why Not use Dropbox or Google Drive?

Dropbox, Google Drive and other services offer some form of version control in their systems. There are times when this may be sufficient for your needs. However there are a number of advantages to using a version control system like Git:

* **Language support**: Git supports both text and programming languages. As research moves to include more digital techniques and tools it becomes increasingly important to have a way of managing and sharing both the ‘traditional’ outputs (journal articles, books, etc.) but also these newer outputs (code, datasets etc.)
* **More control**: a proper version control systems gives you a much greater deal of control over how you manage changes in a document, including the ability to comment on every change making it easier to revert. This is especially true when sets of changes across documents need to be coordinated as one unit.
* **Useful history**: using version control systems like Git will allow you to produce a history of your document in which different stages of the documents can be navigated easily both by yourself and by others.

## What are Git and GitHub?

Though often used synonymously, Git and GitHub are two different things:

* Git is a particular implementation of version control. However, it is used to refer both to a particular approach taken to version control and the software underlying it.

* GitHub is a company which hosts Git repositories (more on this below) and provides software for using Git, e.g. ‘GitHub Desktop’. GitHub is currently the most popular host of open source projects by [number of projects and number of users](https://en.wikipedia.org/wiki/Comparison_of_source_code_hosting_facilities#Popularity). But other hosts exist, including [SourceForge](https://sourceforge.net/), [BitBucket](https://bitbucket.org/), and [Gitlab](https://about.gitlab.com/), to name a few.



Becoming familiar with GitHub will be useful not only for version controlling your own documents but will also make it easier to contribute and draw upon other projects which use GitHub. 

In this lesson the focus will be on gaining an understanding of the basic aims and principles of Version Control by uploading and version controlling a plain text document using Github. This lesson will not cover everything but will provide a starting point to using Version Control (Git/Github or [other](https://en.wikipedia.org/wiki/Comparison_of_version_control_software)).

***

* Materials used in these lessons are derived from Daniel van Strien's ["An Introduction to Version Control Using GitHub Desktop,"](http://programminghistorian.org/lessons/getting-started-with-github-desktop), Programming Historian, (17 June 2016). [The Programming Historian ISSN 2397-2068](http://programminghistorian.org/), is released under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*

* Materials are also derived from [Software Carpentry instructional material](https://swcarpentry.github.io/git-novice/). These materials are also licensed under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*
