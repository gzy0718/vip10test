#1-异常

#语法：
try:
    print(a)
except:
    print('出现异常执行的代码')

#捕获异常信息
try:
    print(a)
except (NameError) as result:
    print(result)

#捕获所有异常
try:
    print(a=1)
except Exception as result:
    print(result)

#没有异常执行的代码else
try:
    print(1)
except Exception as result:
    print(result)
else:
    print('没有异常执行的部分')

#无论是否有异常，都需要执行的部分
try:
    print(a)
except Exception as result:
    print(result)
finally:
    print("有没有异常，都要执行这段话")
