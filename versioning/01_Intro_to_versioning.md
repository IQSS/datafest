---
layout: default
title: "Versioning with Git/Github"
author: "Daniel van Strien, Radhika Khetani, Bob Freeman, Amir Karger"
output: html_document
---

# Version Control with Git/Github

>> NOTE: Materials used in these lessons are derived/adapted from [Daniel van Strien's "An Introduction to Version Control Using GitHub Desktop," Programming Historian, (17 June 2016)](http://programminghistorian.org/lessons/getting-started-with-github-desktop). Licensing information available at the bottom of this page.

## What is Version Control, and why use it?

It is helpful to understand what version control is and why it might be useful for the work you are doing prior to getting stuck into the practicalities. At a basic level version control involves taking ‘snapshots’ of files at different stages. Many people will have introduced some sort of version control systems for files. Often this is done by saving different versions of the files. Something like this:

```
mydocument.txt
mydocumentversion2.txt
mydocumentwithrevision.txt
mydocumentfinal.txt
```
The system used for naming files may be more or less systematic. Adding dates makes it slightly easier to follow when changes were made:

```
mydocument2016-01-06.txt
mydocument2016-01-08.txt
```

Though this system might be slightly easier to follow, there are still problems with it. Primarily this system doesn’t record or describe the changes that took place between these two saves. It is possible that some of these changes were small typo fixes but the changes could also have been a major re-write or re-structuring of a document. If you have a change of heart about some of these changes you also need to work out which date the changes were made in order to go back to a previous version.

Version control tries to address problems like these by implementing a systematic approach to recording and managing changes in files. At its simplest, version control involves taking ‘snapshots’ of your file; this snapshot records information about when the snapshot was made but also about what changes occurred between different snapshots. You decide when these snapshots are collected, and this allows you to ‘rewind’ your file to an older version. From this basic aim of version control a range of other possibilities are made available.

## Why Version Control Text Documents?

As research increasingly makes use of digital tools and storage it becomes important to consider how to best manage our research data. This becomes especially important when we want to collaborate with other people. Though version control was originally designed for dealing with code (.R, .pl. .py) there are many benefits to using it to with text documents too (.txt, .csv, .tsv). Though not all of these benefits will be covered in this lesson, version controlling your document allows you to:

* Track developments and changes in your documents
* Record the changes you made to your document in a way that you will be able to understand later
* Experiment with different versions of a document while maintaining the original version
* ‘Merge’ two versions of a document and manage conflicts between versions
* Revert changes, moving ‘backwards’ through your history to previous versions of your document

> Note: Different Version Control systems handle different non-text files differently. In most cases Word documents, graphics files, data objects from R or STATA, etc., can be included but most tools have limited capabilities for these.

Version control will not be necessary for all of the documents you write. However there are times when version control will be very useful. For substantial work such as articles, books, or dissertations, version control makes a lot of sense.

Version control is particularly useful for facilitating collaboration. One of the original motivations behind version control systems was to allow different people to work on large projects together, in the case of Git to manage the Linux kernel source code. Benefits of collaborating with Version Control include:

* flexibility and control
* multiple people can simultaneously work on a document
* easy conflict resolution 
* easy to revert to an older version

The example implementation of version control we are going to use today will be public; but, it is possible to use version control and keep your documents hidden permanently or until you decide to make them available.

## Why Not use Dropbox or Google Drive?

Dropbox, Google Drive and other services offer some form of version control in their systems. There are times when this may be sufficient for your needs. However there are a number of advantages to using a version control system like Git:

* Language support: Git supports both text and programming languages. As research moves to include more digital techniques and tools it becomes increasingly important to have a way of managing and sharing both the ‘traditional’ outputs (journal articles, books, etc.) but also these newer outputs (code, datasets etc.)
* More control: a proper version control systems gives you a much greater deal of control over how you manage changes in a document, including the ability to comment on every change making it easier to revert.
* Useful history: using version control systems like Git will allow you to produce a history of your document in which different stages of the documents can be navigated easily both by yourself and by others.

## What are Git and GitHub?

Though often used synonymously, Git and GitHub are two different things. Git is a particular implementation of version control originally designed by Linus Torvalds as a way of managing the Linux source code. [Other systems](https://en.wikipedia.org/wiki/Comparison_of_version_control_software) of version control exist though they are used less frequently. Git can be used to refer both to a particular approach taken to version control and the software underlying it.

GitHub is a company which hosts Git repositories (more on this below) and provides software for using Git. This includes ‘GitHub Desktop’ which will be covered in this tutorial. GitHub is currently the most popular host of open source projects by [number of projects and number of users](https://en.wikipedia.org/wiki/Comparison_of_source_code_hosting_facilities#Popularity).

Although GitHub’s focus is primarily on source code, other projects are increasingly making use of version control systems like GitHub to manage the work-flows of journal publishing, open textbooks, other humanities projects, and teaching materials. 

Becoming familiar with GitHub will be useful not only for version controlling your own documents but will also make it easier to contribute and draw upon other projects which use GitHub. In this lesson the focus will be on gaining an understanding of the basic aims and principles of version control by uploading and version controlling a plain text document. This lesson will not cover everything but will provide a starting point to using version control.

***

*Materials used in these lessons are derived from Daniel van Strien's ["An Introduction to Version Control Using GitHub Desktop,"](http://programminghistorian.org/lessons/getting-started-with-github-desktop), Programming Historian, (17 June 2016). [The Programming Historian ISSN 2397-2068](http://programminghistorian.org/), is released under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*
