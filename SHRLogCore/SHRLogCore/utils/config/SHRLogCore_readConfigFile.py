
# src\utils\config\SHRLogCore_readConfigFile.py

from .SHRLogCore_readConfigFileBase import CaseSensitiveConfigParser

def read_config_file(file_path : str) -> dict:
    temp_result_dict : dict = {}

    object_conf = CaseSensitiveConfigParser()
    object_conf.read(file_path , encoding='utf-8')
    
    for section in object_conf.sections():
        section_dict = {}
        for key in object_conf[section]:
            section_dict[key] = object_conf.get(section, key)
        temp_result_dict[section] = section_dict
    
    return temp_result_dict

