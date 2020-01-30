#!/usr/bin/env python3

# Import packages at beginning of script.
# matplotlib and seaborn needed for Anscombe's quartet example
import matplotlib.pyplot as plt
import seaborn as sns

# Define the four functions.

# 1. prints "Hello world!" text to the screen when the function is called.
def greeting():
    print("Hello world!")

# 2. Calculate pi



# 3. Square function
# adapted from https://hbctraining.github.io/Intro-to-R/lessons/03_introR-functions-and-arguments.html#user-defined-functions
# and https://www.r-bloggers.com/how-to-write-and-debug-an-r-function/

# function returns the squared value of a integer, assuming an integer is passed to it
def square_it(x):
    square = x*x
    return square

# 4. Anscombe's quartet
# https://en.wikipedia.org/wiki/Anscombe%27s_quartet
# code from https://seaborn.pydata.org/examples/anscombes_quartet.html
def anscombe():
    # set seaborn "ticks" theme
    sns.set(style="ticks")

    # Load the data for Anscombe's quartet from the seaborn package
    anscombes_quartet = sns.load_dataset("anscombe")

    # Show the results of a linear regression within each dataset
    # will create 4 plots, one for each of the datasets
    # reference https://seaborn.pydata.org/generated/seaborn.lmplot.html for descriptions of what these parameters do
    sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=anscombes_quartet,
           col_wrap=2, ci=None, palette="colorblind", height=4,
           scatter_kws={"s": 50, "alpha": 1})
    # save the plots to a file
    plt.savefig("anscombe.png")
    # if you'd prefer to view the figure instead of saving it to a file, then uncomment and run the next line:
    #plt.show()

# Code that doesn't belong in functions goes here
# Call each of the functions
def main(): 
    greeting()
    # will need to call calculate pi function here once it is written
    print( square_it(5) )
    anscombe()

# see https://docs.python.org/3.7/library/__main__.html
if __name__ == '__main__':
    main()
