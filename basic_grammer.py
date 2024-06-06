# 縮進規則
# A、邏輯行的“首行”需要頂格，即無縮進（也就是一份源碼的第一個邏輯行）


class BasicGrammar:
    """
    二、代码缩进规则

    缩进是针对逻辑行的，因此首先要区分代码中的物理行和逻辑行。
    什么是物理行：代码在编辑器中显示的一行就是一个物理行。
    """


a = 1
b = 2
c = 3

# 例1: 該賦值語句,只是將對象書寫為多個物理行,對於python解釋器,它只是一條語句 一個邏輯行,等效於 s = {"a":1,"b":2,"c":3}
s = {
    "a": 1,
    "b": 2,
    "c": 3
}

# 例2: 該語句則是把一個邏輯行使用"\"書寫為多個物理行,其等效於：print("========\n===測試===\n========")
print("========\n===測試===\n========")

"""
":"标记一个新的逻辑层

如：while循环、if分支、函数声明、类定义等等:

增加缩进表示进入下一个代码层
减少缩进表示返回上一个代码层
"""

d = True

if d:
    d = 1
else:
    d = 2

e = 2

if e == 2:
    f = e
else:
    f = e + 1

f += 1

"""
缩进量及缩进字符

1、Python可以使用空格或制表符（tab符）标记缩进。缩进量（字符个数）不限。

A、空格和tab符通常都以空白形式显示，混用不容易区分，影响代码阅读，增加维护及调试的困难。 因此 Python PEP8 编码规范，指导使用4个空格作为缩进。

在这里插入图片描述

B、实际开发，代码规模较大，缩进深度的影响，会选择2个空格做为缩进，更易于阅读。
"""


def modify_incoming(list_arg):
    """修改傳入的列表"""
    list_arg.append([40, 50, 60])
    print("函數內修改后的變量：", list_arg)
    return list_arg


def describe_student(person_name, student_age='18'):
    """函數功能：顯示學生的信息"""
    print("my name is", person_name)
    print(person_name + " is " + student_age + " years old")


def enroll1(name, gender):
    """注冊學生的信息"""
    print("name:", name)
    print("gender:", gender)


def enroll2(name, gender, age='18', city='Beijing'):
    """注冊學生的信息"""
    print("name:", name)
    print("gender:", gender)
    print("age:", age)
    print("city:", city)


def list_add1(list1=[]):
    list1.append('END')
    return list1


def list_add2(list2=None):
    if list2 is None:
        list2 = []
    list2.append('END')
    return list2


def calculate1(numbers):
    sum_numbers = 0
    for n in numbers:
        sum_numbers = sum_numbers + n
    return sum_numbers


def calculate2(*numbers):
    sum_numbers = 0
    for n in numbers:
        sum_numbers = sum_numbers + n
    return sum_numbers


def enroll3(name, gender, *, age, city):
    print(name, gender, age, city)


def enroll4(name, gender, *, age='18', city):
    print(name, gender, age, city)


def parameter_combination(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)


def reverse(word):
    return word[::-1]


def get_lambda(arg2, arg3):
    return lambda arg1: arg1 + arg2 + arg3


def func():
    print(a, b, c, d, e, f)
    # 可以使用"\"對一個邏輯行進行換行，書寫為多個物理行。
    print("1111111111111111111111111111111111\
           2222222222222222222222222222222222")  # 換行
    print('pow2,4:' + str(pow(2, 4)), 'abs100:' + str(abs(100)), 'abs-10:' + str(abs(-10)), 'max1,2:' + str(max(1, 2)),
          'max-2,'
          '0,'
          '4,'
          '1:' + str(max(-2, 0, 4, 1)))  # 內建函數
    print("int('12'):", int('12'))
    print("int(12.3):", int(12.3))
    print("float('12.3'):", float('12.3'))
    print("str(1.23):", str(1.23))
    print("str(10):", str(10))
    print("bool(1):", bool(1))
    print("bool(''):", bool(''))
    g = abs
    print('g:' + str(g(-1)))
    list_arg = [10, 20, 30]
    modify_incoming(list_arg)
    print("函數外變量的值：", list_arg)
    # 位置參數
    # Python語言必須將函數調用中的每個實參都關聯到函數的相應形參。最簡單的關聯方式是基于實參的順序，這種關聯方式被稱為位置實參。
    describe_student('Jack', '24')
    describe_student('18', 'Black')
    describe_student('Tom')
    describe_student('Jerry', '18')
    # 默認參數
    # 編寫函數時，可給每個形參指定默認值。在調用函數時，如果給形參提供了實參，Python語言將使用指定的實參值；否則，將使用形參的默認值。給形參指定默認值后，可在函數調用中省略相應的實參。使用默認值可簡化函數調用，還可清楚地指出函數的典型用法。
    enroll1('Jack', 'F')
    enroll2('Sarah', 'F')
    print('-' * 70)
    enroll2('Sarah', 'M', '17')
    # 要注意的是，設置默認參數時，必選參數在前，默認參數在后，否則Python語言的解釋器會報錯。使用默認參數最大的好處是能降低調用函數的難度。編寫一個學生注冊的函數，需要傳入name和gender兩個參數。
    print(list_add1([1, 2, 3]))
    print(list_add1(['a', 'b', 'c']))
    print(list_add1())
    print(list_add1())
    print(list_add1())
    print(list_add2())
    print(list_add2())
    print(calculate1([1, 2, 3]))  # 結果是6
    print(calculate1([1, 2, 3, 4]))  # 結果是10
    print(calculate2())
    num = [1, 2, 3]
    print(calculate2(*num))
    enroll3('Jack', 'M', age='18', city='Beijing')
    enroll4('Jack', 'M', city='Beijing')  # 結果是：Jack M 18 Beijing
    # 定義的順序必須是：必選參數、默認參數、可變參數、命名關鍵字參數和關鍵字參數
    print(parameter_combination(1, 2))
    # 輸出結果：a= 1 b= 2 c= 0 args= () kw= {}
    print(parameter_combination(1, 2, c=3))
    # 輸出結果：a= 1 b= 2 c= 3 args= () kw= {}
    print(parameter_combination(1, 2, 3, 'a', 'b'))
    # 輸出結果：a= 1 b= 2 c= 3 args= ('a', 'b') kw= {}
    print(parameter_combination(1, 2, 3, 'a', 'b', x=4))
    # 輸出結果：a= 1 b= 2 c= 3 args= ('a', 'b') kw= {'x': 4}
    args = (1, 2, 3, 4)
    kw = {'x': 5}
    print(parameter_combination(*args, **kw))
    # 輸出結果：a= 1 b= 2 c= 3 args= (4,) kw= {'x': 5}

    # 高階函數
    # 接受函數為參數，或者把函數作為結果返回的函數稱為高階函數。例如，若要根據單詞的長度排序，只需把len函數傳給key參數。
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=len))
    print(reverse('testing'))
    print(sorted(fruits, key=reverse))

    # 匿名函數
    # 所謂匿名函數，即不再使用def語句這樣標准形式定義的函數。Python語言經常使用lambda來創建匿名函數。lambda 只是一個表達式，函數體比def定義的函數體要簡捷。
    """lambda [arg1[, arg2], ....argn]]:expression"""
    sum = get_lambda(2, 3)
    print(sum(1))
    # 上述代碼中，第一行定義了一個lambda函數，執行兩個數的和運算，並且把該lambda函數命名為sum。會面的代碼通過sum（）函數即實現了調用lambda函數的功能。

    