import pandas as pd

def getUserInputNaive() -> int:
    userInput = input("Enter a date (DD-MM) - Cannot be February 29: ") # Prompt the user to enter a date in the format DD-MM
    try:
        input_date = pd.to_datetime(userInput, format="%d-%m") # Convert the user input to a datetime object using the specified format
        doy_input = input_date.dayofyear # Extract the day of year from the input date
        print(f"The day of year for {userInput} is: {doy_input}")
    except ValueError:
        print("Invalid date format. Please enter the date in DD-MM format.")
        exit()
    return doy_input