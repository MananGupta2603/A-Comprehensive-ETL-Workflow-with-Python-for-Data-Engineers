from script.extract_csv import extract_csv
from script.extract_json import extract_json
from script.extract_xml import extract_xml
from script.transform import transform_data
from script.load import load_data
import logging
import pandas as pd

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO, filename='A-Comprehensive-ETL-Workflow-with-Python-for-Data-Engineers/logs/etl_process.log',
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Starting ETL process')
    
    # Extraction
    logging.info('Extracting CSV data...')
    csv_data = extract_csv('A-Comprehensive-ETL-Workflow-with-Python-for-Data-Engineers/data/')
    logging.info('Extracting JSON data...')
    json_data = extract_json('A-Comprehensive-ETL-Workflow-with-Python-for-Data-Engineers/data/')
    logging.info('Extracting XML data...')
    xml_data = extract_xml('A-Comprehensive-ETL-Workflow-with-Python-for-Data-Engineers/data/')
    logging.info('Data extraction complete')

    # Combine Data
    logging.info('Combining extracted data...')
    combined_data = pd.concat([csv_data, json_data, xml_data], ignore_index=True)

    # Transformation
    logging.info('Transforming data...')
    transformed_data = transform_data(combined_data)
    logging.info('Data transformation complete')

    # Loading
    logging.info('Loading transformed data into output...')
    load_data(transformed_data, 'A-Comprehensive-ETL-Workflow-with-Python-for-Data-Engineers/transformed/transformed_data.csv')
    logging.info('Data loading complete')

if __name__ == '__main__':
    main()
