# fitting a Regression Model to the Toyota Data
# reduce data frame to the top 1000 rows and select columns for regression analysis
car_df = pd.read_csv('ToyotaCorolla.csv')
car_df = car_df.iloc[0:1000]
predictors = ['Age_08_04', 'KM', 'Fuel_Type', 'HP', 'Met_Color', 'Automatic', 'CC', 'Doors', 'Quarterly_Tax', 'Weight']
outcome = 'Price'

# partition data
X = pd.get_dummies(car_df[predictors], drop_first = True)
Y = car_df[outcome]
train_X, valid_X, train_y, valid_y = train_test_split(X, y, test_size = 0.4, random_state = 1) # test_size = 0.4 -> put 40% in validation (test) partition

car_lm = LinearRegression()
car_lm.fit(train_X, train_y)

# output of the Regression Model
print(pd.DataFrame({'Predictor':X.columns, 'coefficient': car_lm.coef_})
      
# partial output
      
      '''predictor    coefficient
      0  Age_08_04    -140.748761
      1  KM           - 0.017840
      2  HP            36.103419
      3  Met_Color
      4  Automatic
      '''
      
## Accuracy Metrics for the Regression Model
# print performance measures (training data)
regressionSummary(train_y, car_lm.predict(train_X) # train data summary

# Regression statistics
'''Mean Error (ME): 0.0000
Root Mean Sqaured Error(RMSE): 1400.5823
Mean Absolute Error(MAE): 1046.9072
Mean Percentage Error (MPE): -1.0223
Mean Absolute Percentage Error (MAPE): 9.2994'''
                  
                  
# Make the Predictions for the Validation Data
# Use predict() to make predictions on a new set
car_lm_pred = car_lm.predict(valid_X)
                  result = pd.DataFrame({'Predicted': car_lm_pred,
                                         'Actual': valid_y, 
                                         'Residual': valid_y - car_lm_pred})
                  print(result.head())
                  
'''   Predicted       Actual      Residual
507   10607.333940    11500       892.666060
818   9272.705792      8950       -332.705792
452   10617.947808    11450       832.052192
'''
                  
regressionSummary(valid_y, car_lm_pred) # validation summary
                  
                  
# Ridge Regression in scikit-learn
ridge = Ridge(normalize = True, alpha=1)
ridge.fit(train_X, train_y)
regressionSummary(valid_y, ridge.predict(valid_X))
                  


            
                  
                  
              
  
  
  
  
