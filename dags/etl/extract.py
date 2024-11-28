import os
import pandas as pd
import opendatasets as od

#info
kaggle_url = "https://www.kaggle.com/datasets/priyamchoksi/credit-card-transactions-dataset"
save_dir = "./batch/data/"

#extract method:
# kaggle api
def extract_data_from_kaggle_api(dataset_url, data_dir):
    data_dir = './data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    od.download(kaggle_url, data_dir=data_dir)


# kaggle csv files
def extract_data_from_kaggle_csv(directory):
# Dictionary to store DataFrame variables
    csv_dataframes = {}

    # Loop through files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):  # Check if the file is a CSV
            variable_name = os.path.splitext(filename)[0]  # Use filename (without extension) as the variable name
            file_path = os.path.join(directory, filename)
            csv_dataframes[variable_name] = pd.read_csv(file_path)
            print(f"Loaded {filename} into variable '{variable_name}'")
    
    return csv_dataframes

def load_dataset():
    extract_data_from_kaggle_api(kaggle_url, save_dir)
    csv_files = extract_data_from_kaggle_csv(save_dir)

    return csv_files