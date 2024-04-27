import pandas as pd

def load_data_from_excel(filepath):
    # Load the Excel file, skipping irrelevant rows if necessary
    df = pd.read_excel(filepath, skiprows=0)
    # Select only the required columns by index
    df = df.iloc[:, [0, 3]]
    # Rename columns for clarity
    df.columns = ['Label', 'English Prompt']
    return df
