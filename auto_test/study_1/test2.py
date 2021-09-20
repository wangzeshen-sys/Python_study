import time
#####################################################################################3
# 函数装饰器
# def cal_time(func):
    
#     def cal_time_out():
#         start = time.time()
#         func()
#         end = time.time()
#         print(int(end - start)) 

#     return cal_time_out

# @cal_time
# def sum():
#     sum1 = 0
#     list1 = [1, 2, 3, 4, 5]
#     for i in list1:
#         sum1 += i
#         time.sleep(1)
    
#     print(sum1)

# sum()
######################################################################
# 类方法的函数装饰器

# def decorator(func):

#     def wrapper(me_instance):
#         start_time = time.time()
#         func(me_instance)
#         end_time = time.time()
#         print(int(end_time - start_time))

#     return wrapper

# class Method(object):

#     @decorator
#     def func(self):
#         for i in [1, 3, 4, 5]:
#             time.sleep(1)
# p1 = Method()
# p1.func()
# 对于类方法来说，都会有一个默认的参数self，它实际表示的是类的一个实例，所以在装饰器的内部函数wrapper也要传入一个参数 - me_instance就表示将类的实例p1传给wrapper，其他的用法都和函数装饰器相同。

#############################################################################################

# 类装饰器

# class Decorator(object):

    # def __init__(self, f):
    #     self.f = f

    # def __call__(self):
    #     start = time.time()
    #     self.f()
    #     end = time.time() 
    #     print(int(end-start))

# @Decorator
# def func():
    # for i in [1,2,3,4]:
    #     time.sleep(1)


# func()

# p = Decorator(func)
# p()

#######################################################################################

# 装饰器的先后顺序

# def makebold(f):
#     return lambda: "<b>" + f() + "</b>"

# def makeitalic(f):
#     return lambda: "<i>" + f() + "</i>"

# @makebold
# @makeitalic
# def say():
#     return "Hello"

# print(say())

# 多个装饰器的执行顺序：是从近到远依次执行























