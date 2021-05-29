'''
实现逻辑：
1.导入包
2.定义数据类

3.定义数据方法
'''

import xlrd, os
from xlutils.copy import copy
from common.logs import logger


class WriteExcel():
    def __init__(self):
        self.excel = os.path.dirname(os.path.dirname(__file__)) + '/testData/data.xls'
        # logger.info(self.excel)
        self.rb = xlrd.open_workbook(self.excel)

        self.wb = copy(self.rb)

        self.ws = self.wb.get_sheet(0)

    def writeData(self, x, y, real, status):
        self.ws.write(x, y, real)
        self.ws.write(x, y + 1, status)
        self.wb.save(self.excel)


if __name__ == '__main__':
    we = WriteExcel()
    # re=we.writeData(1,6,200,403)
    # 提供给testcase使用
