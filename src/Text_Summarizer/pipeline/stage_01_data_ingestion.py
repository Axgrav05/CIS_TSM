from Text_Summarizer.logging import logger
from Text_Summarizer.config import ConfigurationDirectory
from Text_Summarizer.entity import DataIngestionConfig
from Text_Summarizer.conponents import DataIngestion

class DataIngestionPipeline:
    def run(self):

        logger.info("----------- Stage 1: Data Ingestion Started -----------")

        directory = ConfigurationDirectory()
        ingestion_config = directory.get_data_ingestion_config()

        data_ingestion= DataIngestion(ingestion_config)

        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

        logger.info("----------- Stage 1: Data Ingestion Completed -----------")


