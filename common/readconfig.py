'''

1.导包
2.准备目标文件
3.创建对象，调用read方法读取
4.对外提供读取section下的键值对的方法

'''

import configparser,os

from common.logs import *

class ReadConfig():
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.file=os.path.dirname(os.path.dirname(__file__))+'/config.ini'
        self.conf.read(self.file,encoding='utf-8-sig')
        # logger.info(f'config.ini文件的路径是：{self.file}')

    def get_mysql(self,section):

        try:
            result = self.conf.items(section)
            logger.info(result)
        except Exception as msg:
            logger.error(f'系统报错：{msg}')


if __name__=='__main__':
    rc=ReadConfig()
    rc.get_mysql('mysql')
