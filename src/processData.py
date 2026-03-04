import pandas as pd


# Load the CSV file and clean the dataset
def loadCleanData(csvPath: str) -> pd.DataFrame:
    # Load and display the dataset head
    print("Loading the dataset...")
    df_whole = pd.read_csv(csvPath)
    print("Dataset loaded successfully. Here are the first few rows:")
    print(df_whole.head())

    # Clean the dataset and display its head
    print("Cleaning the dataset...")
    df = df_whole[['DATE', 'TMAX']].copy() # Select only the 'DATE' and 'TMAX' columns for analysis
    df['DATE'] = pd.to_datetime(df['DATE']) # Convert 'DATE' column to datetime format
    print("Dataset cleaned. Here are the first few rows of the cleaned dataset:")
    print(df.head())

    return df

#Calculate mean and median, store it on a new dataframe
def meanAndMedianDF(df: pd.DataFrame) -> pd.DataFrame:
    # Set up Dataset to include year, month, day, and day-of-year (doy)
    df['DATE'] = pd.to_datetime(df['DATE']) # Convert 'DATE' column to datetime format
    df["year"] = df["DATE"].dt.year # Extract year from 'DATE' and create a new column 'year'
    df["month"] = df["DATE"].dt.month # Extract month from 'DATE' and create a new column 'month'
    df["day"] = df["DATE"].dt.day # Extract day from 'DATE' and create a new column 'day'

    # Remove February 29 to maintain a consistent 365-day cycle
    is_feb29 = (df["month"] == 2) & (df["day"] == 29) # Identify rows corresponding to February 29
    df = df.loc[~is_feb29].copy() # Remove rows corresponding to February 29

    df["doy"] = df["DATE"].dt.dayofyear # Extract day of year from 'DATE' and create a new column 'doy'
    print("Dataset prepared with additional date-related columns. Here are the first few rows:")
    print(df.head())

    # Calculate mean, median, and mode for each day of the year (doy)
    agg = df.groupby("doy")["TMAX"].agg(["mean", "median"]).reset_index() # Group by 'doy' and calculate mean and median of 'TMAX' 
    print("Created a new DataFrame with mean and median temperatures for each day of the year. Here are the first few rows:")
    print(agg.head())
    
    return agg