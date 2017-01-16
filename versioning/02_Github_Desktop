---
layout: default
title: "Versioning with Git/Github"
author: "Daniel van Strien, Radhika Khetani, Bob Freeman, Amir Karger"
output: html_document
---

# Version Control with Git/Github

>> NOTE: Materials used in these lessons are derived/adapted from [Daniel van Strien's "An Introduction to Version Control Using GitHub Desktop," Programming Historian, (17 June 2016)](http://programminghistorian.org/lessons/getting-started-with-github-desktop). Licensing information available at the bottom of this page.

## Getting Started with Github Desktop

GitHub Desktop will allow us to easily start using version control. GitHub Desktop offers a Graphical User Interface (GUI) to use Git. Though there are some potential advantages to using the command line version of Git in the long run, using a GUI can reduce the learning curve of using version control and Git. If you decide you are interested in using the command line you can find more resources at the end of the lesson.

### A Note on Terminology

One of the trickiest aspects of using GitHub is the new terminology. Some of the commands are fairly self-explanatory, others less so. This tutorial will try and briefly summarise new terms. It may also be helpful to have a [glossary](https://help.github.com/articles/github-glossary/) on hand to refer to. But in general it can be best to pick up terminology through using GitHub rather than trying to understand all of the terms before you begin using it.

### Register for a GitHub Account

Since we are going to be using [GitHub](https://github.com/) we will need to register for an account at GitHub if we don’t already have one. For [students](https://education.github.com/pack) and [researchers](https://github.com/blog/1840-improving-github-for-science) GitHub offers free private repositories. These are not necessary but might be appealing if you want to keep some work private.

### Install GitHub Desktop

Most of you should have already installed [Github Desktop](https://desktop.github.com/). Open it and sign in using the credentials you used to sign up for a github account. 

<img src="img/setup.png" width="200" align="center">

<img src="img/setup2.png" width="350" align="center">

Once you sign in, you'll see that there is already a tutorial repository available to you.

<img src="img/new.png" width="700" align="center">

## Version Controlling a directory of files

### Creating a Repository

Git tracks the contents of a folder by creating a repository in a given folder; so it is important to organize projects in folders. 

Tracking items in a folder (repository) using Git:

* The repository is made up of a folder whose contents are ‘watched’ for changes by Git.
* A repository can have many files and sub-folders
* It is best to create one repository for each major project you are working on, i.e., one repository for an article, one for a book, and one for some code you are developing. 
* These folders are like the normal folders you would have on your computer for different projects, though the files in the folders have to be deliberately added to the repository in order to be version controlled. 
* It can be set up to ignore some items in the folder (very large datasets, or temp files)
* Do not create repositories for folders within a repository (avoid matryoshka repos!)

Download the folder we have generated for this session [from here](https://github.com/IQSS/datafest/raw/master/versioning/data/DataFest2017.zip), and unzip it.

### Adding a Folder/Repository

There are a number of different ways to add files/folders for GitHub Desktop to track. We can drag the folder containing the file onto GitHub Desktop. When you do this you will be asked whether you want to create a repository for this folder. Alternatively we can click on the ‘plus’ icon to open a window to choose folders we want to add. 

<img src="img/add.png" width="700" align="center">

Once we have added our folder we will be able to see it in a list of repositories on the left column.

<img src="img/repo1.png" width="700" align="center">

If we choose the repository we just added we will see the files contained in that repository. From this menu we can choose which files we want to version control. (There might be times when we are working on projects in which files are produced which we don’t need or want to version control.) On the right we will see the current document.

If we were to look at hidden folders in the folder we have just added to GitHub you will see that the folder now contains an extra folder with the name ‘.git’. This folder is how GitHub desktop tracks changes we make within our version controlled folder whether these changes be adding new files or modifying existing ones.

Let's open the `mars.txt` document using our favorite text editor (see note below) and add a couple of lines to it.

```
Mars is a red planet.
It is cold and dry, but everything is my favorite color.

The two moons may make things interesting
```
> **Text Editors:**
> When creating a plain text document, you will want to use a text editor like TextWrangler (Mac) or NotePad++ (Windows) instead of Microscoft Word or the default text editors. You will also want to make sure that you do not save it as Rich Text Format, but as plain text. There are a huge number of free and paid text editors available. Some of these are very straightforward and simple to use while others have a learning curve and potential uses beyond simple text editing. In the long run using a more advanced and extendable text editor like Vim or Emacs may save you time.

Save the changes to your file and go back to GitHub Desktop. You will see that these new lines of text appear. This lets us know that GitHub is able to see changes in your file but at the moment these changes haven’t been recorded in an official ‘snapshot’ of your repository. To do this we need to **add** and **commit** our changes.

<img src="img/git-staging-area.png" width="700" align="center">

In the context of Github Desktop the **add** to place changes in the *staging area* is completely transparent. However, it is important to know these terms for a proper understanding of how Git functions. You can place several changes in the staging area, and only **commit** when you are ready. But, do spend some time thinking about how and if all these changes go together, it might be best to only group a few related changes together in the staging area before the **commit** step.

### Committing Changes

A **commit** tells Git that you made some changes which you want to record. Though a **commit** seems similar to saving a file, there are different aims behind ‘committing’ changes compared to saving changes. **Commits** take a snapshot of the file at that point and allow you to document information about the changes made to the document.

To commit changes you must give a summary of the changes and include an optional message. It is important that you think carefully about when to make commits, since the advantages of version control taking snapshots of your changes regularly relies on you making commits. It is often tempting to just commit changes when you have finished working on a document but this might not reflect when important changes occurred.

<img src="img/local_change.png" width="700" align="center">

When you commit you will see ‘commit to master’. This refers to the ‘master branch’. Within a Git repository it is possible to have multiple ‘branches.’ These different branches are essentially different places in which to work. Often they are used to test new ideas or work on a particular feature without modifying or "contaminating" the master copy (e.g. production version of a webpage). Initially it is not necessary to use the branches feature of GitHub, but you may want to learn to use it in the future, particularly if you want to use GitHub to collaborate on a repository with other people. 

A useful way to think about commits is as the ‘history’ of your document. Each commit records a development or change made to the documents in your repository; the history of the document can be traced by looking at all of the commits. For this history to be useful later on, either for ourselves or for someone else, it is important that this history is recorded at relevant points. Trying to make commits ‘atomic’ is an important consideration. What this means is that each commit ‘makes sense’ on its own. The changes in the commit and the message are understandable without having to look at surrounding commits.

> **Commit Messages**: It is important that you use meaningful commit summaries and messages. You don't need to write which files were changes, as Git will track that by itself; you should describe changes at a higher level. Writing good commit messages requires some prior thought. This is especially important when you are working on a collaborative project, as it is especially important that other people can understand your commit messages. 

### Publishing Your Repository

At the moment we are only recording our changes locally. We may be happy to only store our changes locally (it is still important to back our files up) but we may want to upload our repository onto GitHub to make it public or to have it stored outside of our computer (for collaborating/sharing/backing up). 

The process of doing this through GitHub Desktop is straightforward. On GitHub desktop you ‘publish’ repositories. This will **push** your repository from your computer to the GitHub website and set up a *remote* repository on Github's servers in the process.

<img src="img/publish.png" width="700" align="center">

***

*Materials used in these lessons are derived from Daniel van Strien's ["An Introduction to Version Control Using GitHub Desktop,"](http://programminghistorian.org/lessons/getting-started-with-github-desktop), Programming Historian, (17 June 2016). [The Programming Historian ISSN 2397-2068](http://programminghistorian.org/), is released under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*
