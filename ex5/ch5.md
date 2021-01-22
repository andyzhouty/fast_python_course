本来这一章节要放到之后讲完`import`再写的，但是为了使本教程有一定实用价值，决定提前现在发布

# 四则运算和指数运算

Python的四则运算非常简单，这里用Python交互式环境演示一下。

`+`为加法，`-`为减法，`*`为乘法，`/`为除法，`()`为括号。

同四则运算一样，`()`优先级最高，`*`和`/`其次，`+`和`-`最低

> 注意在Python中四则运算只有小括号，没有[]和{}

```
>>> 1 + 1
2
>>> 1 - 1
0
>>> 9 * 9
81
>>> 9 / 3
3.0
>>> 5 / 2
2.5
>>> 5 / 0 # 除零错误
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> (3 * (1 + 3 * 3)) * 9
270
```

## 指数运算

Python中的指数运算表示为`x ** y`表示x的y次方，优先级低于括号而高于乘除。

```
>>> 2 ** 3
8
>>> 3 ** 10
59049
>>> 3 ** 2.5
15.588457268119896
```

## 求余与整除运算

Python中求余运算表示为`x % y`，返回x除以y的余数。

整除运算是`x // y`，相当于`(x - x % y) / y`。

如果还是看不懂，那么我再解释一下：

假设x除以y等于a余b，那么`x % y`返回b，`x // y`返回a

> 注：这里%和百分数没有关系

```
>>> 5 % 2 # 5除以2余1
1
>>> 5 // 2 # 5除以2去除余数后是2
2
```

## 虚数

Python提供了对虚数运算的支持。在Python中，虚数用`j`而非常见的`i`来表示，`j`相当于`i`：

```
>>> 3j ** 2
-9
>>> (3j + 1) ** 2
(-8+6j)
```

# Python的数学运算库

Python中有专门的数学运算库名为`math`，需要用`import`来导入，这个库提供了一系列数学运算的工具：

```
>>> import math
>>> math.pi # 输出pi（就是3.1415926...)的值
3.141592653589793
>>> math.e # 输出e的值
2.718281828459045
>>> math.sqrt(4)
2.0
>>> math.sqrt(-1) # sqrt只能接受非负实数
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
```

想单独引入`sqrt`还可以写为`from math import sqrt`


# 用Python解数学题——例题

![sample_math_problem.svg](./sample_math_problem.svg)
```python
from math import sqrt, floor

x = sqrt(19 - 8 * sqrt(3))
a = floor(x) # x的整数部分
b = x - a

print(a + b + 1 / b)
```
输出：
```
5.999999999999998
```

由于计算机使用二进制存储数据，一些误差难以避免，但是答案已经非常接近正确答案6了，可以说符合要求。

# 小练习
请用Python解决以下问题：
![homework_math_problem.svg](./homework_math_problem.svg)
