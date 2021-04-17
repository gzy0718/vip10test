print("你好")
# try:
#  可能发⽣错误的代码
# except:
#  如果出现异常执⾏的代码
try:
    f= open("test.py", "r")
except:
    f= open("text.py", "w")
    # else表示的是如果没有异常要执⾏的代码
else:
    print("没有异常都要打印的东西")
    # finally表示的是⽆论是否异常都要执⾏的代码，例如关闭⽂件
finally:
    f.close()
# print(num)
try:
    print(num)
# except NameError:   两种方法，一种是已知错误类型，另一种是不知道错误类型Exception
except Exception as msg:  #打印错误信息
    print(msg)
else:
    print("没有异常都要打印的东西")
