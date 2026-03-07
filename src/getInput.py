
import pandas as pd

def getInput() -> tuple[int, int]:
    while True:
        try:
            userInput = input("Enter a date (YYYY-MM-DD) - Cannot be February 29: ")
            inputDate = pd.to_datetime(userInput, format="%Y-%m-%d")

            # reject Feb 29
            if inputDate.month == 2 and inputDate.day == 29:
                print("February 29 is not allowed.")
                continue

            yearInput = inputDate.year
            doyInput = inputDate.dayofyear

            print(f"The year for {userInput} is: {yearInput}")
            print(f"The day of year for {userInput} is: {doyInput}")

            return yearInput, doyInput

        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")






