import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import StratifiedShuffleSplit

# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Use only one feature
diabetes_X = diabetes_X[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

sss = StratifiedShuffleSplit(n_splits=5)
regr = linear_model.LinearRegression()
scores = []

print(diabetes_y)


"""for train_index, test_index in sss.split(diabetes_X, diabetes_y):
    print('train index', train_index)
    print(test_index)

    X_train, X_test = diabetes_X[train_index], diabetes_X[test_index] 
    y_train, y_test = diabetes_y[train_index], diabetes_y[test_index] 
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X_test)
    scores.append(accuracy_score(y_test, y_pred))
print(scores)"""

# Split the targets into training/testing sets
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)
print(diabetes_y_pred)

# The coefficients
print("Coefficients: \n", regr.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs

print('X-test', len(diabetes_X_test), diabetes_X_test)

print('y_test', len(diabetes_y_test), diabetes_y_test)
print('y_predictions', len(diabetes_y_pred), diabetes_y_pred)

plt.scatter(diabetes_y_test, diabetes_y_pred, color="black")
plt.plot(diabetes_X_test, diabetes_y_test, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())


plt.show()
