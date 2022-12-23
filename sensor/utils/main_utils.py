import yaml
import numpy as np
import os,sys
from sensor.exception import SensorException
from sensor.logger import logging


""" Reading the yaml_file"""
def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise SensorException(e, sys) from e

    
""" Reading the yaml_file and creating if we want the yaml_file if replace we keep to true"""

def write_yaml_file(file_path:str,content:object,replace:bool = False) ->None:
    try:

        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)   ## remove the previously created file
        
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file:
            yaml.dump(content,file)   ## dumping the content into the yaml_file


    except Exception as e:
        raise SensorException(e,sys)


















