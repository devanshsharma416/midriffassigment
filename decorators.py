# # # def add(x):
# # #     def add_more(y): 
# # #         return x + y
# # #     return add_more

# # # add_15 = add(15)
# # # print(add_15(10))

# # # def func(a):
# # #     yield a
# # # a=[1,2,3]
 
# # # b=func(a)
# # # print(next(b))

# # # # 
# # # from _typeshed import OpenTextModeReading


# # data1 = ""
# # data2 = ""

# # with open("text2.txt", 'r') as df1:
# #     data1 = df1.read()

# # with open("text3.txt", 'r') as df2:
# #     data2 = df2.read()

# # data1 = data1 + "\n"
# # data1 = data1 + data2

# # with open("text4.py", "w") as fp:
# #     fp.write(data1)
# # flag = False
# # def prime(num):
    
# #     if num>1:
# #         for i in range(2, num):
# #             if num % i == 0:
# #                 flag = True
# #                 break
# #     return num
# # a = prime(11)
# # if flag:
# #     print(a, "is not prime")
# # else:
# #     print(a, "is prime")

# # def outer(new):
# #     def inner():
# #         print("I am a inner method")
# #         new()
# #     return inner

# # @outer
# # def outermost():
# #     print("I am most outer method")

# # outermost()
# # # a()


# # def substract(func):
# #     def inner(a, b):
# #         if a<b:
# #             a,b = b, a
# #         return func(a,b)
# #     return inner

# # @substract
# # def newfunc(a,b):
# #     print(a-b)

# # # newfunc = substract(newfunc)
# # newfunc(10, 15)


# def star(func):
#     def inner(*args, **kwargs):
#         print('*' * 30)
#         func(*args, **kwargs)
#         print('*' * 30)
#     return inner

# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 30)
#         func(*args, **kwargs)
#         print('%' * 30)
#     return inner

# @star
# @percent
# def printer(msg):
#     print(msg)

# printer("hello")

# # def uppercase(func):
# #     def inner(msg):
# #         new_msg = msg.lower()
# #         func(new_msg)
# #         return new_msg
# #     return inner
# # @uppercase
# # def msg_function(msg):
# #     print(msg)

# # # msg_function = uppercase(msg_function)
# # msg_function("TODAY IS MY BEST DAY")

# # def greets(text):
# #     return "Hello Devansh"

# # def hi(text):
# #     return "Hello Arpita"

# # def myname(func):
# #     a = func("Hello there")
# #     return a 

# # print(myname(hi))


 
# decorated_function = decorator(some_random_function)
