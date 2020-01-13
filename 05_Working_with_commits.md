---
layout: default
title: "Working with Commits"
author: "Bob Freeman, Radhika Khetani, Amir Karger"
---

***
Previous: [Remote repositories, managing conflicts](03_Github_remote_and_conflicts.md)

***
Objectives:
- Learn how to amend a commit
- Learn how to revert a commit
- Learn how to work with a previous commit
- Learn how to temporarily hide work in progress


## Working with Commits

Sometimes a simple commit isn't that simple: you've forgotten something, you need to undo what you've done, or you need to go back to something you committed some time ago. This section with help you navigate these items.

## Amending Commits

Oops! Pushed 'Commit' button too fast? As long as you have not updated any remotes, you can amend the last commit message, add additional changes, or both.

To make changes / add files, click on the //WIP node on the graph:

<img src="img/4.01.WIP_amend.png" width="700" align="center">

stage the files would wish to include in the updated commit, and selected the Amend checkbox in the Commit Message pane:

<img src="img/4.02.amend_checkbox.png" width="700" align="center">

You'll note that the previous commit message is copied into the Message and Description fields. And the Commit button is titled Amend Previous Commit instead. Go ahead.

If you wish to amend the message only, hover over and click on the commit message in the bottom pane for the latest commit:

<img src="img/4.03.click_on_commit_message.png" width="700" align="center">

Change your commit message, and click on the Update Message button at the bottom:

<img src="img/4.04.update_message_button.png" width="700" align="center">


## Reverting Commits

Sometimes you just want to undo the last thing you did. Like that last change (e.g. commit, branch, etc) you didn't mean to make? GitKraken's Undo button in the top toolbar will let you undo most actions (which can also Redo if needed!). Hover over the Undo button to see what action it will take, and click if that seems appropriate:

<img src="img/4.05.undo_button_hover.png" width="700" align="center">

If the Undo option is not available or not appropriate, one can use the Revert Commit option for the latest commit or even a previous one. This will not only bring back the changes to your working directory, but will include an explicit commit to document that this change to the repo. To perform this, click on the commit node, and right-mouse click to see the popup menu. From there, select the Revert Commit option:

<img src="img/4.06.revert_commit_popup_menu.png" width="700" align="center">
  
When prompted, you can immediate commit this explicit change, or keep the changes as a WIP (work in progress) for you to do additional work. Clicking Yes enters the new commit to your repo:

<img src="img/4.07.commit_a_revert_commit.png" width="700" align="center">

**Exercises-Coming soon!**

## Resetting (Checking Out Previous) Commits, and Stash/Pop

At times, there may be the need to go back in history to a previous commit: perhaps you wish to retrieve files that you've deleted or changed, or perhaps you wish to inspect the state of your project and code to inform current work. No matter, like a time machine, Git allows you to move the pointer on your repo to any commit, and it will likewise change the repo files and structure to reflect that.

To get us there, we're going to do a little cleanup on our project repo. We forgot to include the other files from our project download, so let's include those files in a folder and make the commit:

<img src="img/4.07b.project_files_cleanup_status.png" width="700" align="center">


In addition, you should create two new files for Jupiter and Saturn, and add those to the project directory, creating a WIP entry. Your commit timeline should look like the following:

<img src="img/4.08.repo_cleanup_status.png" width="700" align="center">

But we realized that we had, in a previous commit, that we deleted the entries for other outer planet entries (asteroid belt, Uranus, & Neptune). Now, we want those back. Working with a previous commit will help us here. If we right-click on the previous commit with these files, "Including outer system planets", we have an option to "Reset master to this commit", with three options: soft, mixed, and hard:

<img src="img/4.09.reset_master_options.png" width="700" align="center">

Although using the 'soft' option may seems safest -- keeping any changes -- one could run into problems if there are files that overlap or change over time. We don't want conflicts. But the 'hard' option seems extreme. What about the files we've added to our project that haven't yet saved? 

Stash to the rescue! This option let's us hide our current work and changes to a safe, hidden, location, so that when resetting our commit pointer we won't lose our work. 

<img src="img/4.10.stash_button.png" width="700" align="center">

After stashing, we have an indicator that our files are safe; and we can see the previous commit is still present:

<img src="img/4.11.after_stash.png" width="700" align="center">

So let's go back to our previous commit "Including outer system planets" and click on it to highlight:

<img src="img/4.12.highlight_previous_commit.png" width="700" align="center">

Right-mouse click, select "Reset master to this commit", and the option "Hard - discard all changes". Your commit pointer for local repo will now point to this commit:

<img src="img/4.13.commit_pointer_changed.png" width="700" align="center">

and the project repo will change accordingly:

<img src="img/4.14.reset_project_repo.png" width="700" align="center">

Let's grab the three files from our project repo -- asteroid belt, Uranus, & Neptune -- and set them aside. Let's fast-forward the commits to go back to our previous state by highlighting the last commit, right-mouse click it, and select the same reset commit options: "Reset master to this commit" > "Hard - discard all changes":

<img src="img/4.15.ff_reset to latest_commit.png" width="700" align="center">

Now that we're back to where we were, let's get our stashed, hidden repo changes back by using the Pop option:

<img src="img/4.16.using_pop_to_retrieve_changes.png" width="700" align="center">

Once popped, we can see our files where we'd left them:

<img src="img/4.17.files_after_pop.png" width="700" align="center">

And finally, let's organize our files into a coherent folder, reflected both in our filesystem:

<img src="img/4.18.files_organized_in_folder.png" width="700" align="center">

and make this commit in GitKraken:

<img src="img/4.19.commit_reorganized_files.png" width="700" align="center">

**Exercises-Coming soon!**

## Next steps and Resources

GitKraken offers an easy way of getting started with GitHub and version control. Depending on your use case it may be sufficient for your needs. If you are already familiar with using the Command Line then using Git on the Command Line is recommended. 

This lesson introduced you to the most rudimentary (yet very useful) concepts and terminology associated with using Version control (Git). The resources below will allow you get started with getting a deeper/better understanding of version control.

* The [GitKraken guide](https://support.gitkraken.com/getting-started/guide) is a great way to start exploring it's functionality, and learning more about what Git can do.
* GitHub also provides extensive support in the form of [guides](https://guides.github.com/) and [help](https://help.github.com/).
* GitHub [Glossary](https://help.github.com/articles/github-glossary/) outlines the most commonly used GitHub/Git terminology.

***

* Materials used in these lessons are derived from Daniel van Strien's ["An Introduction to Version Control Using GitHub Desktop,"](http://programminghistorian.org/lessons/getting-started-with-github-desktop), Programming Historian, (17 June 2016). [The Programming Historian ISSN 2397-2068](http://programminghistorian.org/), is released under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*

* Materials are also derived from [Software Carpentry instructional material](https://swcarpentry.github.io/git-novice/). These materials are also licensed under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).*

* Materials are also derived from [GitKraken Support for Git Client](https://support.gitkraken.com/start-here/interface/) on GitKraken's website. 
