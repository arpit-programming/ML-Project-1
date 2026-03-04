from src.processData import loadCleanData, meanAndMedianDF
from src.plot1971 import plot1971
from src.meanAndMedian import plotMeanAndMedian 
from src.naivePrediction import getUserInputNaive


def main():
    
    # Get DataFrames
    df = loadCleanData("data/berlin_daily_weather.csv") # Load and clean the dataset, returning a DataFrame with 'DATE' and 'TMAX' columns
    agg = meanAndMedianDF(df) # Process the DataFrame to add date-related columns and calculate mean and median temperatures for each day of the year, returning a new DataFrame with 'doy', 'mean', and 'median' columns

    # Plotting 1971 data
    plot1971(df)

    # Plotting mean and median
    plotMeanAndMedian(agg)

    # Get user input as a day of year for Naive Prediction
    userInputNaive = getUserInputNaive(agg) # Prompt the user to enter a date in DD-MM format, convert it to day of year, and return the day of year as an integer

if __name__ == "__main__":
    main()


