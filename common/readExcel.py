'''
1.导入xlrd包
2.打开excel
3.确定sheet页
4.确定数据的最大行（循环的次数）
    4.1定有一个空列表保存最终数据
    4.2读取第一行最为key列表
    4.3迭代读取剩下的所有行（value列表）
    4.4将key列表和value列表组合成字典
    4.5将组合后的字段追加进列表
5.返回textdata，return

'''
import  xlrd,os


#
# #获取当前路径，推导目标文件路径
# print(os.path.dirname(__file__))
#
# #读取目标文件
# readbook = xlrd.open_workbook(r'/Users/v_gaoziyang/PycharmProjects/unitest/testcase/data.xls')
#
# #获取目标文件所有sheet名字
# # allsheetnames = readbook.sheet_names()
# # print(allsheetnames)
#
# #通过名字读取目标文件的sheet
# sheet = readbook.sheet_by_name('urlSheet')
#
# #确定sheet最大行
# nrows = sheet.nrows
# print(nrows)
#
# #确定一个空列表，保存数据
# listdata=[ ]
#
# #获取某行的值
# listdata_key = sheet.row_values(0)
# print(listdata_key)
# #遍历获取剩余行数的值
# listdata_value=[sheet.row_values(i) for i in range(1,4)]
# print(listdata_value)
#
#
# # #将key和value组合成字典
# # dict1={listdata_key[i]:listdata_value[i] for i in range(len(listdata_key))}
# # print(dict1)
#
# import collections
#
# #
#
#
# # dic = collections.defaultdict(list)
# # for i,key in enumerate(listdata_key):
# #     for val in listdata_value:
# #         dic[key].append(val[i])
# #
# # print(dic)
#
# res = []
# for val in listdata_value:
#     temp = dict()
#     # print(val)
#     for i,key in range(len(listdata_key)):
#         # print(i,key)
#         temp[key] = val[i]
#     res.append(temp)
# print("key-val")
# print(res)
class ReadExcel():

    def __init__(self):
        cur_path = os.path.dirname(os.path.dirname(__file__))  # 当前路径/上一层目录/
        excel_dir = cur_path + '/testData/data.xls'
        readbook = xlrd.open_workbook(excel_dir)
    # allsheetnames = readbook.sheet_names()
        self.sheet = readbook.sheet_by_name('urlSheet')
        self.nrows = self.sheet.nrows

    def getData(self):
        # cur_path = os.path.dirname(os.path.dirname(__file__))  # 当前路径/上一层目录/
        # excel_dir = cur_path + '/testData/data.xls'
        # readbook = xlrd.open_workbook(excel_dir)
        # # allsheetnames = readbook.sheet_names()
        # sheet = readbook.sheet_by_name('urlSheet')
        # nrows = sheet.nrows
        # # print(nrows)

        listdata = []
        listdata_key = self.sheet.row_values(0)
        # print(listdata_key)
        for k in range(1,self.nrows):
            listdata_value = self.sheet.row_values(k)
            # print(listdata_value)
            dict1 = {listdata_key[i]:listdata_value[i] for i in range(len(listdata_key))}
            listdata.append(dict1)

            # print(listdata)
        return listdata

if __name__=='__main__':
    re=ReadExcel()
    print(re.getData())
