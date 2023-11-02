import sys
import pandas as pd
import numpy as np
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error

#submit base file name
file_input = sys.argv[1]

#SKLEARN Bayesian
log_regressor = BayesianRidge()
regressor = BayesianRidge()

#File Names from Base Name
train_suffix = '_train.csv'
validate_suffix = '_validate.csv'
test_suffix = '_test.csv'

#Read Data from File
df_train = pd.read_csv(file_input + train_suffix)
df_validate = pd.read_csv(file_input + validate_suffix)
df_test = pd.read_Csv(file_input + test_suffix)

#Get the Features X into one Matrix and extract what we're looking for
log_train_y, train_y, train_x = df_train.drop(columns=['Amount','log_Amount']), df_train['Amount'], df_train['log_Amount']

#Check with log transform Transform
log_regressor.fit(train_x, log_train_y)
#Check without log Transform
regressor.fit(train_x, train_y)

##TODO
# Use current model to adjust hyperparameter and test with the validation data.
# Look for methods to adjust hyperparameter
# Checkout 
# https://towardsdatascience.com/a-conceptual-explanation-of-bayesian-model-based-hyperparameter-optimization-for-machine-learning-b8172278050f
# https://machinelearningmastery.com/what-is-bayesian-optimization/
# https://scikit-learn.org/stable/modules/grid_search.html
# https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation
# https://scikit-learn.org/stable/modules/grid_search.html
# https://machinelearningmastery.com/scikit-optimize-for-hyperparameter-tuning-in-machine-learning/

#1 is shape paramemter and 2 is inverse scale parameter
grid = {
    'alpha_1': np.linspace(1e-8,1e-2,num=100),
    'alpha_2': np.linspace(1e-8,1e-2,num=100),
    'lambda_1': np.linspace(1e-8,1e-2,num=100),
    'lambda_2':np.linspace(1e-8,1e-2,num=100)
}
#use grid search cv

#Extract Data from the Validation data set to train the hyperparameter
log_validate_y, validate_y, validate_x = df_validate.drop(columns=['Amount','log_Amount']), df_validate['Amount'], df_validate['log_Amount']

#Possibly a loop here or some kind of method to go about training the data
log_y_predict = log_regressor.predict(validate_x)
y_predict = regressor.predict(validate_x)

#Figure out a good method of evaluation of the amount
#Checkout https://stats.stackexchange.com/questions/51046/how-to-check-if-my-regression-model-is-good
log_mse = mean_squared_error(validate_y, log_y_predict)
mse = mean_squared_error(validate_y, y_predict)


##TODO
#Use the new hyperparameter data for newly trained model
#Use the test data to retrieve points to evaluate
#Write data to csv to use for analysis later 
log_test_y, test_y, test_x = df_test.drop(columns=['Amount','log_Amount']), df_test['Amount'], df_test['log_Amount']
