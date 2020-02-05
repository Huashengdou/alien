
# 导入python模块的方式
import math
# from math import cos,tan
print(math.sin(1.23))

# 以这种方式导入，可以不用跟"math."
from math import *
print(tan(1))

# 导入模块并指定别名
import  math as m
print(m.sin(1.23))