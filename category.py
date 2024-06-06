"""
__name__ ：属性的名字
__doc__ ：属性的文档字符串
__get__(object) ：获取对象属性值的方法
__set__(object, value) ：设置对象属性值的方法
__delete__(object, value) ：删除对象属性的方法=

"""


# 類定義
class Category:  # 類名
    name = "張三"  # 屬性名

    def un_date_name(self, name):  # 方法名
        self.name = name


# 類的屬性
# Python語言中，屬性分為類級別和實例級別兩種。實例級別的屬性值默認共享類級別的屬性值。除非顯式進行賦值操作。

class A:
    age = 10


obj2 = A()
obj3 = A()


class People:  # 類的內部定義的類，主要目的是為了更好抽象現實世界。
    code = 0

    class Father:
        code = 1

    class Mother:
        code = 2


class World:

    # 魔術方法
    # 在Python語言中，所有以雙下划線“__”包起來的方法，都統稱為“魔術方法”。
    # 這些方法在實例化時會自動調用，
    # 比如“_str__()”、“__init__()”、“__del__()”等。
    # 使用魔術方法可以構造出非常優美的代碼，比如將復雜的邏輯封裝成簡單的API等。

    name = "人"

    def __init__(self, n="非洲人"):
        self.name = n
        print("我是構造函數", self.name)

    def __del__(self):
        print("我是析構函數", self.name)


def func():

    print(obj2.age, obj3.age, A.age)
    obj2.age += 2
    print(obj2.age, obj3.age, A.age)
    A.age += 3
    print(obj2.age, obj3.age, A.age)

    family = People()
    father = family.Father()
    print(father.code)
    mother = People.Mother()
    print(mother.code)

    world = World()
    west_side = World("歐美人")
    world.__del__()  # 調用析構函數
    print(world)
    del world
