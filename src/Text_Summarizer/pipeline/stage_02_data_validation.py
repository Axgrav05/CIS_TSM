from Text_Summarizer.logging import logger
from Text_Summarizer.config import ConfigurationDirectory
from Text_Summarizer.conponents import DataValidation

class DataValidationPipeline:
    def run(self, unzip_dir):
        try:
            logger.info("----------- Stage 2: Data Validation Started -----------")

            directory = ConfigurationDirectory()
            validation_config = directory.get_data_validation_config()

            data_val = DataValidation(validation_config)
            val = data_val.validate_all_files_exist(unzip_dir)

            logger.info("----------- Stage 2: Data Validation Completed -----------")

            return val
        except Exception as e:
            logger.info(f"Exception in Validation: {e}")