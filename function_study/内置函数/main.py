# eval() 执行一个字符串表达式
x = 7
a = eval("3 * x")
print(a)

# exec() 类似与eval() 
exec("print('asd')")

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象
def is_odd(n):
    return n % 2 == 1
 
tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)

# input() 函数接受一个标准输入数据，返回为 string 类型

# next() 返回迭代器的下一个项目。

# next() 函数要和生成迭代器的 iter() 函数一起使用

# repr() 函数将对象转化为供解释器读取的形式。





