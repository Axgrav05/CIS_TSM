from Text_Summarizer.entity import DataValidationConfig, DataIngestionConfig
from Text_Summarizer.logging import logger
import os
from pathlib import Path

class DataValidation:
    def __init__(self, config=DataValidationConfig):
        self.config = config
        os.makedirs(self.config.root_dir, exist_ok=True)
        
    def validate_all_files_exist(self, val=DataIngestionConfig) -> bool:
        validation = True
        folder_path = Path(val.config.unzip_dir)

        for file in self.config.all_required_files:
            file_path = folder_path / file
            if not file_path.exists():
                logger.info(f"Path doesn't exist: {file_path}")
                validation = False
            else:
                logger.info(f"Path exist: {file_path}")

        with open(self.config.status_file, 'w') as file:
            file.write(f"Validation Status: {validation}")
        
        return validation


                

