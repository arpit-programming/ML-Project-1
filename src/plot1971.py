import pandas as pd
import matplotlib.pyplot as plt


def plot1971(df: pd.DataFrame) -> None:
    #Set up data for 1971
    print("Filtering data for the year 1971...")
    df['DATE'] = pd.to_datetime(df['DATE']) # Ensure 'DATE' column is in datetime format
    df_1971 = df[df['DATE'].dt.year == 1971].copy() # Filter the DataFrame to include only rows where the year is 1971
    print("Data for 1971 filtered. Here are the first few rows:")
    print(df_1971.head())

    #Plot the data for 1971
    print("Plotting the daily maximum temperature for Berlin in 1971...")

    plt.figure(figsize=(14, 6)) # Size of the plot
    plt.plot(df_1971['DATE'], df_1971['TMAX'], marker='o', linestyle='-', color='b')  # Date as x-axis(independent) and Temp as y-axis(dependent), "o":ppoints are marked as circles, "-" : points are connected by lines, "b": color blue
    plt.title('Daily Maximum Temperature in Berlin (1971)') # Title of the plot
    plt.xlabel('Date') # Label for x-axis
    plt.ylabel('Maximum Temperature (°C)') # Label for y-axis
    plt.xticks(rotation=45) # Rotate x-axis labels  45 degrees for better visibility
    plt.tight_layout() # Adjust layout to prevent overlap
    plt.show() # Display the plot
    print("Plotting completed.")


