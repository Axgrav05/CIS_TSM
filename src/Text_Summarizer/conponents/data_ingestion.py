from Text_Summarizer.logging import logger
from Text_Summarizer.entity import DataIngestionConfig
import os
from urllib.request import urlretrieve
import zipfile

class DataIngestion:
    def __init__(self, config=DataIngestionConfig):
        self.config = config
        os.makedirs(self.config.root_dir, exist_ok=True)

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                logger.info(f"Started downloading URL {self.config.source_URL}")
                urlretrieve(self.config.source_URL, self.config.local_data_file)
                logger.info(f"File downloaded at {self.config.local_data_file}")
            except Exception as e:
                logger.info(f"Error during download:  {e}")


    def extract_zip_file(self):
        if not os.path.exists(self.config.unzip_dir):
            try:
                logger.info(f"Started extracting zip file")
                with zipfile.ZipFile(self.config.local_data_file) as zip_file:
                    zip_file.extractall(self.config.unzip_dir)
                logger.info(f"Successfully extracted zip file")
            except Exception as e:
                logger.info(f"Error during extracting: {e}")