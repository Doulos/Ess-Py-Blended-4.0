#!/usr/bin/env python
# coding: utf-8

"""
First, generate some example data to work with by loading a well-known
dataset from the web (The California Housing Dataset).
"""
import pandas as pd
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)


"""
Plot a scatter plot map of the California housing, which offers great visual
way to show that the location data fits within the outline shape of California, clearly shows the coastline:
"""
import matplotlib.pyplot as plt

df.plot.scatter(x="Longitude", y="Latitude")
plt.show()

"""
For the sake of the exercise, let force some of the values to be undefined:
"""
print("Exporting to excel...")
df.loc[1000:4000, "Latitude"] = None
df.loc[3000:6000, "Longitude"] = None
df.to_excel("dataset.xlsx", "Sheet1")


"""
Read in the contents of the Excel spreadsheet `dataset.xlsx` generated above.
Read the spreadsheet into a Pandas dataframe.
"""
print("Reading from excel...")
df = pd.read_excel("dataset.xlsx", "Sheet1", index_col=0)


"""
Call Pandas methods such as `head`, `info`, `describe`, and `plot.hist` to
learn what you can about the distribution of the data in the dataframe and
whether there are any missing values.
"""
print("df.head=\n", df.head())
df.info()
df.describe()


df[["MedInc", "HouseAge", "AveBedrms", "Latitude"]].plot.hist(
    alpha=0.5, bins=100, figsize=(10, 5)
)
plt.show()

"""
If there are missing values in any columns of the dataframe, fill the missing
values with the mean average value of the particular column in which they
occur.
"""
df = df.fillna(
    {"Latitude": df["Latitude"].mean(), "Longitude": df["Longitude"].mean()}
)

"""
Confirm that each column now contains exactly the same number of non-null
values (you could use `info` or `describe`)
"""
print("\n*** Check dataframe after fillna")
df.info()


"""
Add a new column named `'Size'` to the dataframe with values dependent on the
values of the RM column (the number of rooms in a house). Set the value in
the new column to 'Small' if RM is less than 6.0, to 'Large' if RM is greater
than 6.5, and otherwise to 'Medium'.
"""

import numpy as np

df["Size"] = np.where(
    df["AveRooms"] < 5.0,
    "Small",
    np.where(df["AveRooms"] > 6.0, "Large", "Medium"),
)


"""
Use the `info` method to confirm the existence and data type of the new
column.
"""
print("\n*** check dataframe after adding the 'Size' column")
df.info()


"""
Use the `groupby` method of the dataframe to show the count and the mean
values of the other columns for each of the three categories 'Small',
'Medium', and 'Large' of the 'Size' column.
"""
print("\n*** groupby category")
df.groupby("Size").agg(["count", "mean"])


"""
Create a new Pandas dataframe with three rows and two columns where the
columns are named 'Size' and 'Code'. The three sizes 'Small', 'Medium',
'Large' should correspond to the three codes 1, 2, 3.
"""
size_to_code = pd.DataFrame(
    {"Size": ["Small", "Medium", "Large"], "Code": [1, 2, 3]}
)
print("size_to_code=", size_to_code)


"""
Use the `merge` function to merge the house prices dataset including the 'Size'
column with the dataframe that maps 'Size' to 'Code'. Confirm that the merged
dataset contains 10 columns, including both 'Size' and 'Code'
"""
print("\n*** merging house prices dataset")
pd.merge(df, size_to_code, left_on="Size", right_on="Size")
df.info()

"""
Scale the values of specific columns by first subtracting the mean of the
column from all the values in that particular column, then dividing the values
in that column by the standard deviation of the values in that column
(you could use `apply`, `mean`, and `std`). Also drop a column.
"""
df2 = df.copy()
df2[["Population", "AveOccup"]] = df2[["Population", "AveOccup"]].apply(
    lambda x: x - x.mean()
)
df2[["Population", "AveOccup"]] = df2[["Population", "AveOccup"]].apply(
    lambda x: x / x.std()
)
df2 = df2.drop(columns=["Longitude"])


"""
Confirm that the scaling worked as expected. Each of these two columns
should now have mean = 0.0 and standard deviation = 1.0
(you could use `describe` or `plot.hist`)
"""
print("\n*** Verify scaling on df2")
df.info()
print(df2[["Population", "AveOccup"]].describe())
df2.plot.hist(alpha=0.5, bins=50, figsize=(10, 5))
plt.show()
