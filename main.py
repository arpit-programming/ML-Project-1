#import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df_whole = pd.read_csv("berlin_daily_weather.csv")

# Display the first few rows of the dataset
print(df_whole.head())

# Filter to keep only DATE and TMAX columns
df = df_whole[['DATE', 'TMAX']]

#display the first few rows of the filtered dataset
print(df.head())


#------------------------------------------------------------------------------------------------------
#1. PLOTTING THE DATA FOR 1971

#1.1 Filter the data for the year 1971
df_1971 = df[df['DATE'].str.startswith('1971')]

#1.2 Plot the data for 1971
plt.figure(figsize=(14, 6)) # Size of the plot
plt.plot(df_1971['DATE'], df_1971['TMAX'], marker='o', linestyle='-', color='b') 
    # Date as x-axis(independent) and Temp as y-axis(dependent), "o":ppoints are marked as circles, "-" : points are connected by lines, "b": color blue
plt.title('Daily Maximum Temperature in Berlin (1971)') # Title of the plot
plt.xlabel('Date') # Label for x-axis
plt.ylabel('Maximum Temperature (°C)') # Label for y-axis
plt.xticks(rotation=45) # Rotate x-axis labels  45 degrees for better visibility
plt.tight_layout() # Adjust layout to prevent overlap
plt.show() # Display the plot

#------------------------------------------------------------------------------------------------------



