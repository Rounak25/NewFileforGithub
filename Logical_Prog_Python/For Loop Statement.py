# Road Maps of For Loop
# for <variable> in <sequence(List,string,tuple)>:
#    # body_of_loop that has set of statements
#    # which requires repeated execution

#############################
# 1st For loop example

# First simple program
# a = [1,2,3,4,5]
# #i = 0
# for val in a:
#     print(val)
#     #i = i + 1


# Second simple program

# num = [0,1,2,3,4,5]
# sum=0
# for val in num:
#     sum=sum+val
# print("Total is ",+sum)


############################################################
"""Program for FOR loop"""

# sum = [0,1,2,3,4]
# num=0
# for a in sum:
#     print(num)
#     num = num + 1

# For using Range
# for i in range(10):
#     print (i+1)

# for i in "Datacamp":
#     if i == 'a':
#         print (i)

# for i in range(1,20,2):
#     print (i)
##########################

# Square of numbers
# num = [1,2,3,4,5]
# a = 0 # in place of "int a" we are using "a=0" for python
# #for val in num:
# #a = num * num
# print(a**num)


# a="Hello"
# b="World"
# print(a+b)
#
# nums = [11,12,13,14,15]
# num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Original list of integers:")
# print(nums+num1)
#
nums = [11,12,13,14,15]
num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[4]**num1[2])
#
# num = [1,2,3,4,5,6,7]
# for i in num:
#     print(i**2)
#
# import numpy as np
# a = [2 ,3, 4]
# np.square(a)


num = [1,2,3,4,5,6]
print([num[0]**2,num[1]**2,num[2]**2,num[3]**2,num[4]**2,num[5]**2])

# num = [1,2,3,4,5,6]
# for i in num:
#     print (pow(i,2))
#
pow2 = [2 ** x for x in range(10)]
print(pow2)

# pow = []
# for x in range(10):
#    pow.append(2 ** x)

#############################

# some more for example

# Python program to illustrate
# Iterating over a list
# print("List Iteration")
# l = ["geeks", "for", "geeks"]
# for i in l:
#     print(i)
#
# # Iterating over a tuple (immutable)
# print("\nTuple Iteration")
# t = ("geeks", "for", "geeks")
# for i in t:
#     print(i)

# # Iterating over a String
# print("\nString Iteration")
# s = "Geeks"
# for i in s:
#     print(i)
#
# # Iterating over dictionary
# print("\nDictionary Iteration")
# d = dict()
# d['xyz'] = 123
# d['abc'] = 345
# for i in d:
#     print("%s  %d" % (i, d[i]))
#
# # Python program to illustrate
# # nested for loops in Python
#
# # from __future__ import print_function
# #
# # for i in range(1, 5):
# #     for j in range(i):
# #         print(i, end=' ')
# #     print()
#
# # Prints all letters except 'e' and 's'
# for letter in 'geeksforgeeks':
#     if letter == 'e' or letter == 's':
#         continue
#     print('Current Letter :', letter)
#
# # Python program to illustrate
# # Iterating over range 0 to n-1
#
# n = 4
# for i in range(0, n):
#     print(i)
#
#
# # Python program to illustrate
# # Single statement while block
# count = 0
# while (count == 0): print("Hello Geek")
#
# #Python program to illustrate
# # combining else with while
# count = 0
# while (count < 3):
# 	count = count + 1
# 	print("Hello Geek")
# else:
# 	print("In Else Block")
#####################################################################

# num =int(input("Enter any number"))
# print(num)