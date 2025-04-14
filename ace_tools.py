import pandas as pd

def display_dataframe_to_user(name: str, dataframe: pd.DataFrame):
    """
    Displays the DataFrame in a user-friendly way.
    
    Args:
        name (str): The name or title of the DataFrame.
        dataframe (pd.DataFrame): The DataFrame to display.
    """
    print(f"Displaying DataFrame: {name}")
    print(dataframe.to_string(index=False))
