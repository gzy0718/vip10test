'''
1.定义公共的日志输出模块，供其他模块调试使用
    1.1导包
    1.2basicconfig定制日志参数
    1.3获取日志记录器，并返回

'''

import logging

def log():
    logging.basicConfig(level=logging.INFO,format='%(name)s-%(asctime)s-%(levelname)s-%(message)s')
    logger=logging.getLogger('Interface')
    return logger

logger=log()
# logger.info("---这是日志-")