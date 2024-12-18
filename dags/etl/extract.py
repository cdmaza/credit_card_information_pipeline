import os
import pandas as pd
import opendatasets as od
import json

#info
kaggle_url = "https://www.kaggle.com/datasets/priyamchoksi/credit-card-transactions-dataset"
kaggle_json_path = './common/kaggle.json'
data_dir = "./batch/data/"


#extract method:
# kaggle api
def extract_data_from_kaggle_api(dataset_url, data_dir):
    with open(kaggle_json_path, 'r') as file:
        kaggle_credentials = json.load(file)

    os.environ['KAGGLE_USERNAME'] = kaggle_credentials['username']
    os.environ['KAGGLE_KEY'] = kaggle_credentials['key']

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    od.download(kaggle_url, data_dir=data_dir)


# kaggle csv files
def extract_data_from_kaggle_csv(directory):
    csv_dataframes = {}

    # Loop through files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"): 
            variable_name = os.path.splitext(filename)[0] 
            file_path = os.path.join(directory, filename)
            csv_dataframes[variable_name] = pd.read_csv(file_path)
            print(f"Loaded {filename} into variable '{variable_name}'")
    
    return csv_dataframes

def load_dataset():
    extract_data_from_kaggle_api(kaggle_url, data_dir)
    csv_files = extract_data_from_kaggle_csv(data_dir)

    return csv_files