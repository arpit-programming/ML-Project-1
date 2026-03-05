import pandas as pd

def naivePrediction(agg: pd.DataFrame) -> float:
    userInput = input("Enter a date (DD-MM) - Cannot be February 29: ") # Prompt the user to enter a date in the format DD-MM
    try:
        input_date = pd.to_datetime(userInput, format="%d-%m") # Convert the user input to a datetime object using the specified format
        doy_input = input_date.dayofyear # Extract the day of year from the input date
        print(f"The day of year for {userInput} is: {doy_input}")

        meanTemp = agg.loc[agg['doy'] == doy_input, 'mean'].values[0] # Retrieve the mean temperature for the specified day of year from the agg DataFrame
        print(f"The predicted temperature for {userInput} is {meanTemp:.2f} °C based on the Naive Prediction Method")
    except ValueError:
        print("Invalid date format. Please enter the date in DD-MM format.")
        exit()
    return meanTemp