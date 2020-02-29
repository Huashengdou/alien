"""
设置python模块搜索路径的方式
1. 设置PYTHONPATH环境变量，直接在pycharm中工程设置中添加该变量即可，在Linux下可配置家目录下的profile文件；或者在命令行中使用export临时添加
2. 添加.pth文件，在python根目录下D:\yanjySoftware\python\Lib\site-packages，添加abc.pth文件，将路径添加到该文件中
3. 通过sys.path设置路径---临时设置，下面的例子显示
4. 如果使用PyCharm，可以直接设置搜索路径，直接在需要引用的模块目录上面右键mark dictionary as
"""

# 默认情况下，python解释器会搜索当前目录，所有已安装的内置模块和第三方模块，
# 搜索路径存放在sys的path变量中
import sys

# 运行时修改，运行完毕后失效
sys.path.append("D:\pythonExerse\python_learn\ererse\someExample\module")
import hello

print(hello.sayHello('Mary'))