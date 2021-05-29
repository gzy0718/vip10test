import requests,unittest
from common.readExcel import *
from ddt import *
from common.configHttp import *
from common.writeExcel import *
re = ReadExcel()
testdata =re.getData()
# logger.info(f'---------{testdata}')
#获取测试数据,调用readexcel内部方法
@ddt

class TestCase(unittest.TestCase):


#提取测试数据内部的method方法
    @data(*testdata)
    @unpack
    def test_run(self,id,interfaceUrl,name, Method, value, expect, real,status):

        # method = Method
        # url=interfaceUrl
        # value=value
        # expect=expect
        # id=id

        #调用CongfigHttp.run
        ch = CongfigHttp(interfaceUrl, value, Method)
        real_errcode,status_code=ch.run()

#根据method进行判断：1.如果是get，调用get请求；2.如果是post，调用poist方法
#         if method == 'get':
#                 result = requests.get(url=url,params=value)
#                 print('result',result.json())
#         elif method=='post':
#                 result = requests.post(url=url,data=value)
#                 print('result',result.json())
#
# #从接口请求结果中，提取需要断言的字段
#         real = result.json()['errorCode']


#将实际提取的errorcode和excel中预期的进行比较
    #相同即通过
    #不同则失败
        try:
            self.assertEqual(str(status_code),'200')
            self.assertEqual(str(real_errcode),str(expect))
            status = 'success'
        except Exception as msg:
            print('系统提示:',msg)
            status = 'fail'
            raise
        finally:
            writeexcel=WriteExcel()
            writeexcel.writeData(int(id),6,real_errcode,status)





#将接口断言得到的结果写入excel-status
if __name__=='__main__':
    unittest.main()
