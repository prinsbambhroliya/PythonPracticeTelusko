#61.Abstract Class And Abstrct Method

# from abc import ABC,abstractmethod

# class computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass

# class laptop(computer):
#     def process(self):
#         print("its running")

# # com = computer()
# com1 = laptop()
# # com.process()
# com1.process()

#61.B Iterator
# nums = [7,8,9,0,1]

# it = iter(nums)

# print(it.__next__())
# print(it.__next__())

# print(next(it))

# for i in nums:
#     print(i)

# class TopTen:

#     def __init__(self):
#         self.num = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.num <=10:
#             val = self.num
#             self.num +=1
#             return val
#         else:
#             raise StopIteration

# values = TopTen()
# print(next(values))
# print(next(values))

# for i in values:
#     print(i)

# 63.Exception Handling in Python
# a=5
# b=0

# try:
#     print("resource open")
#     print(a/b)

    
# except ZeroDivisionError as e:
#     print("hey,  zero Division Error Found...")
#     print(e)

# except ValueError as e:
#     print("Value Error Found----")
#     print(e)

# except Exception as e:
#     print("hey, you can not divide a number by zero----",e)
#     print(e)

# finally:
#     print("resource closed")

# 64. Multi Threading
# from time import sleep
# from threading import *

# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(1)

# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hii")
#             sleep(1)

# t1 = Hello()
# t2 = Hi()

# t1.start()
# sleep(0.2)  #2 second gap
# t2.start()

# t1.join()
# t2.join()
# print("Bye")

# 65. File Handling

# f = open('MyData.txt','r')
# print(f.readline(),end="#")
# print(f.readline())


# a = open('abc','w')
# a.write("Something Will be good very good")
# a = open('abc','+a')

# a.write("Mobile")

# for data in f:
#     print(data)

f = open('prince.jpg','rb')
f1 = open('myphoto.jpg','wb')
for i in f:
    f1.write(i)

