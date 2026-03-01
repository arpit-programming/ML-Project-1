#import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load and display the dataset head
print("Loading the dataset...")
df_whole = pd.read_csv("berlin_daily_weather.csv")
print("Dataset loaded successfully. Here are the first few rows:")
print(df_whole.head())

# Clean the dataset and display its head
print("Cleaning the dataset...")
df = df_whole[['DATE', 'TMAX']].copy() # Select only the 'DATE' and 'TMAX' columns for analysis
print("Dataset cleaned. Here are the first few rows of the cleaned dataset:")
print(df.head())


#------------------------------------------------------------------------------------------------------
#1. PLOTTING THE DATA FOR 1971

#1.1 Set up data for 1971
print("Filtering data for the year 1971...")
df_1971 = df[df['DATE'].str.startswith('1971')]
print("Data for 1971 filtered. Here are the first few rows:")
print(df_1971.head())

#1.2 Plot the data for 1971
print("Plotting the daily maximum temperature for Berlin in 1971...")

plt.figure(figsize=(14, 6)) # Size of the plot
plt.plot(df_1971['DATE'], df_1971['TMAX'], marker='o', linestyle='-', color='b') 
    # Date as x-axis(independent) and Temp as y-axis(dependent), "o":ppoints are marked as circles, "-" : points are connected by lines, "b": color blue
plt.title('Daily Maximum Temperature in Berlin (1971)') # Title of the plot
plt.xlabel('Date') # Label for x-axis
plt.ylabel('Maximum Temperature (°C)') # Label for y-axis
plt.xticks(rotation=45) # Rotate x-axis labels  45 degrees for better visibility
plt.tight_layout() # Adjust layout to prevent overlap
plt.show() # Display the plot

print("Plotting completed.")
#------------------------------------------------------------------------------------------------------

#2. FINDING MEAN AND MEDIAN FOR EACH DAY OF THE YEAR (1971-2020)

#2.1 Set up Dataset to include year, month, day, and day-of-year (doy)
df['DATE'] = pd.to_datetime(df['DATE']) # Convert 'DATE' column to datetime format
df["year"] = df["DATE"].dt.year # Extract year from 'DATE' and create a new column 'year'
df["month"] = df["DATE"].dt.month # Extract month from 'DATE' and create a new column 'month'
df["day"] = df["DATE"].dt.day # Extract day from 'DATE' and create a new column 'day'

#2.1.1 Remove February 29 to maintain a consistent 365-day cycle
is_feb29 = (df["month"] == 2) & (df["day"] == 29) # Identify rows corresponding to February 29
df = df.loc[~is_feb29].copy() # Remove rows corresponding to February 29

df["doy"] = df["DATE"].dt.dayofyear # Extract day of year from 'DATE' and create a new column 'doy'
print("Dataset prepared with additional date-related columns. Here are the first few rows:")
print(df.head())

#2.2 Calculate mean, median, and mode for each day of the year (doy)
agg = df.groupby("doy")["TMAX"].agg(["mean", "median"]).reset_index() # Group by 'doy' and calculate mean and median of 'TMAX' 
    # Group the data rows by day of year 
    # Calculate the mean and median of the maximum temperature for each day 
    # Reset the index to get a DataFrame
aggRounded = df.copy() # Create a copy of the original DataFrame
aggRounded["TMAX_round"] = aggRounded["TMAX"].round(1) # Round the 'TMAX' values to one decimal place and create a new column 'TMAX_round'
print("Created a new DataFrame with mean and median temperatures for each day of the year. Here are the first few rows:")
print(aggRounded.head())

#2.3 Plot the mean and median temperatures for each day of the year
print("Plotting the mean and median daily maximum temperature for each day of the year...")

plt.figure(figsize=(14, 6))
# Plot mean line
plt.plot(agg["doy"], agg["mean"], color='blue', label='Mean')
# Plot median line
plt.plot(agg["doy"], agg["median"], color='red', label='Median')
# Set title and labels
plt.title('Mean vs Median Daily Maximum Temperature by Day of Year (1971-2020)')
plt.xlabel('Day of Year (1=Jan 1, 365=Dec 31)')
plt.ylabel('Daily Maximum Temperature (°C)')
plt.legend()
# Adjust layout and display the plot
plt.tight_layout()
plt.show()

print("Plotting completed.")
#------------------------------------------------------------------------------------------------------




