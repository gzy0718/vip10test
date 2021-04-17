# print("你好")
# # try:
# #  可能发⽣错误的代码
# # except:
# #  如果出现异常执⾏的代码
# try:
#     f= open("test1.txt", "r")
# except:
#     f= open("text1.txt", "w")
#     # else表示的是如果没有异常要执⾏的代码
# else:
#     print("没有异常都要打印的东西")
#     # finally表示的是⽆论是否异常都要执⾏的代码，例如关闭⽂件
# finally:
#     f.close()
# # print(num)
# try:
#     print(num)
# # except NameError:   两种方法，一种是已知错误类型，另一种是不知道错误类型Exception
# except Exception as msg:  #打印错误信息
#     print(msg)
# else:
#     print("没有异常都要打印的东西")

"""
体验异常传递
需求：
1. 尝试只读⽅式打开test.txt⽂件，如果⽂件存在则读取⽂件内容，⽂件不存在则提示⽤户即可。
2. 读取内容要求：尝试循环读取内容，读取过程中如果检测到⽤户意外终⽌程序，则 except 捕获异常
并提示⽤户。

"""

import time

try:
    f = open('text1.txt')

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果在读取⽂文件的过程中，产⽣生了了异常，那么就会捕获到
        # ⽐比如 按下了了 ctrl+c
        print('意外终⽌止了了读取数据')
    finally:
        f.close()
        print('关闭⽂文件')
except:
    print("没有这个⽂文件")
