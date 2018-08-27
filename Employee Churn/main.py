import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# Exploratory Analysis
"""
Exploratory Data Analysis is an initial process of analysis,
in which you can summarize characteristics of data such as pattern, trends, outliers,
and hypothesis testing using descriptive statistics and visualization.
"""

data = pd.read_csv('HR_comma_sep.csv')

data.head()

