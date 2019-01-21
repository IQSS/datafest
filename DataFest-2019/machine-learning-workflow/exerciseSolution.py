import sklearn
print(sklearn.__version__)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt

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

data = pd.read_csv('https://raw.githubusercontent.com/IQSS/datafest/master/DataFest-2019/machine-learning-workflow/flower.csv')
pd.set_option('display.max_columns', 100)
print(data.head(10))

print(data.Species.value_counts())

# 2) Preprocess the dataset: a. separate feature columns from the class label column;
#							 b. separate data into a training and testing sets at ratio 8:2;
#	                         c. reshape the class column into an 1d array for both training and testing sets.

features = data.loc[:, (data.columns != 'Species')]
classLabel = data.loc[:, (data.columns == 'Species')]

features_train, features_test, classLabel_train, classLabel_test = train_test_split(features, classLabel, test_size = 0.2, random_state = 0)

print("classLabel_test shape before: {}".format(classLabel_test.shape))
c, r = classLabel_test.shape
classLabel_test = classLabel_test.values.reshape(c,)
print("classLabel_test shape after: {}".format(classLabel_test.shape))

print("classLabel_train shape before: {}".format(classLabel_train.shape))
cc, rr = classLabel_train.shape
classLabel_train = classLabel_train.values.reshape(cc,)
print("classLabel_train shape after: {}".format(classLabel_train.shape))

# 3) Build a DEFAULT CART model and report its accuracy performance.

dt_default = DecisionTreeClassifier(random_state = 123)
dt_default.fit(features_train, classLabel_train)
classLabel_test_predict = dt_default.predict(features_test)
accuracy_default = accuracy_score(classLabel_test, classLabel_test_predict)
print("default tree accuracy:: {:.8f}".format(accuracy_default, end = "\n\n"))

# 4) Use grid search method with 5-fold cross-validation to find the best tree parameters and setting as well as corresponding
#    mean accuracy. You could choose parameters different from those used in demonstration.

param_grid = {"criterion": ["gini", "entropy"],
              "max_depth": [3, 5, 10, 15],
              "min_samples_split": [10, 15, 20],
              "min_samples_leaf": [5, 10, 15]}
dt = DecisionTreeClassifier(random_state = 123)
grid_search = GridSearchCV(dt, param_grid = param_grid, cv = 5, scoring = "accuracy")
grid_search.fit(features_train, classLabel_train)
dt_grid = grid_search.best_params_
for k, v in dt_grid.items():
    print("parameter: {} setting: {}".format(k, v))
dt_grid_score = grid_search.best_score_
print("Mean accuracy score of the best parameters: {:.8f}\n\n".format(dt_grid_score))
 
# 5) Report accuracy performance of the optimal tree. Compare this performance with that of the default tree.

dt_grid_best = DecisionTreeClassifier(random_state = 123, **dt_grid)
dt_grid_best.fit(features_train, classLabel_train)
classLabel_test_grid_predict = dt_grid_best.predict(features_test)
accuracy_grid = accuracy_score(classLabel_test, classLabel_test_grid_predict)
print("Grid search tree Accuracy:: {:.8f}\n\n".format(accuracy_grid))

# 6) (Optional) Report feature importance of the optimal tree.

dt_grid_importances = dt_grid_best.feature_importances_
print(dt_grid_importances)

#######################################################################################################
########################################### END EXERCISE 1 ############################################
#######################################################################################################

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

del dt_grid["criterion"]
numTrees = [50, 60, 70, 80]
subsample = [0.6, 0.7, 0.8, 0.9]
max_score_numTrees_sampleSize = 0
for i in numTrees:
	for j in subsample:
		gbm1 = GradientBoostingClassifier(random_state = 123, learning_rate = 0.1, n_estimators = i, subsample = j, **dt_grid)
		scores = cross_val_score(gbm1, features_train, classLabel_train, cv = 10, scoring = "accuracy")
		print("when learning_rate = 0.1, recall at numTrees = {} and subsample size = {}:: mean: {:.8f} (std: {:.8f})\n\n".format(i, j, scores.mean(), scores.std()))
		if scores.mean() > max_score_numTrees_sampleSize:
			max_score_numTrees_sampleSize = scores.mean()
			max_numTrees = i   
			max_subsample = j
print("GBM Grid:: best number of trees: {}; best subsample size: {}; maximum cross-validated mean accuracy: {:.8f}".format(max_numTrees, max_subsample, max_score_numTrees_sampleSize))

# 2) Given the best combination of number of trees and size of subsample from 1), tune boosting parameter learning rate to report its optimal
#    setting. Learning rate values could be [0.01, 0.05, 0.1, 0.2].

learning_rate = [0.01, 0.05, 0.1, 0.2]
max_score_learning_rate = 0
for r in learning_rate:
	gbm2 = GradientBoostingClassifier(random_state = 123, learning_rate = r, n_estimators = int(0.2/r) * max_numTrees, subsample = max_subsample, **dt_grid)
	scores = cross_val_score(gbm2, features_train, classLabel_train, cv = 10, scoring = "accuracy")
	print("when learning rate = {}, number of trees = {}, accuracy:: mean: {:.8f} (std: {:.8f})\n\n".format(r, int(0.2/r) * max_numTrees, scores.mean(), scores.std()))
	if scores.mean() > max_score_learning_rate:
		max_score_learning_rate = scores.mean()
		max_learning_rate = r
		max_number_trees = int(0.2/r) * max_numTrees
print("GBM Grid:: best pair of learning rate and number of trees: {} and {}, maximum cross-validated mean accuracy: {:.8f}\n\n".format(max_learning_rate, max_number_trees, max_score_learning_rate))

# 3) Report accuracy performance of the optimal tree boosting model. Compare this performance with that of the grid random forest model.

gbm_grid_best = GradientBoostingClassifier(random_state = 123, learning_rate = max_learning_rate, n_estimators = max_number_trees, subsample = max_subsample, **dt_grid)
gbm_grid_best.fit(features_train, classLabel_train)
classLabel_test_gbm_predict = gbm_grid_best.predict(features_test)
accuracy_gbm = accuracy_score(classLabel_test, classLabel_test_gbm_predict)
print("GBM Grid Accuracy:: {:.8f}".format(accuracy_gbm, end = "\n\n"))

# 4) (Optional) Report feature importance of the optimal tree boosting model.

gbm_importances = gbm_grid_best.feature_importances_
print(gbm_importances)

#######################################################################################################
########################################### END EXERCISE 2 ############################################
#######################################################################################################

#######################################################################################################
########################################### EXERCISE 3 FEATURE IMPORTANCE ############################
#######################################################################################################
## NOTE: feel free to copy code from above as a starting point

# 1) Print out the ranked features of the grid tree boosting model based on feature importance.

gbm_flatList = [item for sublist in gbm_grid_best.estimators_.tolist() for item in sublist]
gbm_importances = gbm_grid_best.feature_importances_
gbm_std = np.std([tree.feature_importances_ for tree in gbm_flatList], axis = 0)
gbm_indices = np.argsort(gbm_importances)[:: -1]
print("Feature ranking: GBM Grid")

for f in range(features_train.shape[1]):
    print("%d. feature %d [%s] importance (%f)" % (f + 1, gbm_indices[f], features_train.columns.tolist()[gbm_indices[f]], gbm_importances[gbm_indices[f]]))

# 2) Plot its feature importance  

plt.figure()
plt.title("Feature importances: GBM Grid" )
plt.bar(range(features_train.shape[1]), gbm_importances[gbm_indices], color = "r", yerr = gbm_std[gbm_indices], align = "center")
plt.xticks(range(features_train.shape[1]), gbm_indices)
plt.xlim([-1, features_train.shape[1]])
plt.show()

#######################################################################################################
########################################### END EXERCISE 3 ############################################
#######################################################################################################
