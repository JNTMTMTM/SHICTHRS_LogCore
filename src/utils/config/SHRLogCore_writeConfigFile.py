
# src\utils\config\SHRLogCore_writeConfigFile.py

from utils.config.SHRLogCore_readConfigFileBase import CaseSensitiveConfigParser

def write_ini_file(config_dict : dict, file_path : str):
    object_conf = CaseSensitiveConfigParser()
    
    for section , options in config_dict.items():
        object_conf[section] = {}
        for key , value in options.items():
            object_conf[section][key] = str(value)
    
    with open(file_path , 'w' , encoding='utf-8') as configfile:
        object_conf.write(configfile)
        configfile.close()