print("你好")
try:
    f= open("test3.py", "r")
except:
    f= open("text.py", "w")
# print(num)
try:
    print(num)
# except NameError:   两种方法，一种是已知错误类型，另一种是不知道错误类型Exception
except Exception as msg:  #打印错误信息
    print(msg)
