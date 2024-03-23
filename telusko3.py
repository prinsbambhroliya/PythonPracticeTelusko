# def greet():
#     print("hello Namaste India")
# greet()
#
# def add(a,b):
#      print(a+b)
# add(6,7)


# keyword
# def person(name, **data):
#     print(name)
#     print(data)
# person('prins',age=20,city='San Francisco',mob=10101010101)
# Global Keyword
# a=10
# b=9
# def glob():
#     global a
#     a = 15
#     print(a)
#     #for accessing only global variable
#     x= globals()['b']
#     print(x)
# glob()


# Pass List to Function
# def count(lst):
#     even = 0
#     odd = 0
#     for i in lst:
#         if (i % 2 == 0):
#             even += 1
#         else:
#             odd += 1
#
#     return even, odd
#
#
# lst = [12, 34, 5, 6, 7, 8, 9, 10, 11]
# even, odd = count(lst)
# print(even, odd)

# 37.Assignment
# take 10 names from user and display how many has more than 5 latter in names
# names = ['Prins', 'Virat', 'Mahi','Rohit','Ravindra','Shubhaman','MdShami','Hardik','Mitchel','Maxwell']
# print(names)
# more = []
# less = []
# for name in names:
#     if(len(name) <= 5):
#         less.append(name)
#     else:
#         more.append(name)
#
# print(less)
# print(more)

#Fibonacci Series
# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     elif n <= 0 :
#         print("Invalid input")
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             fib = a + b
#             a = b
#             b = fib
#             print(fib)
#
# n=int(input('Please type the no. of values-'))
# fib(n)

#Factorial Number

# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f =f*i
#
#     return f
# x = 5
# result = fact(x)
# print(result)

# Recursion

# import sys
# sys.setrecursionlimit(1990)
# print(sys.getrecursionlimit())
# i=0
# def greet():
#     global i
#     i+=1
#     print("Hello",i)
#     greet()
# greet()

#Factorial Using Recursion
#
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
#
# result = fact(5)
# print(result)

# def square(a):
#     return a*a
#
# result = square(5)
# print(result)

# f = lambda a,b: a * b
# result = f(5,6)
# print(result)
#
# nums = [3,6,4,9,7,8,5,2,1,9]
# # def is_even(n):
# #         return n % 2 == 0
# # evens = list(filter(is_even, nums))
#
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)
# doubles = list(map(lambda n: n*2, nums))
# print(doubles)
#
#
# from functools import reduce
# sum = reduce(lambda x, y: x+y, nums)
# print(sum)

def div(a,b):
    print(a/b)
def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div1 = smart_div(div)

div1(2,4)

