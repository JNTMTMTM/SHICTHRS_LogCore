
import sys , os
import inspect
import logging
from colorama import init
sys.path.append('..')
init()

from utils.config.SHRLogCore_readConfigFile import read_config_file
from utils.time.SHRLogCore_pytzTimeSynchronizer import sync_system_time

class SHRLogCore():
    def __init__(self):
        self._EXEPATH = os.getcwd()
        self._SHRLogCoreConfigSettings : dict = {}
        self.__init_SHRLogCoreConfigSettings()
    
    def __init_SHRLogCoreConfigSettings(self):
        if os.path.exists(os.path.join(self._EXEPATH , 'config' , 'SHRLogCoreConfigSettings.ini')):
            try:
                self._SHRLogCoreConfigSettings = read_config_file(os.path.join(self._EXEPATH , 'config' , 'SHRLogCoreConfigSettings.ini'))
                self.__outputLogsInConsole('DEBUG' , 'SHRLogCoreConfigSettings.ini 文件读取成功')
            except:
                self.__outputLogsInConsole('CRITICAL' , 'SHRLogCoreConfigSettings.ini 文件读取失败')
        else:
            self.__outputLogsInConsole('CRITICAL' , 'SHRLogCoreConfigSettings.ini 文件丢失')
    
    def __outputLogsInConsole(self , log_level : str , log_message : str):
        """
        LOG_LEVEL_COLOR_CPT | LOG-LEVELS
        --------------------|-------------
        GREEN               | DEBUG
        BLUE                | INFO
        YELLOW              | WARNING
        RED                 | ERROR
        MAGENTA             | CRITICAL
        """

        LOG_LEVEL_COLOR_CPT : dict = {'DEBUG' : '\033[32m' , 'INFO' : '\033[34m' , 'WARNING' : '\033[33m' , 'ERROR' : '\033[31m' , 'CRITICAL' : '\033[35m'}
        END_COLOR : str = '\033[0m'
        temp_frame = inspect.currentframe()
        print(f'\033[1m{sync_system_time()}\033[0m {LOG_LEVEL_COLOR_CPT[log_level]}[{log_level}] {temp_frame.f_back.f_code.co_name} {END_COLOR}: {log_message}')

log = SHRLogCore()