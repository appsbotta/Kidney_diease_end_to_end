import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self)->str:
        try:
            os.makedirs(self.config.root_dir,exist_ok=True)
            url = self.config.source_url
            zip_location = self.config.local_data_file
            logger.info(f"Downloading data set from {url} in to {zip_location}")
            id = url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+id,zip_location)
            logger.info(f"Downloaded data set from {url} in to {zip_location}")
        except Exception as e:
            raise e
        
    def extract_zip(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_file:
            zip_file.extractall(unzip_path)