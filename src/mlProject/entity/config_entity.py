from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_directory: str
    source_url: str
    local_data_file: str
    unzip_directory: str
