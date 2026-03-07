"""
This module contains functions to load and clean the dataset, as well as to calculate mean and median temperatures for each day of the year.
"""


# 1. Import necessary libraries
import pandas as pd

# 2. Load the CSV file and clean the dataset
def loadCleanData(csvPath: str) -> pd.DataFrame:
    # 2.1 Load and display the dataset head
    print("Loading the dataset...")
    df_whole = pd.read_csv(csvPath)
    print("Dataset loaded successfully. Here are the first few rows:")
    print(df_whole.head())

    # 2.2. Clean the dataset and display its head
    print("Cleaning the dataset...")
    df = df_whole[['DATE', 'TMAX']].copy() # Select only the 'DATE' and 'TMAX' columns for analysis, make a copy to avoid modifying the original DataFrame
    df['DATE'] = pd.to_datetime(df['DATE']) # Convert 'DATE' column to datetime format
    print("Dataset cleaned. Here are the first few rows of the cleaned dataset:")
    print(df.head())

    # 2.3 Return the cleaned DataFrame
    return df

# 3. Calculate mean and median, store it on a new dataframe
def meanAndMedianDF(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    # 3.1. Parse the 'Date' column to set up the Dataset to include year, month, day, and day-of-year (doy)
    df['DATE'] = pd.to_datetime(df['DATE']) # Convert 'DATE' column to datetime format
    
    # 3.1.1 Extract year, month, and day from 'DATE' and create new columns for each
    df["year"] = df["DATE"].dt.year 
    df["month"] = df["DATE"].dt.month
    df["day"] = df["DATE"].dt.day 

    # 3.2 Remove February 29 to maintain a consistent 365-day cycle
    is_feb29 = (df["month"] == 2) & (df["day"] == 29) # Identify rows corresponding to February 29
    df = df.loc[~is_feb29].copy() # Remove rows corresponding to February 29

    # 3.3. Extract day of year (doy) from 'DATE' and create a new column 'doy'
    df["doy"] = df["DATE"].dt.dayofyear
    
    # 3.4. Give system feedback to the user and display the head of the updated DataFrame
    print("Dataset prepared with additional date-related columns. Here are the first few rows:")
    print(df.head())

    # 3.5. Calculate mean, median, and mode for each day of the year (doy)
    agg = df.groupby("doy")["TMAX"].agg(["mean", "median"]).reset_index() # Group by 'doy' and calculate mean and median of 'TMAX' 
    print("Created a new DataFrame with mean and median temperatures for each day of the year. Here are the first few rows:")
    print(agg.head())
    
    # 3.6 Return the new DataFrame containing 'doy', 'mean', and 'median' columns 
    return df, agg