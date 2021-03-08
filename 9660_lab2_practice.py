#  predictors and outcome
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
predictors = ['US', 'Freq', 'last_update_days_ago', 'Web_order', 'Gender=male', 'Address_is_res']
outcome = 'Spending'
X = pd.get_dummies(tayko_df[predictors], drop_first = True)
y = tayko_df[outcome]

# partition data
train_X, valid_X, train_y, valid_y = train_test_split(X, y, test_size = 0.4, random_state = 1)
print('Training set:', train_X.shape, 'Validation set:', valid_X.shape)

# fit the regression model
tayko_lm = LinearRegression()
toyko_lm.fit(train_X, train_y)
print('Intercept', tayko_lm.intercept_)
print(pd.DataFrame({'Predictor': X.columns, 'coefficient': tayko_lm.coef_}))


'''Intercept 10.176297414610474
              Predictor  coefficient
0                    US    -4.620293
1                  Freq    91.274450
2  last_update_days_ago    -0.010374
3             Web_order    18.628731
4           Gender=male    -9.111366
5        Address_is_res   -75.815354'''

# The Regression equation: Spedning = Intercept + (coeff1*US) + (coeffn*Address_Is_res)

'''Coefficient explanation
1) A positive coefficient: as the value of the independent variable(x) increese, 
the mean of the dependent variable(y) also tends to increase.
2) A negative coefficeint: as the independent variable increases, the dependent variable tends to decrease.'''
