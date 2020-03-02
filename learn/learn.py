import matplotlib
import numpy
import pandas
import scipy
import sys
# Load libraries
from pandas import read_csv

print('Python: {}'.format(sys.version))
print('scipy: {}'.format(scipy.__version__))
print('numpy: {}'.format(numpy.__version__))
print('matplotlib: {}'.format(matplotlib.__version__))
print('pandas: {}'.format(pandas.__version__))

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# Data Checks
# shape of the data set
print('Data Set Shape: ')
print(dataset.shape)

#First 20 rows of sample data set
print('First 20 Rows of Data Set')
print(dataset.head(20))

#Statisical Summary of Sample Data Set
print('Statistical Summary of Data Set')
print(dataset.describe())

#Class Distribution of Data Set
print('Class Distribution of Data Set')
print(dataset.groupby('class').size())

#Start 4.1 on https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
