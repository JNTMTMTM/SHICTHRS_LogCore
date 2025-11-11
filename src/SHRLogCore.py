
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
        self.__init_SHRLogCoreConfigSettings()  # 初始化日志配置文件
        self.__init_SHRLogCoreRecorder()  # 初始化日志记录器
    
    def __init_SHRLogCoreRecorder(self):
        logging.basicConfig(
            level = logging.DEBUG,
            format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            filename = 'app.log' ,
            datefmt = '%Y-%m-%d %H:%M:%S' ,
            encoding = 'utf-8'
        )
        self._logger = logging.getLogger("SHRLogCore")
        self.add_log('INFO' , 'SHRLogCore 日志记录器初始化完成')
    
    def __init_SHRLogCoreConfigSettings(self):
        if os.path.exists(os.path.join(self._EXEPATH , 'config' , 'SHRLogCoreConfigSettings.ini')):
            try:
                self._SHRLogCoreConfigSettings = read_config_file(os.path.join(self._EXEPATH , 'config' , 'SHRLogCoreConfigSettings.ini'))
                self.__outputLogsInConsole('INFO' , 'SHRLogCoreConfigSettings.ini 文件读取成功')
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

        LOG_LEVEL_COLOR_CPT : dict = {'DEBUG' : '\033[32m' ,
                                    'INFO' : '\033[34m' ,
                                    'WARNING' : '\033[33m' ,
                                    'ERROR' : '\033[31m' ,
                                    'CRITICAL' : '\033[35m'}

        END_COLOR : str = '\033[0m'
        temp_frame = inspect.currentframe()
        print(f'\033[1m{sync_system_time()}\033[0m {LOG_LEVEL_COLOR_CPT[log_level]}[{log_level}] {temp_frame.f_back.f_code.co_name} {END_COLOR}: {log_message}')

    def add_log(self , log_level : str , log_message : str):
        """
        >>> LOG_LEVEL_CPT   | LOG-LEVELS
        --------------------|-------------
                            | DEBUG
                            | INFO
                            | WARNING
                            | ERROR
                            | CRITICAL
        """
        LOG_LEVEL_CPT : dict = {'DEBUG' : self._logger.debug ,
                            'INFO' : self._logger.info ,
                            'WARNING' : self._logger.warning ,
                            'ERROR' : self._logger.error ,
                            'CRITICAL' : self._logger.critical}
        
        temp_frame = inspect.currentframe()
        log_message = f'{temp_frame.f_back.f_code.co_name} | ' + log_message

        if eval(self._SHRLogCoreConfigSettings['SHRLogCore']['isOutpuingLogsInConsole']):
            self.__outputLogsInConsole(log_level , log_message)
        LOG_LEVEL_CPT[log_level](log_message)


log = SHRLogCore()