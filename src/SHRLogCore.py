
import sys , os
sys.path.append('..')

from utils.config.SHRLogCore_readConfigFile import read_config_file
import logging


class SHRLogCore():
    def __init__(self):
        pass

print(read_config_file(os.path.join(os.getcwd() , 'config' , 'SHRLogCoreConfigSettings.ini')))
