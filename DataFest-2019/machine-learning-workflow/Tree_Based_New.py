#######################################################################################################
##################################################### SETUP ###########################################
#######################################################################################################

# Download data -- two csv files
	# fraud.csv for demonstration
	# flower.csv for exercises
# Place data on desktop
# Install all necessary packages 

#######################################################################################################
##################################################### END SETUP #######################################
#######################################################################################################

import sklearn
print(sklearn.__version__)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt


# Read in datafile
data = pd.read_csv('D:\\DataFest_Datasets\\fraud.csv')
#pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 100)
print(data.head(5))

print(data.isFraud.value_counts())

x_data = data.loc[:, (data.columns != 'isFraud')]
y_data = data.loc[:, (data.columns == 'isFraud')]

x_data_train, x_data_test, y_data_train, y_data_test = train_test_split(x_data, y_data, test_size = 0.3, random_state = 0)

print("y_data_test shape before: {}".format(y_data_test.shape))
c, r = y_data_test.shape
y_data_test = y_data_test.values.reshape(c,)
print("y_data_test shape after: {}".format(y_data_test.shape))

print("y_data_train shape before: {}".format(y_data_train.shape))
cc, rr = y_data_train.shape
y_data_train = y_data_train.values.reshape(cc,)
print("y_data_train shape after: {}".format(y_data_train.shape))

print("The default tree -- no thresholds")
dt_default = DecisionTreeClassifier(random_state = 123)
dt_default.fit(x_data_train, y_data_train)
y_test_predict = dt_default.predict(x_data_test)
recall_default = recall_score(y_data_test, y_test_predict, average='micro')
print("default tree recall:: {:.8f}".format(recall_default, end = "\n\n"))


print("Grid Parameter Search via 10-fold cross-validation")
param_grid = {"criterion": ["gini", "entropy"],
              "max_depth": [10, 15, 20, 25],
              "min_samples_split": [10, 20, 30],
              "min_samples_leaf": [5, 10, 15]}

dt = DecisionTreeClassifier(random_state = 123)
grid_search = GridSearchCV(dt, param_grid = param_grid, cv = 10, scoring = "recall")
grid_search.fit(x_data_train, y_data_train)
dt_grid = grid_search.best_params_

print("\nBest Parameters based on Recall:")
for k, v in dt_grid.items():
    print("parameter: {} setting: {}".format(k, v))

dt_grid_score = grid_search.best_score_
print("Mean recall score of the best parameters: {:.8f}\n\n".format(dt_grid_score))

print("\n\nTesting best parameters [Grid] based on Recall...")
dt_grid_best = DecisionTreeClassifier(random_state = 123, **dt_grid)
dt_grid_best.fit(x_data_train, y_data_train)
y_test_grid_predict = dt_grid_best.predict(x_data_test)
recall_grid = recall_score(y_data_test, y_test_grid_predict)
print("Grid search tree Recall:: {:.8f}\n\n".format(recall_grid))

#######################################################################################################
########################################### EXERCISE 1 CART: ##########################################
#######################################################################################################
# NOTE: feel free to copy code from above as a starting point

# 1) Explore the dataset: a. print out the first 10 records;
#                         b. print out the class distribution.

# 2) Preprocess the dataset: a. separate feature columns from the class label column;
#							 b. separate data into a training and testing sets at ratio 8:2.

# 3) Build a DEFAULT CART model and report its accuracy performance.

# 4) Use grid search method with 5-fold cross-validation to find the best tree parameter setting and corresponding mean accuracy.
 
# 5) Report accuracy performance of the optimal tree. Compare this performance with that of the default tree.

# 6) (Optional) Report feature importance of the optimal tree.

#######################################################################################################
########################################### END EXERCISE 1 ############################################
#######################################################################################################

## Extend with Random Forest Classifier
## Random Forest Default
rf_default = RandomForestClassifier(random_state = 123)
rf_default.fit(x_data_train, y_data_train)
y_test_rf_default_predict = rf_default.predict(x_data_test)
recall_rf_default = recall_score(y_data_test, y_test_rf_default_predict, average='micro')
print("Random Forest default recall:: {:.8f}".format(recall_rf_default, end = "\n\n"))

## Random Forest Grid
# Run an example
rf_example = RandomForestClassifier(random_state = 123, oob_score = True, n_estimators = 50, max_features = "log2", **dt_grid)
scores = cross_val_score(rf_example, x_data_train, y_data_train, cv = 10, scoring = "recall")
print("Example -- Recall at numTrees = 50, max_features = log2:: mean: {:.8f} (std: {:.8f})\n\n".format(scores.mean(), scores.std()))

# With loop
numTrees = [100, 150, 200, 250]
max_features = [None, "log2", "sqrt"]
max_score = 0
for i in numTrees:
    for j in max_features:
        rf = RandomForestClassifier(random_state = 123, oob_score = True, n_estimators = i, max_features = j, **dt_grid)
        scores = cross_val_score(rf, x_data_train, y_data_train, cv = 10, scoring = "recall")
        print("Recall at numTrees = {}, max_features = {}:: mean: {:.8f} (std: {:.8f})\n\n".format(i, j, scores.mean(), scores.std()))
        if scores.mean() > max_score:
            max_score = scores.mean()
            max_numTrees = i    
            max_numFeatures = j
print("best number of trees: {}; max number of fearures: {}".format(max_numTrees, max_numFeatures))

print("\n\nTesting Random Forest Grid based on Recall...")
rf_grid_best = RandomForestClassifier(random_state = 123, oob_score = True, n_estimators = max_numTrees, max_features = max_numFeatures, **dt_grid)
rf_grid_best.fit(x_data_train, y_data_train)
y_test_rf_predict = rf_grid_best.predict(x_data_test)
recall_rf = recall_score(y_data_test, y_test_rf_predict)
print("Random Forest Grid Recall:: {:.8f}".format(recall_rf, end = "\n\n"))


## Extend with GBM
## GBM Default
gbm_default = GradientBoostingClassifier(random_state = 123)
gbm_default.fit(x_data_train, y_data_train)
y_test_gbm_default_predict = gbm_default.predict(x_data_test)
recall_gbm_default = recall_score(y_data_test, y_test_gbm_default_predict, average='micro')
print("GBM default recall:: {:.8f}".format(recall_gbm_default, end = "\n\n"))


del dt_grid["criterion"]
## Show an example
gbm_example = GradientBoostingClassifier(random_state = 123, learning_rate = 0.2, n_estimators = 70, subsample = 0.8, **dt_grid)
scores = cross_val_score(gbm_example, x_data_train, y_data_train, cv = 10, scoring = "recall")
print("Example -- when learning_rate = 0.2, recall at numTrees = 70 and at subsample = 0.8:: mean: {:.8f} (std: {:.8f})\n\n".format(scores.mean(), scores.std()))

## Tune number of trees
numTrees = [20, 30, 40, 50, 60, 70, 80, 90, 100]
max_score_numTrees = 0
for i in numTrees:
    gbm1 = GradientBoostingClassifier(random_state = 123, learning_rate = 0.2, n_estimators = i, subsample = 0.8, **dt_grid)
    scores = cross_val_score(gbm1, x_data_train, y_data_train, cv = 10, scoring = "recall")
    print("when learning_rate = 0.2, recall at numTrees = {}:: mean: {:.8f} (std: {:.8f})\n\n".format(i, scores.mean(), scores.std()))
    if scores.mean() > max_score_numTrees:
            max_score_numTrees = scores.mean()
            max_numTrees = i   
print("GBM Grid:: best number of trees: {}".format(max_numTrees))

## Tune subsample size
subsample = [0.6, 0.7, 0.75, 0.8, 0.85, 0.9]
max_score_subsample = 0
for j in subsample:
    gbm2 = GradientBoostingClassifier(random_state = 123, learning_rate = 0.2, n_estimators = max_numTrees, subsample = j, **dt_grid)
    scores = cross_val_score(gbm2, x_data_train, y_data_train, cv = 10, scoring = "recall")
    print("when learning_rate = 0.2, tree number = {}, recall at subsample = {}:: mean: {:.8f} (std: {:.8f})\n\n".format(max_numTrees, j, scores.mean(), scores.std()))
    if scores.mean() > max_score_subsample:
            max_score_subsample = scores.mean()
            max_subsample = j    
print("GBM Grid:: best subsample size: {}".format(max_subsample))

## Tune learning_rate
learning_rate = [0.1, 0.05, 0.01]
max_score_learning_rate = 0
for r in learning_rate:
	gbm3 = GradientBoostingClassifier(random_state = 123, learning_rate = r, n_estimators = int(0.2/r) * max_numTrees, subsample = max_subsample, **dt_grid)
	scores = cross_val_score(gbm3, x_data_train, y_data_train, cv = 10, scoring = "recall")
	print("when learning rate = {}, number of trees = {}, recall:: mean: {:.8f} (std: {:.8f})\n\n".format(r, int(0.2/r) * max_numTrees, scores.mean(), scores.std()))
	if scores.mean() > max_score_learning_rate:
		max_score_learning_rate = scores.mean()
		max_learning_rate = r
		max_number_trees = int(0.2/r) * max_numTrees
print("GBM Grid:: best pair of learning rate and number of trees: {} and {}\n\n".format(max_learning_rate, max_number_trees))

print("\n\nTesting GBM Grid based on Recall...")
gbm_grid_best = GradientBoostingClassifier(random_state = 123, learning_rate = max_learning_rate, n_estimators = max_number_trees, subsample = max_subsample, **dt_grid)
gbm_grid_best.fit(x_data_train, y_data_train)
y_test_gbm_predict = gbm_grid_best.predict(x_data_test)
recall_gbm = recall_score(y_data_test, y_test_gbm_predict)
print("GBM Grid Recall:: {:.8f}".format(recall_gbm, end = "\n\n"))

#######################################################################################################
########################################### EXERCISE 2 TREE BOOSTING ##################################
#######################################################################################################
## NOTE: feel free to copy code from above as a starting point

# 1) For a given learning rate at 0.1, tune two boosting parameters--number of trees and size of sample--together to report their best 
#    combination and corresponding average accuracy.

# 2) Given the best combination of number of trees and size of samples from 1), tune boosting parameter learning rate to report its optimal
#    setting.

# 3) Report accuracy performance of the optimal tree boosting model. Compare this performance with that of the grid random forest model.

# 4) (Optional) Report feature importance of the optimal tree boosting model.

#######################################################################################################
########################################### END EXERCISE 2 ############################################
#######################################################################################################

dt_grid_importances = dt_grid_best.feature_importances_
print(dt_grid_importances)
dt_grid_indices = np.argsort(dt_grid_importances)[:: -1]
print(dt_grid_indices)
print("Feature ranking::Grid Single Tree:")

for f in range(x_data_train.shape[1]):
    print("%d. feature %d [%s] importance (%f)" % (f + 1, dt_grid_indices[f], x_data_train.columns.tolist()[dt_grid_indices[f]], dt_grid_importances[dt_grid_indices[f]]))

plt.figure()
plt.title("Feature importances::Grid Single Tree" )
plt.bar(range(x_data_train.shape[1]), dt_grid_importances[dt_grid_indices], color = "r", align = "center")
plt.xticks(range(x_data_train.shape[1]), dt_grid_indices)
plt.xlim([-1, x_data_train.shape[1]])
plt.show()


rf_importances = rf_grid_best.feature_importances_
rf_std = np.std([tree.feature_importances_ for tree in rf_grid_best.estimators_], axis = 0)
print(rf_std)
rf_indices = np.argsort(rf_importances)[:: -1]
print("Feature ranking: Random Forest Grid")

for f in range(x_data_train.shape[1]):
    print("%d. feature %d [%s] importance (%f)" % (f + 1, rf_indices[f], x_data_train.columns.tolist()[rf_indices[f]], rf_importances[rf_indices[f]]))

plt.figure()
plt.title("Feature importances: Random Forest Grid" )
plt.bar(range(x_data_train.shape[1]), rf_importances[rf_indices], color = "r", yerr = rf_std[rf_indices], align = "center")
plt.xticks(range(x_data_train.shape[1]), rf_indices)
plt.xlim([-1, x_data_train.shape[1]])
plt.show()


gbm_flatList = [item for sublist in gbm_grid_best.estimators_.tolist() for item in sublist]
gbm_importances = gbm_grid_best.feature_importances_
gbm_std = np.std([tree.feature_importances_ for tree in gbm_flatList], axis = 0)
gbm_indices = np.argsort(gbm_importances)[:: -1]
print("Feature ranking: GBM Grid")

for f in range(x_data_train.shape[1]):
    print("%d. feature %d [%s] importance (%f)" % (f + 1, gbm_indices[f], x_data_train.columns.tolist()[gbm_indices[f]], gbm_importances[gbm_indices[f]]))

plt.figure()
plt.title("Feature importances: GBM Grid" )
plt.bar(range(x_data_train.shape[1]), gbm_importances[gbm_indices], color = "r", yerr = gbm_std[gbm_indices], align = "center")
plt.xticks(range(x_data_train.shape[1]), gbm_indices)
plt.xlim([-1, x_data_train.shape[1]])
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
