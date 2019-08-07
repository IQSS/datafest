---
layout: default
title: "Git(hub) Remote and Conflicts"
author: "Bob Freeman, Radhika Khetani, Amir Karger"
---

***
Previous: [Getting Started with Git using GitKraken](02_GitKraken.md)

***

## Repositories online (remote)

Once you have ‘published’ your repository it will be viewable on your profile at [GitHub.com](github.com). You can choose to keep it public or make it private; and if it's private, you can choose specific GitHub users with whom you want to share it or collaborate with.

For this lesson, we will stick with a public repository. To quickly view your repository online right-click on your remote's Origin in the left pane, and select 'View origin on GitHub.com'. This will reveal your online repository in your web browser.


<img src="img/2.new-view_origin_on_github.png" width="700" align="center">


<img src="img/2.new-repo_on_github.png" width="700" align="center">


Once your document is online, you can continue to make local changes to your file. But you will have to synchronize your local changes to reflect these changes in the published GitHub repository. GitHub stores changes both locally (on your computer) and remotely (on their servers), and it is important to keep these changes in sync. 

In GitKraken and standard Git workflows, this is accomplished by regular, intentional rounds of **Pull** and **Push**, which both **pulls** in changes from the remote repository, and **pushes** any local changes to the remote repo. 

### Making Changes Remotely

It is also possible to make a change to your repository on the web interface. We forgot to give attribution to our functions in the `util_functions.R` file. Go into the `code` directory, and click on the name of the file in the title area to take you to a new page showing your document.

Click on the 'Edit' option or icon. You will now be able to edit the file and add some new text. Let's add comments to both the square function:

```
# Square function
# adapted from https://hbctraining.github.io/Intro-to-R/lessons/03_introR-functions-and-arguments.html#user-defined-functions
# and https://www.r-bloggers.com/how-to-write-and-debug-an-r-function/

```

and the Anscombe's quartet function:

```
# Anscombe's quartet
# Examples from https://www.r-bloggers.com/using-and-abusing-data-visualization-anscombes-quartet-and-cheating-bonferroni/
```

<img src="img/3.new-edit_on_github_web.png" width="700" align="center">

Once you have made some changes to your file, you will again see the option to commit changes near the bottom of the text entry box.

<img src="img/3.new-online_commit.png" width="700" align="center">

One can also add and delete files from the repo. Since we're working in R, let's remove the python code files. One must first view the file itself (click on the file's name) to reveal the Delete (trash can) icon. Click here to delete:

<img src="img/3.delete_one_file.png" width="700" align="center">

This solitary action requires a description and subsequent Commit:

<img src="img/3.commit_delete_one_file.png" width="700" align="center">

Let's delete the other two as well. Your code repo should look like the following:

<img src="img/3.code_folder_after_deletions.png" width="700" align="center">

One can also add files and folders to the repo via the web interface. We'll keep this simple. In the `doc` folder we can add the `Pi formulas...` document from our workshop downloads folder. Navigate to the `docs` folder in the repo, and click on the Upload files button.

<img src="img/3.upload_files_button.png" width="700" align="center">

This action also requires a Description and subsequent Commit:

<img src="img/3.commit_uploaded_file.png" width="700" align="center">

You should now see the `Pi Formulas...` document in your `docs` folder.

Two important sidebars: since on GitHub.com file changes are done serially, coodinated file changes cannot be done here -- the must be done on your local machine with GitKraken. Also, all these changes are realtime on the GitHub remote -- Once you have committed these changes these changes are immediate.

Let's return to our local machine. GitKraken has already noticed that our remote repo has changed, and the markers for the two repos (local and remote) have diverged:

<img src="img/3.new-local_remote_differ_on_commits.png" width="700" align="center">

Click on the timeline entry to view the file changes:

<img src="img/3.view_remote_commit_changes.png" width="700" align="center">

And click on the filename itself to see the changes made within:

<img src="img/3.view_remote_file_diff.png" width="700" align="center">

You can see from this view that we now have the text with changes highlighted in <span style="color:green">green</span> and <span style="color:red">red</span>. <span style="color:red">Red</span> indicates where things have been removed, while <span style="color:green">green</span> indicates additions. 

Click on the filename again to return to our commit timeline.

To get all these changes back onto our own (local) computer, we need to Pull these changes back to our local repo, using the Pull button in the GitKraken toolbar towards the top of the screen:

<img src="img/3.new-pull.png" width="700" align="center">

If all goes well, you should see a brief 'Success' message, and your repos should be in sync again:

<img src="img/3.local_remote_in_sync.png" width="700" align="center">


## Viewing File Histories

One very useful feature of this and other Git clients is looking at how a file has changed over time. In GitKraken, select the timeline entry 'Refactor code...', and in the section below, right-mouse click on the `scriptlets.R` file and select "File History" to see exactly that: 

<img src="img/3.new-get_to_file_history.png" width="700" align="center">

Our code file is displayed with comments on the left and differences between the (left) selected and previous versions:

<img src="img/3.new-showing_file_history.png" width="700" align="center">

Clicking on the previous comment shows the next level of changes:

<img src="img/3.new-file_history_previous_comments.png" width="700" align="center">

And finally, clicking on the File View button shows all the changes together, with the log (legend) of changes being indicated with color coding:

<img src="img/3.new-history_combined_file_view.png" width="700" align="center">

Click on the X at the upper right to close this window and return to the commit timeline.



## Managing Conflicts

A **conflict** emerges when you try to merge (sync) two versions of a document with changes which conflict with each other. If you are careful about committing and syncing then it is unlikely you will run into this issue; but if you do, it can be resolved fairly easily.

The most likely way a conflict will emerge is if you, or if you are sharing your repo with a collaborator, make a change on either the local or online repo, and then make a subsequent change on the other without first syncing the changes.

If you make changes in different parts of a file or within the repo, these changes can be merged (synced) together without any conflict. But if these changes conflict with one another – if you try and change the same line of the document in two different ways – that's when there is an issue, as Git will not know which change is the one you wish to keep.

<img src="img/conflict.png" width="700" align="center">

An example will help illustrate the most likely way conflicts can emerge, and how to deal with them. 

Let's add a change to our remote repository to main documentation `README.md` file. The first title line isn't properly formatted. Let's edit this file and line with a single `#` as an H1 tag:

<img src="img/3.new-edit_online_to_start_conflict.png" width="700" align="center">

Don't forget commit this change on the website. 

Without syncing, make a change to the same document using the text editor locally:

<img src="img/3.new-edit_locally_to_make_conflict.png" width="700" align="center">

Save the changed file. Return to GitKraken, click on the WIP line, stage your change, add a description, and Commit:

<img src="img/3.new-local_conflict_commit.png" width="700" align="center">

Note the divergence as a branch. Synchronize the repos by doing a Push. GitKraken warns us that we are behind the remote, so we must do a Pull:
 
<img src="img/3.new-local_pull_warning.png" width="700" align="center">
 
Once you do the Pull, we get a transient message about a 'Merge Conflict' and a timeline message warning us about "Merge Conflicts", which is not unexpected:

<img src="img/3.new-merge_confict_warning.png" width="700" align="center">

This is not a big problem: What Git is aking you to do is manage these conflicts. GitKraken offers you the option of opening the file with the sync conflicts.

Instead, open the file with an external text editor (the document will open with whichever text editor/application we have chosen as the default for opening Markdown files). 

<img src="img/merge.png" width="400" align="center">

Looking at the file, we will see Git has denoted the conflicting section (selected here).

<img src="img/3.new-conflict_text.png" width="600" align="center">

This conflicting section is marked with `<<<<<<<` and ends with `>>>>>>>`. These are known as the **conflict markers**. The two conflicting blocks are divided by a `=======` line. 

There are a number of approaches to dealing with a conflict:

* You could choose to go with either of the changes by deleting the version you no longer want and removing the conflict markers, OR

* You could change the section entirely and not choose either of the options, OR

* You could keep both of the versions

Whichever option you choose, you must **remove** the conflict markers in order to proceed. We're going to keep the local copy, as it is more informative. Once you have *resolved* the conflict, save the file, click on the conflict timeline entry, and indicate to GitKraken that you have resolved the problem in the lower section:

<img src="img/3.new-conflict_resolved.png" width="600" align="center">

and then proceed to **commit** and merge the changes (resolved conflict). When you go to Commit your changes you see that GitKraken specifies that the commit is to merge a conflict. This is useful historical information if you later wish to review how you managed any conflicts:

<img src="img/3.new-commit_and_merge_conflict.png" width="600" align="center">

GK now shows our commit & its message in the timeline in the upper pane:

<img src="img/3.new-merged_conflict_timeline.png" width="600" align="center">

Now, synchronize your local changes by the standard workflow of **Pull and Push** and your local and remote repositories will be in sync:


<img src="img/3.new-commit_conflict_synched_timelines.png" width="700" align="center">

This may seem like a convoluted approach to dealing with conflicts, but it is very useful as you have total control and the last word in dealing with conflicts. In contrast, if conflicts emerge on a system like Dropbox, the result is two files being created: Although this is better than potentially losing important changes, it also means you still have to look at these two documents and decide how you are going to merge them. 

If you are careful about always syncing changes you will be able to avoid having to deal with conflicts. When collaborating, the likelihood for conflicts increases; so, it is useful to be aware of how to deal with conflicts before you begin to collaborate using GitHub. 

***

**Exercise**

1. Publish the "learning_github" repo. 
2. Create a conflict within the "data-file.txt" file by making changes locally and remotely.
3. Resolve the conflict and commit.
4. [Optional] Add your neighbor as a collaborator to a the "learning_github" repo (in Settings -> Collaborators & teams), make changes to create a conflict within the "data-file.txt" document in one of the repos (pick one), and resolve the conflict.


***
Next: Working with Commits

***

* Materials used in these lessons are derived from Daniel van Strien's ["An Introduction to Version Control Using GitHub Desktop,"](http://programminghistorian.org/lessons/getting-started-with-github-desktop), Programming Historian, (17 June 2016). [The Programming Historian ISSN 2397-2068](http://programminghistorian.org/), is released under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*

* Materials are also derived from [Software Carpentry instructional material](https://swcarpentry.github.io/git-novice/). These materials are also licensed under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*
