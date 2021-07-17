'''
查找所有用例，执行用例，生成报告，清理报告
1.导入包：unitest，HTMLTestRunner
2.使用TestLoader查找测试用例，生成测试套件
3.使用HtmlTestRunner执行测试用例，生成报告
4.实现自动清理（1.自动清理报告的数量；2.每次运行前，删除以前报告
5.自动生成的报告添加邮件的额附件发送
'''
#把HTMLTestRunner文件放到venv目录下

import unittest,os,time
from HTMLTestRunner import HTMLTestRunner
from common.logs import *
from common.configEmail import SendEmail



project_dir = os.path.dirname(__file__)

def creat_suite():
    # project_dir = os.path.dirname(__file__)
    case_dir = project_dir + '/testcase'

    suite = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='test*.py', top_level_dir=None)



    return  suite

def auto_clear(count):

    filelist = os.listdir(project_dir+'/report')


            #方案2
            # os.remove(project_dir+'/report/'+i)
            #方案1
    logger.info(filelist)
    if len(filelist)>count:
        for i in range(len(filelist)-count):
            os.remove(project_dir + '/report/' + filelist[i])





if __name__ == '__main__':
    auto_clear(5)
    suite = creat_suite()
    timestr = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime())

    report = project_dir + '/report/'+timestr+'report.html'
    fp = open(report, 'wb')
    runner = HTMLTestRunner(stream=fp,title='玩安卓测试报告',description='测试详情')
    runner.run(suite)
    suite=SendEmail()
    suite.senMail()
    fp.close()


