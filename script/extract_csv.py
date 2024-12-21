
import pandas as pd
import glob

def extract_csv(folder_path):
    csv_files = glob.glob(f"{folder_path}/*.csv")  # Find all CSV files
    dataframes = [pd.read_csv(file) for file in csv_files]  # Read each CSV file
    combined_data = pd.concat(dataframes, ignore_index=True)  # Combine all CSV files
    return combined_data

