from Text_Summarizer.entity import DataIngestionConfig, DataValidationConfig
import yaml 
import os

class ConfigurationDirectory:

    def __init__(self, config_filepath="config/config.yaml"):
        with open(config_filepath, 'r') as f:
            self.config = yaml.safe_load(f)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        ingestion_config = self.config["data_ingestion"]
        print(f"{type(ingestion_config)}")
        os.makedirs(ingestion_config["root_dir"], exist_ok=True)
        return DataIngestionConfig(**ingestion_config)
    
    def get_data_validation_config(self) -> DataValidationConfig:
        validation_config = self.config["data_validation"]
        os.makedirs(validation_config["root_dir"], exist_ok=True)
        return DataValidationConfig(**validation_config)

