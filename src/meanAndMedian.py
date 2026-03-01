import pandas as pd
import matplotlib.pyplot as plt

def plotMeanAndMedian(df: pd.DataFrame) -> None:
    # Plot the mean and median temperatures for each day of the year
    
    df = df.copy() # Create a copy of the DataFrame to avoid modifying the original

    print("Plotting the mean and median daily maximum temperature for each day of the year...")

    plt.figure(figsize=(14, 6))
    # Plot mean line
    plt.plot(df["doy"], df["mean"], color='blue', label='Mean')
    # Plot median line
    plt.plot(df["doy"], df["median"], color='red', label='Median')
    # Set title and labels
    plt.title('Mean vs Median Daily Maximum Temperature by Day of Year (1971-2020)')
    plt.xlabel('Day of Year (1=Jan 1, 365=Dec 31)')
    plt.ylabel('Daily Maximum Temperature (°C)')
    plt.legend()
    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()

    print("Plotting completed.")