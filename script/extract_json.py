import pandas as pd
import glob

def extract_json(folder_path):
    json_files = glob.glob(f"{folder_path}/*.json")  # Find all JSON files
    dataframes = [pd.read_json(file, lines=True) for file in json_files]  # Read each JSON file
    combined_data = pd.concat(dataframes, ignore_index=True)  # Combine all JSON files
    return combined_data
