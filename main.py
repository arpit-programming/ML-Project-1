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
df = df_whole[['DATE', 'TMAX']]
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



