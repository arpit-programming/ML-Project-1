import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def splitTrainAndTest(df: pd.DataFrame, splitYear: int = 2010):
    # Split the dataset into training and testing sets(80% training, 20% testing, with 2010 as the split
    print(f"Splitting the dataset into training and testing sets with {splitYear} as the split year...")
    train = df[df['year'] <= splitYear].copy() # Create the training set by filtering the DataFrame to include only rows where the year is less than or equal to the split year
    test = df[df['year'] > splitYear].copy() # Create the testing set by filtering the DataFrame to include only rows where the year is greater than the split year
    return train, test

def calculateSeasonality(train: pd.DataFrame) -> pd.Series:
    return train.groupby("doy")["TMAX"].mean() # Group the training set by 'doy' and calculate the mean of 'TMAX' for each group, returning a Series with 'doy' as the index and the mean temperatures as the values

def addResiduals(df: pd.DataFrame, seasonality: pd.Series) -> pd.DataFrame:
    dfResiduals = df.copy() # Create a copy of the input DataFrame to avoid modifying the original
    dfResiduals["seasonalMean"] = dfResiduals["doy"].map(seasonality) # Map the 'doy' values in the DataFrame to the corresponding mean temperatures from the seasonality Series and create a new column 'seasonalMean' to store these values
    dfResiduals["residual"] = dfResiduals["TMAX"] - dfResiduals["seasonalMean"] # Calculate the residuals by subtracting the 'seasonalMean' from the actual 'TMAX' values and create a new column 'residual' to store these values
    return dfResiduals

