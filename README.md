# chowtest
Package to test for structural breaks at a specified date using the Chow Test.

More details on the Chow Test are here: https://en.wikipedia.org/wiki/Chow_test

An example of its use is here: https://towardsdatascience.com/the-time-series-they-are-a-changing-why-all-good-models-eventually-fail-24a96a5f48d3

It contains 3 functions.

1. linear_residuals(X, y) which returns a dataframe containing the predicted y-values, the actual y-values, the residuals of the linear regression, and their squared residuals.

2. calculate_RSS(X, y) which returns the residual sum of squares from a linear regression

3. ChowTest(X, y, last_index_in_model_1, first_index_in_model_2) which returns the p-value from a Chow Test

Installation

Clone this repository, move into the directory, and install with pip:

git clone https://github.com/jkclem/chowtest.git
cd chowtest
pip install .

In your Python code you can import it as:

from chowtest import ChowTest

or 

import chowtest

to get all the functions.

Usage
The function has four parameters, and returns the a tuple of the Chow Statistic p-value of your Chow test.

Input	Requirements

X:	a pandas DataFrame of the independent variable(s) in order (first row is the earliest observation and the last row is the latest observation)
y:	a pandas DataFrame of the dependent variable in order (first row is the earliest observation and the last row is the latest observation)
last_index_in_model_1: the index value (for example '2000-01-01') of the last observation to include in the pre-break point model
first_index_in_model_2:	the index value (for example '2000-01-02') of the first observation to include in the post-break point model

Example

This repository has an example of the chowtest package being used.
