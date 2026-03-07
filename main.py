""" This is the main file that will run the entire project. Ideas of Object-Oriented Programming (OOP) have been used to structure the code in a modular way.
    It will call the functions from other files toward a comprehensive final project
    The order of execution is as follows:
    1. Load and clean the dataset using loadCleanData() from processData.py
    2. Process the dataset to calculate mean and median temperatures for each day of the year using meanAndMedianDF() from processData.py
    3. Plot the daily maximum temperature for Berlin in 1971 using plot1971() from plot1971.py
    4. Plot the mean and median daily maximum temperature for each day of the year using plotMeanAndMedian() from meanAndMedian.py
    5. Get user input for a date and provide a naive prediction based on the mean temperature for that day of the year using getUserInputNaive() from naivePrediction.py
    6. Future steps (currently IP) include implementing a more sophisticated machine learning model for temperature prediction, allowing the user to input a full date (including year) for more personalized predictions, and adding error handling for invalid inputs.
    
    NOTE: This project ignores leap years as assumes a constant 365 day cycle."""



# 1. Import necessary libraries and functions from other files
from src.processData import loadCleanData, meanAndMedianDF
from src.plot1971 import plot1971
from src.meanAndMedian import plotMeanAndMedian
from src.getInput import getInput 
from src.naivePrediction import naivePrediction
from src.ML import splitTrainAndTest, calculateSeasonality, addResiduals, residualRegression, predictTemperature, evaluate


# 2. Main function that executes the project in its entirety
def main():
    
    # 2.1 Load and clean datasets and calculate mean and median temperatures for each day of the year
    df = loadCleanData("data/berlin_daily_weather.csv") 
    dailyDF,agg = meanAndMedianDF(df) 
    
    # 2.2 Initial Plotting, 1971 and mean/median
    plot1971(df)
    plotMeanAndMedian(agg)

    # 2.3 Get User Input
    yearInput, doyInput = getInput()

    # 2.4 Prediction (Naive) -> Return the mean temperature for the input day of year (doy)
    naive = naivePrediction(agg, doyInput) 

    # 2.5 Machine Learning Setup 
    train, test = splitTrainAndTest(dailyDF) # Split the dataset into training and testing sets based on a specified split year (default is 2010), returning two DataFrames for training and testing
    seasonality = calculateSeasonality(train) # Calculate the mean temperature for each day of the year (seasonality) using the training set, returning a Series with 'doy' as the index and mean temperatures as values
    dfResiduals = addResiduals(train, seasonality) # Calculate the residuals for each day in the training set by subtracting the seasonal mean from the actual temperatures, returning a new DataFrame with additional columns for 'seasonalMean' and 'residual'
    model = residualRegression(dfResiduals) # Perform linear regression on the residuals to capture overall weather trends over the years, returning a fitted LinearRegression model

    # 2.6 Predictions using ML model
    predictedTemperature = predictTemperature(model, seasonality, yearInput, doyInput)

if __name__ == "__main__":
    main()


