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
file_location = "location"
df = pd.read_csv(file_location, encoding="UTF-8")

# View the data
df.head(10)
