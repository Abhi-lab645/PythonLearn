# Lambda Function in python

"""
Lambda functions are small anonymous functions
defined using the lambda keyword.They can have 
any number of arguments but only one expression.
They are commonly used for short operations or as
arguments to higher-order functions.
"""

# def add(a,b):
#     return a+b
# print(add(2,3))


# mul=lambda a,b:a*b

# print(type(mul))

# print(mul(2,3))


# def is_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False
    
# print(is_even(14))


# even=lambda num:num%2==0

# print(even(11))
# print(even(12))


# def addition(x,y,z):
#     return x+y+z

# print(addition(2,5,8))


# add1=lambda x,y,z:x+y+z

# print(add1(2,3,4))

# 😍😍 map() -> Applies a function to all items in a list😍😍

# numbers=[1,2,3,4,5,6]

# squared_num=[i**2 for i in numbers]

# print(squared_num)


number1=[3,4,5,6,10]

sqr_num=list(map(lambda x:x**2,number1))

print(sqr_num)




