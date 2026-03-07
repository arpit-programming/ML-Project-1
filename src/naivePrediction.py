import pandas as pd

def naivePrediction(agg: pd.DataFrame, userInput: int) -> float:
    # Get the mean temperature for the input day of year (doy) from the agg DataFrame
    prediction = agg.loc[agg["doy"] == userInput, "mean"].values[0] # Filter the agg DataFrame to find the row where 'doy' matches the user input and extract the 'mean' value
    print(f"The predicted mean temperature for day of year {userInput} is: {prediction:.2f} °C") # Print the predicted mean temperature with 2 decimal places
    return prediction
    
