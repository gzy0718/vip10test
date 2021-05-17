import requests,json

#get请求
# urlstr='https://www.wanandroid.com/'
# paramer={'k':'android'}
# r=requests.get(url=urlstr,params=paramer)
#
# print(r.text)
# print(r.status_code)
# print(r.headers)
# print(r.cookies)
# print('-----------')
# #print(r.json())
# print('--------')
#
# #post请求
# urlstr='http://httpbin.org/post'
# payload={'qq群名':'selenium+jmeter+loadrunner','qq群号':'106014970'}
# payload=json.dumps(payload)
# r=requests.post(url=urlstr,data=payload)
# #r=requests.post(url=urlstr,json=payload)第二种方法，可以不用提前转换json
# print(r.text)
# print(r.json())
# print('-----------------------')

#post登录接口实例
urlstr='https://www.wanandroid.com/user/login'
header={'User-Agent': 'Mozilla/5.0'}
payload={'username': '18612863544','password': '000000'}
a = requests.session()
r1=a.post(url=urlstr,data=payload,headers=header)
#需要判断是否是表单，如果是表单，可以直接使用data
print(r1.text)
print(r1.cookies['JSESSIONID'])
# if r.status_code==200:#断言判断
#     dict1=s.json()
#     print(dict1['data']['username'])
# else:
#     print('接口不通')
print('----------------')

cookie1=r1.cookies  #方法1：携带cookie发送请求
cookie2={'JSESSIONID':r1.cookies['JSESSIONID']}  #方法2：通过定制cookie，访问目标网址
url1='https://www.wanandroid.com/lg/todo/list/0'
header2={'cookie':'JSESSIONID='+r1.cookies['JSESSIONID']} #方法3：通过headers带入cookie
r2 = requests.get(url=url1,headers=header2)
print(r2.text)
print('===============')

url3='http://www.kuaidi.com/index-ajaxselectcourierinfo-773058962040428-shentong-KUAIDI1621064142609.html'
# header1={'User-Agent': 'Mozilla/5.0'}
# s=requests.session()
r=requests.get(url=url3)
result=r.json()
data=result['data']
print(data)
print(data[0])
grt_result=data[0]['context']
print(grt_result)


