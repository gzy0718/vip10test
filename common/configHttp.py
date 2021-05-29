#接受testcase传入的接口请求数据，根据具体的请求逻辑完成接口测试，将接口返回的关键结果返回给testcase
#实现 逻辑同tastcase
import requests
from  common.logs import *

class CongfigHttp():

    def __init__(self,url,value,method):
        self.url=url
        self.value=value
        self.method=method
        # logger=log()
        # logger.info('调用的日志方法')


    def run(self):
        #根据method进行判断
        if self.method.lower()=='get':
            return self.__get()
        elif self.method.lower()=='post':
            return self.__post()

    def __get(self):
        #读出来的都是字符串，需要eval转换
        result = requests.get(url=self.url, params=eval(self.value))
        self.real_errcode = result.json()['errorCode']
        self.status_code = result.status_code
        # print(result)
        return self.real_errcode,self.status_code

    def __post(self):
        result = requests.post(url=self.url, data=eval(self.value))
        # logger.debug(f"post请求的参数:url={self.url}")
        real_errcode = result.json()['errorCode']
        status_code = result.status_code
        # logger.info(f'返回的statuscode:{status_code},url={self.url}')
        return real_errcode, status_code

if __name__=='__main__':
    list1=[{'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'Method': 'post', 'value': "{'username':'liangchao','password':'123456'}", 'expect': '0', 'real': '', 'status': ''}, {'id': '2', 'interfaceUrl': 'https://www.wanandroid.com/user/register', 'name': 'register', 'Method': 'post', 'value': "{'username':'liangchao03','password':'123456','repassword':'123456'}", 'expect': '0', 'real': '', 'status': ''}, {'id': '3', 'interfaceUrl': 'https://www.wanandroid.com/user/logout/json', 'name': 'logout', 'Method': 'get', 'value': "{'username':'liangchao'}", 'expect': '0', 'real': '', 'status': ''}]
    url = list1[0]['interfaceUrl']
    value = list1[0]['value']
    method= list1[0]['Method']
    ch = CongfigHttp(url,value,method)
    print(ch.run())

