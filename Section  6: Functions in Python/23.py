# 😈😈 The filter() function in python 😈😈

"""
The filter() function constructs an iterator 
from elements of an iterable for which a function
returns true.It is used to filter out items from
a list (or any other iterable) based on a condition.
"""

def is_even(num):
    if num%2==0:
        return True
    else:
        return False
    
print(is_even(12))
print(is_even(11))

# num_lst=[1,2,3,4,5,6,7,8,9,10,11,12]
# ls=[]
# def even(lst):
#     for num in lst:
#         if num%2==0:
#             ls.append([num,True])
#         else:
#             ls.append([num,False])

# even(num_lst)
# print(ls)


lst1=[20,24,25,42,22,18,15,13]

lst2=list(filter(is_even,lst1))

print(lst2)

# 😈😈 Filter with a Lambda Function😈😈

nums1=[1,2,3,4,5,6,7,8,9,]

greater_than_five=list(filter(lambda x:x>5,nums1))

print(greater_than_five)

# 😈😈 Filter with a lambda function and multiple conditions😈😈

nums2=[10,15,20,25,30,35,40,4,6]

even_and_greater_than_five=list(filter(lambda x:x>5 and x%2==0,nums2))

print(even_and_greater_than_five)

# 😈😈 filter() to check if the age is grater than 25 in dictionaries 😈😈

people=[
    {'name':'Abhinav','age':26},
    {'name':'Shivam','age':28},
    {'name':'Apish','age':17},
    {'name':'Krishav','age':19}
]

def age_grater_than_25(person):
    return person['age']>25


person_age_greater_than_25=list(filter(age_grater_than_25,people))

print(person_age_greater_than_25)

# 😈😈😈😈    Conclusion.        😈😈😈😈

"""
The filter() function is a powerful tool for 
creating iterators that filter items out of an
iterable based on a function.it is commonly used 
for data cleaning,filtering objects,and removing
unwanted elements from lists.By mastering filter(),
you can write more concise and efficient code for 
processing and manipulating collections in python.

"""

