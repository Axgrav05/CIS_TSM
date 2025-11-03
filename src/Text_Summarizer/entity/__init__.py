from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: str
    source_URL: str
    local_data_file: str
    unzip_dir: str 

@dataclass
class DataValidationConfig:
    root_dir: str
    status_file: str 
    all_required_files: str 