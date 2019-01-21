#######################################################################################################
##################################################### SETUP ###########################################
#######################################################################################################

# Our data -- two csv files
	# fraud.csv for demonstration
	# flower.csv for exercises
# Install all necessary packages 

#######################################################################################################
##################################################### END SETUP #######################################
#######################################################################################################

# sklearn: machine learning
# pandas: flexible data structures for analysis
# numpy: n-dimensional arrays

import sklearn
print(sklearn.__version__)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import recall_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt

################################################## Data Preprocessing #######################################################

# Read a csv datafile into a dataframe  
data = pd.read_csv('https://raw.githubusercontent.com/IQSS/datafest/master/DataFest-2019/machine-learning-workflow/fraud.csv')
# Set display option to print out all columns on console
pd.set_option('display.max_columns', 100)
# print out the first 5 records
print(data.head(5))

# For an 1d array (class label column), print out the object that contains counts of unique values
print(data.isFraud.value_counts())

# Obtain the feature subset, the output is a dataframe
features = data.loc[:, (data.columns != 'isFraud')]
# Obtain the class column, the output is a dataframe
classLabel = data.loc[:, (data.columns == 'isFraud')]

# Separate both feature subset and class vector into two parts, output has the same datatype as the input
features_train, features_test, classLabel_train, classLabel_test = train_test_split(features, classLabel, test_size = 0.3, random_state = 0)

################################################## Reshape ##################################################################

# Reshape the class column (a dataframe) of the testing set into an 1d array
print("classLabel_test shape before: {}".format(classLabel_test.shape))
c, r = classLabel_test.shape
classLabel_test = classLabel_test.values.reshape(c,)
print("classLabel_test shape after: {}".format(classLabel_test.shape))

# Reshape the class column (a dataframe) of the training set into an 1d array
print("classLabel_train shape before: {}".format(classLabel_train.shape))
cc, rr = classLabel_train.shape
classLabel_train = classLabel_train.values.reshape(cc,)
print("classLabel_train shape after: {}".format(classLabel_train.shape))

################################################## Default Single Tree #######################################################

# Build the default tree -- no thresholds and natural stop

# Create an object of this class
dt_default = DecisionTreeClassifier(random_state = 123)
# Build a decision tree classifier from the training set.
dt_default.fit(features_train, classLabel_train)
# Predict class for each sample in the testing set, input is a dataframe, output is a list/1d array
classLabel_test_predict = dt_default.predict(features_test)
# Obtain recall score, inputs are 1d array for true target values and 1d array for estimated targets, return a float
recall_default = recall_score(classLabel_test, classLabel_test_predict)
print("default tree recall:: {:.8f}".format(recall_default, end = "\n\n"))

################################################## Grid Single Tree #########################################################

# Grid Parameter Search via 10-fold cross-validation -- early stop
# Letting the tree grow all the way out will overfit the training set. Tree classifier parameters control model complexity. Tuning those
# parameters to find the correct level of model complexity.

# Set up parameters and their range of values. These are predetermined arbitrarily. A dictionary data structure is required 
# with parameters names (string) as keys and lists of parameter settings to try as values.
param_grid = {"criterion": ["gini", "entropy"],
              "max_depth": [10, 15, 20, 25],
              "min_samples_split": [10, 20, 30],
              "min_samples_leaf": [5, 10, 15]}

# Create an object of this estimator 
dt = DecisionTreeClassifier(random_state = 123)
# Exhaustive search over specified parameter values for an estimator. Inputs are an estimator object, dictionary of predetermined 
# parameter values, integer for cross-validation splitting strategy, and a single string defining model evaluation rule. Return an
# object of this class  
grid_search = GridSearchCV(dt, param_grid = param_grid, cv = 10, scoring = "recall")
# Run fit over the training set with all sets of parameters.  
grid_search.fit(features_train, classLabel_train)
# Return the parameter setting that maximizes the score of the hold out data as a dictionary
dt_grid = grid_search.best_params_

# Print out the best parameters based on Recall
# Loop over each key-value pair in the returned dictionary
for k, v in dt_grid.items():
    print("parameter: {} setting: {}".format(k, v))

# Return a float as mean cross-validated score of the best estimator (the one with the best parameters). 
dt_grid_score = grid_search.best_score_
print("Mean recall score of the best parameters: {:.8f}\n\n".format(dt_grid_score))

# Estimate performance of the optimal tree [Grid] based on Recall...
# Create an object of this estimator/classifier with the best parameters derived
dt_grid_best = DecisionTreeClassifier(random_state = 123, **dt_grid)
# Build an optimal decision tree classifier from the training set
dt_grid_best.fit(features_train, classLabel_train)
# Predict class for each sample in the testing set, input is a dataframe, output is a list/1d array
classLabel_test_grid_predict = dt_grid_best.predict(features_test)
# Obtain recall score, inputs are 1d array for true target values and 1d array for estimated targets, return a float
recall_grid = recall_score(classLabel_test, classLabel_test_grid_predict)
print("Grid search tree Recall:: {:.8f}\n\n".format(recall_grid))

#######################################################################################################
########################################### EXERCISE 1 CART: ##########################################
#######################################################################################################
# NOTE: 1) Feel free to copy code from above as a starting point;
#	    2) Take reference to DecisionTreeClassifier documentation at 
#	    https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
#	    3) Take reference to GridSearchCV documentation at 
#	    https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html

# 1) Explore the dataset: a. print out the first 10 records;
#                         b. print out the class distribution.

# 2) Preprocess the dataset: a. separate feature columns from the class label column;
#							 b. separate data into a training and testing sets at ratio 8:2.
#                            c. reshape the class column into an 1d array for both training and testing sets.

# 3) Build a DEFAULT CART model and report its accuracy performance.

# 4) Use grid search method with 5-fold cross-validation to find the best tree parameters and setting as well as corresponding
#    mean accuracy. You could choose parameters different from those used in demonstration.
 
# 5) Report accuracy performance of the optimal tree. Compare this performance with that of the default tree.

# 6) (Optional) Report feature importance of the optimal tree.

#######################################################################################################
########################################### END EXERCISE 1 ############################################
#######################################################################################################

################################################# Grid Random Forest #############################################################

# Given the best individual tree-level parameters, tune two forest-level parameters--number of trees and number of subset features.
# Higher number of trees gives you better performance but makes your code slower.
# Increasing number of subset features generally improves the performance of the model as at each node we have a higher number of 
# options to be considered. However, this decreases the diversity of individual trees. It also decreases the speed of algorithm. 

# Creat a list of predetermined values for each forest-level tuning parameter 
numTrees = [100, 150, 200, 250]
max_features = [None, "log2", "sqrt"]
# Create a variable recording the maximum cross-validated mean over a grid. Initialize it equal to 0.
max_score = 0
# Loop over the numTrees list. Namely loop over every predetermined value in that list.
for i in numTrees:
	# For each predetermined value of number of trees, loop over every predetermined value in max_features list
    for j in max_features:
		# For a specific combination of number of trees and number of subset features, create an object of this estimator. 
		# n_estimators means the number of trees in the forest, max_features means the number of features to consider when
		# looking for the best split, oob_score means whether to use out-of-bag samples to estimate the generalization accuracy,
		# **dt_grid means that we use the best parameters derived from a grid single tree as the parameters for planting 
		# individual trees in this forest
        rf = RandomForestClassifier(random_state = 123, oob_score = True, n_estimators = i, max_features = j, **dt_grid)
		# Parameters are the object of the estimator used to fit the data, a dataframe for the data to fit, an 1d array for class
		# variable, integer for cv splitting strategy, and a string for model evaluation. Return an 1d array of scores of the 
		# estimator for each run of the cross validation.
        scores = cross_val_score(rf, features_train, classLabel_train, cv = 10, scoring = "recall")
        print("Recall at numTrees = {}, max_features = {}:: mean: {:.8f} (std: {:.8f})\n\n".format(i, j, scores.mean(), scores.std()))
		# Record the larger cross-validated mean over any 2 combinations and the parameter values corresponidng to the larger one.  
        if scores.mean() > max_score:
            max_score = scores.mean()
            max_numTrees = i    
            max_numFeatures = j
# After loops are finished, print out the best parameter settings and corresponding maximal cross-validated mean.
print("best number of trees: {}; max number of fearures: {}; maximum cross-validated mean recall: {}".format(max_numTrees, max_numFeatures, max_score))

# Estimate performance of the optimal Random Forest [Grid] based on Recall...
# Create an object of this estimator/classifier with the best parameters derived
rf_grid_best = RandomForestClassifier(random_state = 123, oob_score = True, n_estimators = max_numTrees, max_features = max_numFeatures, **dt_grid)
# Build a forest of trees from the trainin set
rf_grid_best.fit(features_train, classLabel_train)
# Predict class for each sample in the testing set by taking votes from the trees in the forest, input is a dataframe, output is a 
# list/1d array
classLabel_test_rf_predict = rf_grid_best.predict(features_test)
# Obtain recall score, inputs are 1d array for true target values and 1d array for estimated targets, return a float
recall_rf = recall_score(classLabel_test, classLabel_test_rf_predict)
print("Random Forest Grid Recall:: {:.8f}".format(recall_rf, end = "\n\n"))

################################################# Grid Gradient Boosting #############################################################

# Given the best individual tree-level parameters, for a given learning rate at 0.2, tune two boosting-level parameters--number of trees
# and subsample size.
# GBM is fairly robust at higher number of sequential trees to be modeled, but it can still overfit at a point. This parameter
# should be tuned for a particular learning rate.
# Subsample size is the fraction of observations to be selected for each tree. Selection is done by random sampling. Smaller size
# reduces variance but increases bias.
# Learning rate determines the impact of each tree on the final outcome. It controls the magnitude of the update in the estimates.
# Lower values are generally preferred as they make the model robust to the specific characteristics of tree and thus allowing it
# to generalize well. But it would require higher number of trees to model all the relations and will be computationally expensive.
# 
# Parameter tuning steps: 1) Choose a relatively high learning rate, 2) Determine the optimum number of trees and size of subsample
# for this learning rate, 3) Lower the learning rate and increase the optimal number of trees proportionally to get more robust model. 

# The function to measure the quality of a split. It does not support tree-specific splitting criterion. Supported criteria are some kind
# of mean squared error. The default value is generally the best as it can provide a better approximation in some cases. 
del dt_grid["criterion"]

# Create a list of predetermined values for each of two boosting-level tuning parameters 
numTrees = [60, 70, 80]
subsample = [0.6, 0.7, 0.8]
# Create a variable recording the maximum cross-validated mean over a grid. Initialize it equal to 0.
max_score_numTrees_sampleSize = 0
# Loop over every predetermined value in the numTrees list.
for i in numTrees:
	# For each predetermined value of number of trees, loop over every predetermined value in the subsample list
	for j in subsample:
		# For a specific combination of number of trees and subsample size, create an object of this estimator. 
		# learning_rate means the contribution of each tree. 
		# n_estimators means the number of boosting stages to perform.
		# subsample means the fraction of samples to be used for fitting the individual base learners.
		# **dt_grid means that we use the best parameters derived from a grid single tree as the parameters for planting 
		# individual trees in this boosting
		gbm1 = GradientBoostingClassifier(random_state = 123, learning_rate = 0.2, n_estimators = i, subsample = j, **dt_grid)
		# Parameters are the object of the estimator used to fit the data, a dataframe for the data to fit, an 1d array for class
		# variable, integer for cv splitting strategy, and a string for model evaluation. Return an 1d array of scores of the 
		# estimator for each run of the cross validation.
		scores = cross_val_score(gbm1, features_train, classLabel_train, cv = 10, scoring = "recall")
		print("when learning_rate = 0.2, recall at numTrees = {} and subsample size = {}:: mean: {:.8f} (std: {:.8f})\n\n".format(i, j, scores.mean(), scores.std()))
		# Record the larger cross-validated mean over any 2 combinations and the parameter values corresponidng to the larger one.
		if scores.mean() > max_score_numTrees_sampleSize:
			max_score_numTrees_sampleSize = scores.mean()
			max_numTrees = i   
			max_subsample = j
# After loops are finished, print out the best parameter settings and corresponding maximal cross-validated mean.
print("GBM Grid:: best number of trees: {}; best subsample size: {}; maximum cross-validated mean recall: {:.8f}".format(max_numTrees, max_subsample, max_score_numTrees_sampleSize))

# Given the best two boosting-level parameters, tune the third boosting-level parameter learning_rate. There is a tradeoff between learning_
# rate and number of stages in the boosting.
# Create a list of predetermined values for learning_rate  
learning_rate = [0.1, 0.05, 0.01]
# Create a variable recording the maximum cross-validated mean over a grid. Initialize it equal to 0.
max_score_learning_rate = 0
# Loop over every predetermined value in the learning_rate list.
for r in learning_rate:
	# For a given learning_rate in the list, set the number of stages in the boosting accordingly. Create an object of this estimator.
	gbm2 = GradientBoostingClassifier(random_state = 123, learning_rate = r, n_estimators = int(0.2/r) * max_numTrees, subsample = max_subsample, **dt_grid)
	scores = cross_val_score(gbm2, features_train, classLabel_train, cv = 10, scoring = "recall")
	print("when learning rate = {}, number of trees = {}, recall:: mean: {:.8f} (std: {:.8f})\n\n".format(r, int(0.2/r) * max_numTrees, scores.mean(), scores.std()))
	if scores.mean() > max_score_learning_rate:
		max_score_learning_rate = scores.mean()
		max_learning_rate = r
		max_number_trees = int(0.2/r) * max_numTrees
print("GBM Grid:: best pair of learning rate and number of trees: {} and {}, maximum cross-validated mean recall: {:.8f}\n\n".format(max_learning_rate, max_number_trees, max_score_learning_rate))

# Estimate performance of the optimal GBM [Grid] based on Recall...

gbm_grid_best = GradientBoostingClassifier(random_state = 123, learning_rate = max_learning_rate, n_estimators = max_number_trees, subsample = max_subsample, **dt_grid)
gbm_grid_best.fit(features_train, classLabel_train)
classLabel_test_gbm_predict = gbm_grid_best.predict(features_test)
recall_gbm = recall_score(classLabel_test, classLabel_test_gbm_predict)
print("GBM Grid Recall:: {:.8f}".format(recall_gbm, end = "\n\n"))

#######################################################################################################
########################################### EXERCISE 2 TREE BOOSTING ##################################
#######################################################################################################
## NOTE: 1) Feel free to copy code from above as a starting point.
#        2) Take reference to RandomForestClassifier documentation at:
#        https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
#        3) Take reference to GradientBoostingClassifier documentation at:
#        https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html
#        4) Take reference to cross_val_score documentation at:
#        https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html

# 1) For a given learning rate at 0.1, tune two boosting parameters--number of trees and size of subsample--together to report their best 
#    combination and corresponding average accuracy. Number of trees could be [50, 60, 70, 80]. Size of subsample could be [0.6, 0,7, 0.8, 0.9].

# 2) Given the best combination of number of trees and size of subsample from 1), tune boosting parameter learning rate to report its optimal
#    setting. Learning rate values could be [0.01, 0.05, 0.1, 0.2].

# 3) Report accuracy performance of the optimal tree boosting model. Compare this performance with that of the grid random forest model.

# 4) (Optional) Report feature importance of the optimal tree boosting model.

#######################################################################################################
########################################### END EXERCISE 2 ############################################
#######################################################################################################

########################################################## Feature Importance ##############################################################

# Call this attribute through the object of the estimator. Return a list of importance scores with the order features are fed in the model.
dt_grid_importances = dt_grid_best.feature_importances_
print(dt_grid_importances)
# Return the indices that would sort an array in descending order. 
dt_grid_indices = np.argsort(dt_grid_importances)[:: -1]
print(dt_grid_indices)

print("Feature ranking::Grid Single Tree:")
# Loop over each feature 
for f in range(features_train.shape[1]):
    print("%d. feature %d [%s] importance (%f)" % (f + 1, dt_grid_indices[f], features_train.columns.tolist()[dt_grid_indices[f]], dt_grid_importances[dt_grid_indices[f]]))

plt.figure()
plt.title("Feature importances::Grid Single Tree" )
# Inputs are sequence of scalars for the x coordinates, sequence of scalars for the heights of the bar, etc. 
plt.bar(range(features_train.shape[1]), dt_grid_importances[dt_grid_indices], color = "r", align = "center")
# Set locations and labels of the x-axis. Inputs are a list of positions at which ticks should be placed, and a list of explicit
# labels to place at the given locations
plt.xticks(range(features_train.shape[1]), dt_grid_indices)
# Set the x limits to left, right
plt.xlim([-1, features_train.shape[1]])
plt.show()


rf_importances = rf_grid_best.feature_importances_
# For each tree classifier in the list, returns a list of importance scores. The first input is a list of lists. Along rows calculating
# std means to calculate std for each feature across all trees. Returns a list of stds of each feature across all trees.
rf_std = np.std([tree.feature_importances_ for tree in rf_grid_best.estimators_], axis = 0)
print(rf_std)
rf_indices = np.argsort(rf_importances)[:: -1]
print("Feature ranking: Random Forest Grid")

for f in range(features_train.shape[1]):
    print("%d. feature %d [%s] importance (%f)" % (f + 1, rf_indices[f], features_train.columns.tolist()[rf_indices[f]], rf_importances[rf_indices[f]]))

plt.figure()
plt.title("Feature importances: Random Forest Grid" )
# yerr: add vertical errorbars to the bar tips. If input is an array, symmetric +/- values for each bar
plt.bar(range(features_train.shape[1]), rf_importances[rf_indices], color = "r", yerr = rf_std[rf_indices], align = "center")
plt.xticks(range(features_train.shape[1]), rf_indices)
plt.xlim([-1, features_train.shape[1]])
plt.show()

# Change a collection of fitted sub-estimators to a list (or an 1d array).  For each element of the list, it could be a list of multiple
# tree classifiers for multi classification, or a list of single tree classifier for binary classification. Put each tree classifier
# in a list. 
gbm_flatList = [item for sublist in gbm_grid_best.estimators_.tolist() for item in sublist]
gbm_importances = gbm_grid_best.feature_importances_
gbm_std = np.std([tree.feature_importances_ for tree in gbm_flatList], axis = 0)
gbm_indices = np.argsort(gbm_importances)[:: -1]
print("Feature ranking: GBM Grid")

for f in range(features_train.shape[1]):
    print("%d. feature %d [%s] importance (%f)" % (f + 1, gbm_indices[f], features_train.columns.tolist()[gbm_indices[f]], gbm_importances[gbm_indices[f]]))

plt.figure()
plt.title("Feature importances: GBM Grid" )
plt.bar(range(features_train.shape[1]), gbm_importances[gbm_indices], color = "r", yerr = gbm_std[gbm_indices], align = "center")
plt.xticks(range(features_train.shape[1]), gbm_indices)
plt.xlim([-1, features_train.shape[1]])
plt.show()

#######################################################################################################
########################################### EXERCISE 3 FEATURE IMPORTANCE ############################
#######################################################################################################
## NOTE: feel free to copy code from above as a starting point

# 1) Print out the ranked features of the grid tree boosting model based on feature importance.

# 2) Plot its feature importance  

#######################################################################################################
########################################### END EXERCISE 3 ############################################
#######################################################################################################
