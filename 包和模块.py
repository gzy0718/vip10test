import time as tt  #定义别名
tt.sleep(2)
print("hello")

from math import *  #导入所有模块
print(sqrt(9))

from mypackage.test1 import *

testA()
#testB()

from mypackage import *
# 必须在 __init__.py ⽂件中添加 __all__ = [] ，控制允许导⼊的模块列表
test2.testB()
