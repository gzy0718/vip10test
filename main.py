'''
查找所有用例，执行用例，生成报告，清理报告
1.导入包：unitest，HTMLTestRunner
2.使用TestLoader查找测试用例，生成测试套件
3.使用HtmlTestRunner执行测试用例，生成报告
4.实现自动清理（1.自动清理报告的数量；2.每次运行前，删除以前报告
5.自动生成的报告添加邮件的额附件发送
'''
#把HTMLTestRunner文件放到venv目录下

import unittest,os
from HTMLTestRunner import HTMLTestRunner

project_dir = os.path.dirname(__file__)

def creat_suite():

    case_dir = project_dir + '/testCase'

    suite = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='test*.py', top_level_dir=None)

    return  suite

if __name__ == '__main__':
    suite = creat_suite()
    report = project_dir + '/report/report.html'
    fp = open(report, 'wb')
    runner = HTMLTestRunner(stream=fp,title='玩安卓测试报告',description='测试详情')
    runner.run(suite)
    fp.close()
