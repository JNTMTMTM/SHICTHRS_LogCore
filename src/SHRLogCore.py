
import sys , os
sys.path.append('..')

from utils.config.SHRLogCore_readConfigFile import read_config_file

from colorama import init
init()

import logging


class SHRLogCore():
    def __init__(self):
        self._EXEPATH = os.getcwd()
        self._SHRLogCoreConfigSettings : dict = {}
        self.__init_SHRLogCoreConfigSettings()
    
    def __init_SHRLogCoreConfigSettings(self):
        if os.path.exists(os.path.join(self._EXEPATH , 'config' , 'SHRLogCoreConfigSettings.ini')):
            self._SHRLogCoreConfigSettings = read_config_file(os.path.join(self._EXEPATH , 'config' , 'SHRLogCoreConfigSettings.ini'))
        else:
            pass
    
    def __outputLogsInConsole(self , base , log_level : str , log_message : str):
        LOG_LEVEL_COLOR_CPT : dict = {'DEBUG' : '\033[32m' , 'INFO' : '\033[34m' , 'WARNING' : '\033[33m' , 'ERROR' : '\033[31m' , 'CRITICAL' : '\033[35m'}
        END_COLOR : str = '\033[0m'

        print(f'{LOG_LEVEL_COLOR_CPT[log_level]}[{log_level}] {base} : {log_message}{END_COLOR}')

# print(read_config_file(os.path.join(os.getcwd() , 'config' , 'SHRLogCoreConfigSettings.ini')))
