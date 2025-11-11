
import sys , os
import inspect
import logging
from colorama import init
sys.path.append('..')
init()

from utils.config.SHRLogCore_readConfigFile import read_config_file
from utils.config.SHRLogCore_writeConfigFile import write_ini_file
from utils.time.SHRLogCore_pytzTimeSynchronizer import sync_system_time

class SHRLogCore():
    def __init__(self):
        self._EXEPATH = os.getcwd()
        self._SHRLogCoreConfigSettings : dict = {}
        self._SHRLogCoreDefaultConfigSettings : dict = {'SHRLogCore': {'isOutpuingLogsInConsole': 'True'}}
        self.__init_SHRLogCoreConfigSettings()
    
    def __init_SHRLogCoreConfigSettings(self):
        if os.path.exists(os.path.join(self._EXEPATH , 'config' , 'SHRLogCoreConfigSettings.ini')):
            try:
                self._SHRLogCoreConfigSettings = read_config_file(os.path.join(self._EXEPATH , 'config' , 'SHRLogCoreConfigSettings.ini'))
                self.__outputLogsInConsole('INFO' , 'SHRLogCoreConfigSettings.ini 文件读取成功')
                print(self._SHRLogCoreConfigSettings)
            except:
                self.__outputLogsInConsole('CRITICAL' , 'SHRLogCoreConfigSettings.ini 文件读取失败')
        else:
            if os.path.exists(os.path.join(self._EXEPATH , 'config')):
                self.__outputLogsInConsole('CRITICAL' , 'SHRLogCoreConfigSettings.ini 文件丢失')
                write_ini_file(self._SHRLogCoreDefaultConfigSettings , os.path.join(self._EXEPATH , 'config' , 'SHRLogCoreConfigSettings.ini'))
                self.__outputLogsInConsole('INFO' , 'SHRLogCoreConfigSettings.ini 重新写入完成')
                self.__init_SHRLogCoreConfigSettings()
            else:
                os.mkdir(os.path.join(self._EXEPATH , 'config'))
                self.__outputLogsInConsole('INFO' , 'config 文件夹已创建')
                self.__init_SHRLogCoreConfigSettings()
    
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