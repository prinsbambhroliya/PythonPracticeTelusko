# import math
# x = int(input("Enter a number1: "))
#
# y = int(input("Enter a number2: "))
# z = x+y
# print(z)
# ch = input("enter a char")[0]
# print(ch)

# import sys
# result = input("Enter the you want to find cube")
# result = int(sys.argv("Enter the no. you want to find cube"))
# print(int(result)**3)
# i=1
# while i<=10:
#     print("Prince ",end="")
#     j=1
#     while j<= 4:
#         print(j,end="")
#         j+=1
#     i+=1
#     print()
# i=1
# for i in range(1,101):
#     if(i%3==0 or i%5==0 ):
#         continue
#     else:
#         print(i)

# For Printing the '#' pattern
# i=1
# while i<5:
#     print("# ", end="")
#     i=i+1
#     j=1
#     while j<5:
#         print("# ", end="")
#         j=j+1
#     print()

# num = int(input("Enter a number: "))
# if(num%2==0):
#     print(num,"is even")
# else:
#     print(num,"is odd")

#22.Fibonacci Problem
# Program to display the Fibonacci sequence up to n-th term
#
# nterms = int(input("How many terms? "))
#
# # first two terms
# n1, n2 = 0, 1
# count = 0
#
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1

#23.Pattern
#
# #
# # #
# # # #
# n=4
# for i in range(4):
#     for j in range(i,4):
#         print(j+1,end=" ")
#     print()


#APQR
#ABQR
#ABCR
#ABCD

# a="ABCD"
# b="PQR"
# for i in range (4):
#     for j in range (3):
#         print(a[0:i+1],end="")
#         print(b[i:j+3],end="")
#         break
#     print()

# num = 10
# for i in range (2,int(num/2)):
#     if num%i ==0:
#         print("not prime")
#         break
# else:
#     print("prime")
#
# from array import *
# vals = array('i',[5,6,7,8,9])
# print(vals)
# print(vals.buffer_info())
# newArr = array(vals.typecode,(a*a for a in vals))
# for e in newArr:
#     print(e)
#

# from array import *
# arr = array('i',[])
# n = int(input("Enter The length of the array: "))
#
# for i in range(n):
#     x = int(input("Enter The next value in the array: "))
#     arr.append(x)
# print(arr)
# search = int(input("Enter The Value for search: "))
# k = 0
# for e in arr:
#     if e == search:
#         print("Element is at index:",k)
#         break
#     k += 1
#
# print(arr.index(search))

# 27.1) Create an array with 5 values & delete the value at index no. 2 without using in-built function.
# #To create array with 5 elements and delete element with index value 2:
# from array import *
# arr = array('i',[])
#
# len = int(input("Enter length of array:"))
#
# for i in range(len):
#     ele = int(input("Enter elements:"))
#     arr.append(ele)
# print(arr)
#
# for d in range(len):
#     if d == 2:
#         arr.pop(d)
# print(arr)
# #       OR
# for d in range(len):
#     if d == 2:
#         del arr[2]
# print(arr)

# Reversing array:
# from array import *
# arr = array('u',['a','b','c','d'])
# len = len(arr)
#
# for i in range(int(len/2)):
#     temp = arr[i]
#     arr[i] = arr[len-i-1]
#     arr[len-i-1] = temp
# print("The reversed array is:",arr)

# Creating new array with reversing of existing array:
from array import *

arr = array('u',['a','b','c','d'])
len = len(arr)
arr1 = array(arr.typecode,[])
i = 1
while i <= len:
    arr1.append(arr[4-i])
    i+=1
print(arr1)
