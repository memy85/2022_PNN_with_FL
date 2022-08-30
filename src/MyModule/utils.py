
import pandas as pd
import yaml 
from pathlib import Path

def load_config():
    project_dir = Path().cwd().parents()[1]
    config_path = project_dir.joinpath('config/config.yaml')
    with open(config_path) as f:
        return yaml.load(f, yaml.SafeLoader)