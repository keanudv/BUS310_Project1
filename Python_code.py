'''
Name: Keanu Valencia
Date: 9/11/2024
Class: BUS 310 (Data Science/Decision Science)
'''

# Import the libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data set into Python
file_location = "C:\\Users\\keanu\\OneDrive\\Desktop\\School\\BUS 310\\BUS 310 Project 1\\"
df = pd.read_csv(file_location, encoding="UTF-8")

# View the data
df.head(10)

# Creates a Histogram to show the spread of the data
sns.histplot(data=df, bins=30, kde=False)
plt.title("Title")
plt.xlabel("Bins of the Histogram")
plt.ylabel("Y Axis")
plt.show()

# Creates a Scatter Plot to show any outliers
sns.scatterplot(data=df, x="x", y="y")
plt.title("Title")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
