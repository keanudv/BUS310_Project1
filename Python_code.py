'''
Name: Keanu Valencia
Date: 9/11/2024
Class: BUS 310 (Data Science/Decision Science)
'''

# Import the libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the data set into Python
file_location = "C:\\Users\\keanu\\OneDrive\\Desktop\\School\\BUS 310\\BUS 310 Project 1\\hotsheet.csv"
df = pd.read_csv(file_location, encoding="UTF-8")

# View the data
df.head(10)

# View the missing values
df.isnull().sum()

'''
The df.isnull().sum() function shows that there are 400 plus missing values in the Closing_Date and Sold_Price columns. This means some properties were not sold.
Since the focus of this analysis is on sold properties, we will drop those rows with missing values.
'''

# Drop the missing values
clean_df = df.dropna(subset=["Closing_Date", "Sold_Price"])

# Verify that the missing values were dropped
clean_df.isnull().sum()

# Select only the needed columns
columns = [
  "City",
  "Original_Price",
  "Days_On_Market",
  "Living_SQFT",
  "Status",
  "Land_SQFT",
  "Sold_Price"
]

# Creates the final dataframe used for analysis
final_df = clean_df[columns]

# Filter the City column to include only Wailuku (used for deep analysis)
wailuku_df = final_df[final_df["City"] == "Wailuku"]

# Creates a Scatter Plot with a trend line to identity outliers between Sold_Price and Living_SQFT in Wailuku
sns.regplot(data=wailuku_df, x="Living_SQFT", y="Sold_Price")
plt.title("Living Square Feet vs. Sold Price in Wailuku")
plt.xlabel("Living Square Feet")
plt.ylabel("Sold Price (In Millions)")
plt.show()

# Calculates the correlation coefficent to determine the strength of the relationship
correl = wailuku_df[["Living_SQFT", "Sold_Price"]].corr().loc["Living_SQFT", "Sold_Price"]
print(correl)

'''
There are a few outliers that we need to drop. To do this, we can use the Interquartile Range (IQR) method:
  Step 1: Calculate the IQR.
  Step 2: Define the boundaries.
  Step 3: Drop the outliers.
'''

# Step 1: Calculate the IQR for the sold price
Q1 = wailuku_df["Sold_Price"].quantile(0.25)
Q3 = wailuku_df["Sold_Price"].quantile(0.75)
IQR = Q3 - Q1

# Step 2: Define the outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Step 3: Drop the outliers
filtered_df = wailuku_df[(wailuku_df["Sold_Price"] >= lower_bound) & (wailuku_df["Sold_Price"] <= upper_bound)]

# Creates the same Scatter Plot without the outliars
sns.regplot(data=filtered_df, x="Living_SQFT", y="Sold_Price")
plt.title("Living Square Feet vs. Sold Price in Wailuku")
plt.xlabel("Living Square Feet")
plt.ylabel("Sold Price (In Millions)")
plt.show()

# Calculates the correlation coefficent to determine the strength of the relationship
correl = filtered_df[["Living_SQFT", "Sold_Price"]].corr().loc["Living_SQFT", "Sold_Price"]
print(correl)

# Creates a Histogram to show the spread of the sold prices in Wailuku
sns.histplot(data=filtered_df, x="Sold_Price", bins=10, kde=False)
plt.title("Distribution of Sold Prices in Wailuku")
plt.xlabel("Sold Price (In Millions)")
plt.ylabel("Frequency")
plt.show()
