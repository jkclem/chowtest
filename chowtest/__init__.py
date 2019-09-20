# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 12:02:06 2019

@author: jkcle
"""

# defines a function to get performance information about a linear regression using sklearn
def linear_fit_and_residuals(X, y):
    
    # imports pandas as pd
    import pandas as pd
    # imports numpy as np
    import numpy as np
    
    # imports the linear regression function from sklearn as lr
    from sklearn.linear_model import LinearRegression as lr
    
    # fits the linear model
    model = lr().fit(X, y)
    
    # creates a dataframe with the predicted y in a column called y_hat
    summary_result = pd.DataFrame(columns = ['y_hat'])
    yhat_list = [float(i[0]) for i in np.ndarray.tolist(model.predict(X))]
    summary_result['y_hat'] = yhat_list  
    # saves the actual y values in the y_actual column
    summary_result['y_actual'] = y.values
    # calculates the residuals
    summary_result['residuals'] = summary_result.y_actual - summary_result.y_hat
    # squares the residuals
    summary_result['residuals_sq'] = summary_result.residuals ** 2
    
    return(summary_result)



# defines a function to return the sum of squares of a linear regression, where X is a 
# pandas dataframe of the independent variables and y is a pandas dataframe of the dependent
# variable
def calculate_RSS(X, y):
    
    # calls the residual_data function
    resid_data = linear_fit_and_residuals(X, y)
    # calculates the sum of squared resiudals
    rss = resid_data.residuals_sq.sum()
    
    # returns the sum of squared residuals
    return(rss)



# defines a function to return the p-value from a Chow Test
def Chow_Test(X, y, last_index_in_model_1, first_index_in_model_2):
    
    # gets the RSS for the entire period
    rss_pooled = calculate_RSS(X, y)
    
    # splits the X and y dataframes and gets the rows from the first row in the dataframe
    # to the last row in the model 1 testing period and then calculates the RSS
    X1 = X.loc[:last_index_in_model_1]
    y1 = y.loc[:last_index_in_model_1]
    rss1 = calculate_RSS(X1, y1)
    
    # splits the X and y dataframes and gets the rows from the first row in the model 2 
    # testing period to the last row in the dataframe and then calculates the RSS    
    X2 = X.loc[first_index_in_model_2:]
    y2 = y.loc[first_index_in_model_2:]
    rss2 = calculate_RSS(X2, y2)
    
    # gets the number of independent variables, plus 1 for the constant in the regression
    k = X.shape[1] + 1
    # gets the number of observations in the first period
    N1 = X1.shape[0]
    # gets the number of observations in the second period
    N2 = X2.shape[0]

    # calculates the numerator of the Chow Statistic
    numerator = (rss_pooled - (rss1 + rss2)) / k
    # calculates the denominator of the Chow Statistic
    denominator = (rss1 + rss2) / (N1 + N2 - 2 * k)
    
    # calculates the Chow Statistic
    Chow_Stat = numerator / denominator
    
    # Chow statistics are distributed in a F-distribution with k and N1 + N2 - 2k degrees of
    # freedom
    from scipy.stats import f
    
    # calculates the p-value by subtracting 1 by the cumulative probability at the Chow
    # statistic from an F-distribution with k and N1 + N2 - 2k degrees of freedom
    p_value = 1 - f.cdf(Chow_Stat, dfn = 5, dfd = (N1 + N2 - 2 * k))
    
    # returns the p-value
    return(p_value)
