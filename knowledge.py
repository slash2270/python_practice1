import os
import sys
import B.B1.b3
from B import B1
from B.B1 import b1
from B.B2 import b4

"""
文檔注釋：

要為所有的公共模塊，函數，類和方法編寫文檔說明
非公共的方法沒有必要，但是應該有一個描述方法具體作用的注釋。這個注釋應該在def那一行之后
多行文檔注釋使用的結尾三引號應該是自成一行

模塊內置屬性：

   __name__   直接運行本模塊，__name__值為__main__；import module，__name__值為模塊名字。
   __file__   當前 module的絕對路徑
   __dict__  
   __doc__   
   __package__   
   __path__   

"""


class A(B1.b1.B01, B1.b3.B03):

    def __init__(self=None):
        B1.b1.B01.__init__()
        B1.b1.b2.B02.__init__()
        B1.b3.B03.__init__()


def describe():
    """
    描述函数要做的事情
    :param: parameter1 参数一描述(类型、用途等)
    :param: parameter2 参数二描述
    :return: 返回值描述
    """


def print_hi(name):  # 在下面的代碼行中使用斷點來調試您的腳本。
    print(f'Hi, {name}')  # 按 ⌘F8 切換斷點.


def print_sys():  # 是一個 將模塊名稱（module_name）映射到已加載的模塊（modules） 的字典。可用來強制重新加載modules。
    print(sys.modules)  # 打印，查看該字典具體內容。


def print_locals(a=1):
    b = 2
    set_locals = locals()
    set_locals['c'] = 3
    print(locals())  # 打印当前函数（方法）的局部命名空间
    print(set_locals['c'])

    """
    locals = locals()#只读，不可写。将报错！
    locals['c'] = 3
    print(c)
    """

    return a + b


def print_globals():
    set_globals = globals()
    set_globals['d'] = 4
    print(set_globals)
    print(globals().get('d'))
    print(globals())  # 打印当前模块main.py的全局命名空间
    # 内置函数locals()、globals()返回一个字典。区别：前者只读、后者可写。


def main_path():
    base_directory = os.path.dirname(os.path.abspath(__file__))  # 存放main.py所在的絕對路徑
    sys.path.append(base_directory)
    print(base_directory)
    print(sys.path)


# 按裝訂線中的綠色按鈕運行腳本。
# if __name__ == '__main__':  # func() 如果沒有Main就用這個方法
def func():
    print_hi('PyCharm')
    print_sys()
    print_locals()
    print_globals()
    main_path()
    b1.B01.__init__()  # 其他類別的絕對路徑
    b1.b2.B02.__init__()  # 其他類別的相對路徑
    B.B1.b3.B03.__init__()  # 單獨導入包
    A.__init__()  # 多繼承
    print(b4.getB5)  # 順序導入-importR
    from B.B2 import b5  # 延遲導入（lazy import)
    print(b5.B05.b)
