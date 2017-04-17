---
layout: default
title: "Getting Started with Github Desktop"
author: "Daniel van Strien, Radhika Khetani, Bob Freeman, Amir Karger"
output: html_document
---

>> NOTE: Materials used in these lessons are derived/adapted from [Daniel van Strien's "An Introduction to Version Control Using GitHub Desktop," Programming Historian, (17 June 2016)](http://programminghistorian.org/lessons/getting-started-with-github-desktop) and from [Software Carpentry instructional material](https://swcarpentry.github.io/git-novice/). Licensing information available at the bottom of this page.

## Getting Started with Github Desktop

GitHub Desktop offers a Graphical User Interface (GUI) to use Git, and will allow us to easily start using Version Control. Though there are advantages to using the command line version of Git in the long run, a GUI is a good place to start. 

> **A Note on Terminology**
> 
> One of the trickier aspects of using GitHub is the new terminology (`repository`,`add`, `commit`, `pull`, `push`, `remote`, `detached head`). Some of the commands/terms are fairly self-explanatory, others less so, and in this workshop you will encounter some of these. [Here is a glossary](https://help.github.com/articles/github-glossary/), however it is best to pick up terminology wile learning how to use GitHub.

### Register for a GitHub Account

Since we are going to be using [GitHub](https://github.com/) we will need to register for an account at GitHub if we don’t already have one. For [students](https://education.github.com/pack) and [researchers](https://github.com/blog/1840-improving-github-for-science) GitHub offers free private repositories. These are not necessary but might be appealing if you want to keep some work private.

### Install GitKraken

Most of you should have already installed [GitKraken](https://www.gitkraken.com/download). Open it, and sign in using the credentials you used to sign up for a github account. 

<img src="img/setup.png" width="700" align="center">

<img src="img/setup2.png" width="700" align="center">

Once you sign in, GitKraken will take you to it's Welcome screen. At this point, you are ready to start working with a repository.


## Version Controlling a directory of files

### Creating a Repository

Git tracks the contents of a folder by creating a repository in a given folder; so it is important to organize projects in folders. 

Tracking items in a folder (repository) using Git:

* The repository is made up of a folder whose contents are ‘watched’ for changes by Git
* A repository can have many files and sub-folders
* Create a repository for each major project you are working on
* These folders are like the normal folders you would have on your computer for different projects, though the files in the folders have to be deliberately added to the repository in order to be version controlled.
* It can be set up to ignore some items in the folder (very large datasets, or temp files)
* Do not create repositories for folders within a repository (avoid matryoshka repos!)

Download the folder we have generated for this session [from here](https://github.com/IQSS/datafest/raw/master/versioning/data/DataFest2017.zip), and unzip it in a location of your choosing.


### Creating a Folder/Repository 

There are a number of different ways to add files/folders for GitKraken to track. For this lesson, click on the folder icon at the top left. This will allow you to Open an existing repository, Clone a repository that you or someone else has created, or Init (create) a new repository. We will do the latter. 

Click on Init, and then GitHub.com, so that we can create a repository that we will keep locally, as well at a remote location as a backup or perhaps for sharing:

<img src="img/init.png" width="700" align="center">

Fill in the fields as appropriate:
* your account
* the name of the repository. Keep this to letters, numbers, and underscores.
* a good description
* set the access for the remote location, whether this should be viewable by anyone, or kept private to yourself and people that you specifically add as collaborators
* leave the Clone after init option checked
* For the New repository path, select the location on your local computer or shared drive / mounted volume where the repo folder should be placed. Please include the name of the folder to house the repo and its files, or create the new folder inside this Browse window.
* Finally, click on the Create Repository and Clone button.

Voila! You now have your first Git repo!

<img src="img/init.png" width="700" align="center">

Once we have added our folder we will be able to see it in a list of repositories on the left column.

<img src="img/first_repo.png" width="700" align="center">

We'll point out a few feature here:
* a list of known/open repos at the top left
* a button/function bar in the top middle
* a listing of the branches for your local and linked remote repositories
* and then the commit (snapshot) message and files that are part of this commit

Since we'll now want to add more files to this repository, right-mouse click on the README.md file and select Show in Finder (Show in Explorer) from the pop-up menu:

<img src="img/show_in_finder.png" width="700" align="center">

The folder we created the repsitory with now contains an extra folder with the name ‘.git’ (this is a hidden folder). This folder is how GitHub Desktop will track changes (adding files/folders, modifying existing ones, deleting files/folders) we make within our version controlled folder: 

<img src="img/finder_view.png" width="700" align="center">


### Staging and Committing Changes

We need to copy in our sample files that you've downloaded. Open up that folder, and copy/move those files here. Your window should look something like this:

<img src="img/finder_view_added_files.png" width="700" align="center">

When we switch back to GitKraken, you'll notice the timeline window at the top has changed. GitKraken has noticed files have changes, and it's indicated this new set of changes is considered Work in Progress:

<img src="img/first_wip.png" width="700" align="center">

Click on the WIP line at the top to show the files it is watching, show in the bottom pane. You can resize this panel to show all the files if you desire:

<img src="img/file_list_resize.png" width="700" align="center">

A **commit** tells Git that you made some changes which you want to record. Though a **commit** seems similar to saving a file, there are different aims behind ‘committing’ changes compared to saving changes. **Commits** take a snapshot of the file at that point and allow you to document information about the changes made to the document.

We next need to tell Git that we wish to prep these files for a commit, what we call an initial commit, when we take a snapshot of the files at the start of our work and any tracking that we wish to do. To include these files for a commit, we Stage the changes by clicking on the 'Stage all changes' button:

<img src="img/initial_commit_stage.png" width="700" align="center">

You do have the option of adding only certain files to the Staging area if you wish to make separate commits. Simply click on the work Stage that appears near the files you wish to include.

To commit changes you must give a summary of the changes, include an optional message, and click on the Commit button:

<img src="img/local_change.png" width="700" align="center">

After the commit, the timeline changes to reflect the current state & history of our repository. Clicking on the top line, our recent commit, shows in the bottom pane the changes that were include, which is the addition (green plus square) of these files:

<img src="img/local_change_after_commit.png" width="700" align="center">

A useful way to think about commits is as the ‘history’ of your project. Each commit records a development or change made to the documents in your repository; the history of the project can be traced by looking at all of the commits. 

* Think carefully about when to make commits, since the advantages of version control rely on taking snapshots of your changes regularly.
* Make the commits "atomic", i.e. **commit** a few related changes together; this will help if you have to revert back to a specific version/snapshot. 
* Use meaningful **commit summaries** and **messages**, so that your messages/summaries are independently understandable by your collaborators and your future self.

> **Note about Branches**:
>
> When you commit you will see ‘commit to master’. This refers to the **master** branch. 
> 
> Within a Git repository it is possible to have multiple ‘branches’. These different branches are essentially different places in which to work. Often they are used to test new ideas or work on a particular feature without modifying or "contaminating" the master copy (e.g. production version of a webpage). This feature is very useful when collaborating with others. We do not have time to go into this aspect of Version Control today, but we encourage you to explore it further.


### Changing File Contents and Committing Changes

Let's open the `mars.txt` document using our favorite text editor (see note below about text editors) and add a couple of lines to it.

```
Mars is a red planet.
It is cold and dry, but everything is my favorite color.

The two moons may make things interesting
```

Save the changes to your file and go back to GitKraken. Again, the program creates a new WIP timeline entry as it has detected changes. Click on this line to show that GitKraken has noticed that our file has changed (file icon with an elipsis inside):

<img src="img/tracking_mars.png" width="700" align="center">

When you click on the filename, you will see that these new lines of text appear; this lets us know that Git is able to see changes in your file but at the moment these changes haven’t been recorded in an official ‘snapshot’ of your repository. To do this we need to **add** and **commit** our changes, just as we did before.

<img src="img/git-staging-area.png" width="700" align="center">


> **Text Editors:**
>
> When creating a plain text document, you will want to use a text editor like TextWrangler (Mac) or NotePad++ (Windows) instead of Microscoft Word or the default text editors. You will also want to make sure that you save it as plain text. There are a [large number of free and paid text editors available](https://en.wikipedia.org/wiki/List_of_text_editors) to choose from.

In the context of Github Desktop the **add** command to place changes in the *staging area* is transparent to us. You can "place/add" several changes in the staging area, and only **commit** when you are ready. 

As we did with our previous initial commit, include a change message, and click on the Commit button:

<img src="img/commit_mars_first_change.png" width="700" align="center">

Again, you'll see our timeline has changed to include this commit:

<img src="img/after_commit_mars_first_change.png" width="700" align="center">


***

**Exercise**

1. Create a new folder called "learning_github", and add a couple of small text files to it from your computer. 
2. Create a repository with this folder in Github Desktop.
3. Create a new plain text file called "data-file.txt", add a line or 2 of content to it and save it to the "learning_github" folder. 
4. Go to Github Desktop, and commit the change with an approriate message.

***

### Pushing Your Changes to Your Remote Repository

At the moment we are only recording our changes locally. We may be happy to only store our changes locally, but we may want to upload our repository onto GitHub to make it public or to have it stored outside of our computer (for collaborating/sharing/backing up). 

This is straightforward in GitKraken and you do it by doing a one-way synchronization of your repository to the remote that you linked it to when you first created the repo. This one-way synchronization will **push** your repository from your computer to the GitHub website, and populate the *remote* repository on Github's servers in the process.

<img src="img/push.png" width="700" align="center">

We can now view our changes on our remote at GitHub.com. If the left pane, our remote is given the name 'origin', the standard term for the remote repository in Git (note that you can call it what you'd like. And you can have more than one remote! But that is beyond the scope of this document.) If we then right-mouse click on our 'origin', we can select the pop-up menu option View origin on Github.com:

<img src="img/view_origin_on_github.png" width="700" align="center">

Indeed, GitKraken sends us to our web browser and our repository on GitHub.com is displayed:

<img src="img/repo_on_github.png" width="700" align="center">

<font align="left">[Prev: Introduction to Version Control](01_Intro_to_versioning.md)</font>
<font align="right">[Next: Remote repositories, managing conflicts](03_Github_remote_and_conflicts.md)</font>

***

* Materials used in these lessons are derived from Daniel van Strien's ["An Introduction to Version Control Using GitHub Desktop,"](http://programminghistorian.org/lessons/getting-started-with-github-desktop), Programming Historian, (17 June 2016). [The Programming Historian ISSN 2397-2068](http://programminghistorian.org/), is released under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*

* Materials are also derived from [Software Carpentry instructional material](https://swcarpentry.github.io/git-novice/). These materials are also licensed under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*
