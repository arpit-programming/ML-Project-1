

# 1. Import necessary libraries and functions from other files
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from datetime import datetime, timedelta

# 2. Split dataset into training and testing sets
def splitTrainAndTest(df: pd.DataFrame, splitYear: int = 2010):
    # 2.1 Split the dataset into training and testing sets(80% training, 20% testing, with 2010 as the split
    print(f"Splitting the dataset into training and testing sets with {splitYear} as the split year...")
    train = df[df['year'] <= splitYear].copy() # Create the training set by filtering the DataFrame to include only rows where the year is less than or equal to the split year
    test = df[df['year'] > splitYear].copy() # Create the testing set by filtering the DataFrame to include only rows where the year is greater than the split year
    print("Dataset split completed. Here are the first few rows of the training and testing sets, respectively:")
    print(train.head())
    print(test.head())
    return train, test

# 3. Calculating Seasonality (mean temperature for each day of the year))
def calculateSeasonality(train: pd.DataFrame) -> pd.Series:
    # 3.1 Group the training set by 'doy' and calculate the mean of 'TMAX' for each group, returning a Series with 'doy' as the index and the mean temperatures as the values
    return train.groupby("doy")["TMAX"].mean() 

# 4. Calculate the residuals for each day in each year (actual temperature - season mean) and add it as a new column to the DataFrame
def addResiduals(df: pd.DataFrame, seasonality: pd.Series) -> pd.DataFrame:
    dfResiduals = df.copy() # Create a copy of the input DataFrame to avoid modifying the original
    dfResiduals["seasonalMean"] = dfResiduals["doy"].map(seasonality) # Map the 'doy' values in the DataFrame to the corresponding mean temperatures from the seasonality Series and create a new column 'seasonalMean' to store these values
    dfResiduals["residual"] = dfResiduals["TMAX"] - dfResiduals["seasonalMean"] # Calculate the residuals by subtracting the 'seasonalMean' from the actual 'TMAX' values and create a new column 'residual' to store these values
    return dfResiduals

# 5. Perform linear regression on the residuals to capture overall weather trends over the years (e.g., due to climate change)
def residualRegression(dfResiduals: pd.DataFrame) -> LinearRegression:
    X = dfResiduals[["year"]]
    Y = dfResiduals["residual"]
    model = LinearRegression() # Create an instance of the LinearRegression model
    model.fit(X, Y) # Fit the model to the data by finding the best-fitting line
    return model

def predictTemperature(model: LinearRegression, seasonality: pd.Series, year: int, doy: int) -> float:
    seasonal = float(seasonality.loc[doy])
    residualValue = float(model.predict(pd.DataFrame({"year": [year]}))[0])
    prediction = seasonal + residualValue
    date = pd.to_datetime(f"{year}-{doy}", format = "%Y-%j")
    print(f" If current climate trends continue, the predicted temperature for {date.strftime('%Y-%m-%d')} is: {prediction:.2f} °C")


def evaluate(model: LinearRegression, seasonality: pd.Series, test: pd.DataFrame) -> dict:
    test2 = addResiduals(test, seasonality)
    # predict residual then reconstruct temperature prediction
    resid_hat = model.predict(test2[["year"]])
    y_hat = test2["seasonalMean"].to_numpy() + resid_hat
    y_true = test2["TMAX"].to_numpy()

    return {
        "r2": float(r2_score(y_true, y_hat)),
        "mae": float(mean_absolute_error(y_true, y_hat)),
        "rmse": float(np.sqrt(mean_squared_error(y_true, y_hat))),
    }
