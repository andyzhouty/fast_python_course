# 变量类型的转换

在前面一章中，我们介绍了Python中的变量，我们现在来学习变量之间的转换：

```
a_number = 3
a_string = "4"
the_string = str(a_number) # 用str函数可以把一个变量变成字符串
the_number = int(a_string) # 用int函数可以把一个变量编程整数

a_float = 3.5
the_number = int(a_float) # 这里会把3.5自动去尾，不是四舍五入
```

这是一个简单的例子，`str(some_variable)`可以把一个变量变成字符串类型，

而`int(some_variable)`可以把一个变量变成整数类型 ，对于字符串，int()会自动检查它的内容，如果是类似于"4" "-10000"这样的字符串就可以通过，如果是类似于"abcd"这样的字符串就会报Error；而对于浮点数，int()会自动执行去尾法，去除小数部分，比如int(3.99)的值是3而不是4。

上面已经提到了，类型转换可能会报Error，因为不是所有的变量都能强制转换为另一个类型的。
布尔值

为了纪念19世纪的数学家George Boole，编程语言中的真假两个值用布尔（bool）类型表示。

布尔值可以是一个表达式，也可以单独给它一个值。Python会把0这个整数、""空字符串、[]空列表、None空值和False视为假值，其他值都是真值。以下是Python交互环境下的示例

```
>>> bool(0) # 0值
False
>>> bool("") # 空字符串
False
>>> bool([]) # 空列表
False
>>> bool(()) # 空元组
False
>>> bool({}) # 空字典
False
>>> bool(set()) # 空集
False
```

# 获取用户输入

不像C/C++等语言，Python提供的获取用户输入的函数非常简单、易于使用：

```python
username = input("Who are you? ")
print("You are" + username + ".")
```

运行结果（<>内容为用户输入，可以替换为你自己的姓名）：

```
Who are you? <Nobody>
You are <Nobody>.
```

在Python中我们使用+来进行字符串的拼接。

我们还可以用刚学过的知识来对用户输入进行一些处理：

```python
age = int(input("How old are you? "))
print("You are " + str(age) + " years old.")
```

运行结果：

```
How old are you? <14>
You are <14> years old.
```

输入有误时：

```
How old are you? <fourteen>
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '<fourteen>'
```

这说明Python无法对字符串`"<fourteen>"`或不完全由数字组成的字符串进行强制转换，我们在之后的章节会学习如何进行错误处理。

# 格式化字符串

> 注：“格式化”在这里并不是删除、清空的意思。如果是初学者，不要见到“格式化”就害怕，认为是格式化磁盘的那个“格式化”。

在上个例子中，有这样一行代码：

```python
print("You are " + str(age) + " years old.")
```

这显得很烦，对不对？格式化字符串力图解决这样的问题

在C/C++, Go等语言中，格式化字符串只能长成这样（这里我用Go写个示例）：

```go
fmt.Println("Your age %d", age)
```

Python也支持这种，只不过是这样：

```python
age = 14
print("My age: %d" % age)
```

看起来比刚才简洁多了。

但是，在Python中还可以更简洁，Python引入了`format()`：

```python
age = 14
print("My age: {}".format(age))
# 等价于
print("My age: {age}".format(age=age))
```

好像还没有上一个简洁，但是它确实更有可读性。

于是乎，在Python 3.6中，我们引入了`f""`（也被称为f-string）。好家伙，现在可以这样写：

```python
age = 14
print(f"My age: {age}")
```

是不是舒服多了？（这也就是为什么我们教程推荐使用Python 3.6及以上的Python版本的原因）

Python没有止步于此，Python 3.8中又引入了新的f-string功能，便于调试：

```python
x = 100
print(f"{x=}")
```

输出：

```
x=100
```

当然，f-string有其缺点，这一个缺点我在Flog的开发中记忆尤其深刻，这迫使我使用format()函数，等到那一章时我会提到这点。

我们来用f-string来改写上一节的程序：

```python
age = int(input("How old are you? "))
print(f"You are {age} years old.")
```

# 小练习

把询问年龄的程序改为询问身高（单位：米，用户不需要输入单位），并输出

提示：如果要求使用米作单位的话，用int整数类型好像不太合适 ，那么应该用什么？请参考[上一章节](../ex2/ch2.md)的变量类型表

