# Python程序的注释
在编程中，随着项目体量的增加，代码几乎不可避免地变得繁琐和难以理解，尤其是多人大型项目中这种情况尤其明显。需要使用自然语言（也就是中文、英文这种语言）来进行解释，这就是注释。
这里来介绍Python程序中的注释，直接上代码：

```python
print("我们在这个程序中会介绍Python中的注释。")
print("就像这样: ") # 这是一个注释
print("在注释外的代码会运行")
# print("而注释内的代码不会运行")
"""
多
行
注
释
"""
print("Yeah!")
```

## 代码讲解
在Python中，我们使用`#`进行注释，有时也会使用多行注释`"""`进行文档的书写。

# Python中的变量
变量的概念来源于数学，是计算机语言中能储存计算结果或能表示值的抽象概念。
变量可以通过变量名访问。

在Python中，普通变量有以下类型：
- int: 整数类型
- float: 浮点数（即小数）类型
- str: 字符串
- bool: 布尔型（真或假）
- list: 列表
- dict: 字典
- tuple: 元组
- set: 集合
- NoneType: 空类型，表示“什么都没有”

代码：
```python
# 这个程序会介绍Python中基本的变量
a_number = 3 # 这是一个整数
print(type(a_number)) # 会输出 <class 'int'>，代表整数
a_float = 3.14 # 这是一个浮点数（小数）
print(type(a_float))
a_boolean = True # 这是一个布尔类型，代表True(真)或False(假)
print(type(a_boolean)) # 会输出 <class 'bool'>
a_list = list()
print(type(a_list))

print(isinstance(a_number, int))
```

输出：
```
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'list'>
True
```

## 代码讲解
在Python中，type(some_variable)函数用来判断变量的类型，
而isinstance(some_variable, some_type)用来判断一个变量是否属于一个类型，并返回布尔值。

# 小练习
不运行以下代码，猜想会输出什么结果
```python
a = 3
b = 3.0
print(type(b))
print(type(a + b))
print(isinstance(a + b, int))
print(isinstance(a + b, float))
```
