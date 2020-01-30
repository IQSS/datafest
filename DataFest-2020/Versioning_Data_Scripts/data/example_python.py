#!/usr/bin/env python3

# Import packages at beginning of script.
# matplotlib and seaborn needed for Anscombe's quartet example
import matplotlib.pyplot as plt
import seaborn as sns

# 1. prints "Hello world!" text to the screen when the program is run.
print("Hello world!")

# 2. Calculate pi



# 3. Square function
# adapted from https://hbctraining.github.io/Intro-to-R/lessons/03_introR-functions-and-arguments.html#user-defined-functions
# and https://www.r-bloggers.com/how-to-write-and-debug-an-r-function/
x = 5
square = x*x
print(square)

# 4. Anscombe's quartet
# https://en.wikipedia.org/wiki/Anscombe%27s_quartet
# code from https://seaborn.pydata.org/examples/anscombes_quartet.html
# set seaborn "ticks" theme
sns.set(style="ticks")

# Load the example dataset for Anscombe's quartet
anscombes_quartet = sns.load_dataset("anscombe")

# Show the results of a linear regression within each dataset
# will create 4 plots for each of the datasets
# reference https://seaborn.pydata.org/generated/seaborn.lmplot.html for descriptions of what these parameters do
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=anscombes_quartet,
           col_wrap=2, ci=None, palette="colorblind", height=4,
           scatter_kws={"s": 50, "alpha": 1})
# save the plots to a file
plt.savefig("anscombe.png")
# if you'd prefer to view the figure instead of saving it to a file, then uncomment and run the next line:
#plt.show()
