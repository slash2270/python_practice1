from . import b2  # 这种导入方式会报错。


# import b2  # 正确
# b2.get() 弱型別語言寫法

def get_b2(arg):
    return 1 + arg


getB2 = get_b2(b2.B02.b)


class B01:

    def __init__(self=None):
        b2.B02.__init__()
        print('Hi B01')
