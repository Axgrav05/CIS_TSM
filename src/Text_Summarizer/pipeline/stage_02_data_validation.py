from Text_Summarizer.logging import logger
from Text_Summarizer.config import ConfigurationDirectory
from Text_Summarizer.entity import DataValidationConfig, DataIngestionConfig
from Text_Summarizer.conponents import DataValidation

class DataValidationPipeline:
    def run(self, ingestion_config = DataIngestionConfig):
        logger.info("-------- Stage 2: Data Validation Started --------")

        directory = ConfigurationDirectory()
        validation_config = directory.get_data_validation_config()

        data_val = DataValidation(validation_config)
        data_val.validate_all_files_exist(ingestion_config)

        logger.info("-------- Stage 2: Data Validation Completed --------")