import os
from pathlib import Path

# Get the root directory of the project
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Define the file paths
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, "config", "config.yaml")
PARAMS_FILE_PATH = os.path.join(ROOT_DIR, "config", "params.yaml")
SCHEMA_FILE_PATH = os.path.join(ROOT_DIR, "config", "schema.yaml")
