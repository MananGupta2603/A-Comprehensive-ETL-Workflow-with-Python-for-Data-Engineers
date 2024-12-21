import pandas as pd
import glob
import xml.etree.ElementTree as ET

def extract_xml(folder_path):
    xml_files = glob.glob(f"{folder_path}/*.xml")  # Find all XML files
    all_data = []

    for file in xml_files:
        tree = ET.parse(file)
        root = tree.getroot()

        # Parse XML into a list of dictionaries
        for person in root.findall('person'):
            data = {
                'name': person.find('name').text,
                'height': float(person.find('height').text),
                'weight': float(person.find('weight').text),
            }
            all_data.append(data)

    # Convert list of dictionaries into a DataFrame
    combined_data = pd.DataFrame(all_data)
    return combined_data
