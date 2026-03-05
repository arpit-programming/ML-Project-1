""" This is the main file that will run the entire project. Ideas of Object-Oriented Programming (OOP) have been used to structure the code in a modular way.
    It will call the functions from other files toward a comprehensive final project
    The order of execution is as follows:
    1. Load and clean the dataset using loadCleanData() from processData.py
    2. Process the dataset to calculate mean and median temperatures for each day of the year using meanAndMedianDF() from processData.py
    3. Plot the daily maximum temperature for Berlin in 1971 using plot1971() from plot1971.py
    4. Plot the mean and median daily maximum temperature for each day of the year using plotMeanAndMedian() from meanAndMedian.py
    5. Get user input for a date and provide a naive prediction based on the mean temperature for that day of the year using getUserInputNaive() from naivePrediction.py
    6. Future steps (currently IP) include implementing a more sophisticated machine learning model for temperature prediction, allowing the user to input a full date (including year) for more personalized predictions, and adding error handling for invalid inputs."""



# 1. Import necessary libraries and functions from other files
from src.processData import loadCleanData, meanAndMedianDF
from src.plot1971 import plot1971
from src.meanAndMedian import plotMeanAndMedian 
from src.naivePrediction import naivePrediction


# 2. Main function that executes the project in its entirety
def main():
    
    # 2.1 Dataframes
    df = loadCleanData("data/berlin_daily_weather.csv") # Load and clean the dataset, returning a DataFrame with 'DATE' and 'TMAX' columns
    agg = meanAndMedianDF(df) # Process the DataFrame to add date-related columns and calculate mean and median temperatures for each day of the year, returning a new DataFrame with 'doy', 'mean', and 'median' columns

    # 2.2 Initial Plotting
    plot1971(df)
    plotMeanAndMedian(agg)

    # 2.3 Prediction (Naive)
    naiv = naivePrediction(agg) # Prompt the user to enter a date in DD-MM format, convert it to day of year, and return the day of year as an integer

    # 2.4 Machine Learning Prediction (IP)

if __name__ == "__main__":
    main()


