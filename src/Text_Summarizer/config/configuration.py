from Text_Summarizer.entity import DataIngestionConfig, DataValidationConfig
import yaml 
import os

class ConfigurationDirectory:

    def __init__(self, config_filepath="config/config.yaml"):
        with open(config_filepath, 'r') as f:
            self.config = yaml.safe_load(f)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]
        os.makedirs(config.root_dir, exist_ok=True)
        return DataIngestionConfig(**config)
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config["data_validation"]
        os.makedirs(config.root_dir, exist_ok=True)
        return DataValidationConfig(**config)

