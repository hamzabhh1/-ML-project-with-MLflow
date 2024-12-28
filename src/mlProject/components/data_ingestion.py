import os
import urllib.request
import zipfile
from src.mlProject.entity.config_entity import DataIngestionConfig
from src.mlProject.utils.common import create_directories

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            create_directories([self.config.root_directory])
            filename, headers = urllib.request.urlretrieve(
                self.config.source_url,
                self.config.local_data_file
            )
            print(f"Downloaded {filename} with headers {headers}")
        else:
            print(f"File already exists: {self.config.local_data_file}")

    def extract_zip_file(self):
        create_directories([self.config.unzip_directory])
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_directory)
        print(f"Extracted data to {self.config.unzip_directory}")
