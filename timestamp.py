import zipfile
import os
import pandas as pd
from datetime import datetime

# Extracting the load_timestamp from the zip file name and formatting it
zip_filename = '20240305124003123456_Extract.zip'
timestamp = datetime.strptime(zip_filename.split('_')[0], '%Y%m%d%H%M%S%f').strftime('%Y-%m-%d %H:%M:%S')

# Create a directory to extract the files if it doesn't exist
extracted_dir = 'extracted_files'
if not os.path.exists(extracted_dir):
    os.makedirs(extracted_dir)

# Extracting the zip file
with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall(extracted_dir)

# Function to add load_timestamp as a new column
def add_load_timestamp(csv_file):
    csv_path = os.path.join(extracted_dir,zip_filename, csv_file)
    df = pd.read_csv(csv_path)
    print(df.head())
    df['load_timestamp'] = timestamp
    df.to_csv(csv_path, index=False)
    print(df.head())

# Applying the function to both sample files
add_load_timestamp('sample.csv')
add_load_timestamp('sample2.csv')






