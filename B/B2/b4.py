from .b5 import B05  # 循環導入/嵌套導入-import


def get_b5(arg):
    return 1 + arg


getB5 = get_b5(B05.b)


class B04:

    def __init__(self=None):
        B05.__init__()
        print('World B04')
