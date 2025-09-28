# 😎😎 The map() Function in python 😎😎
"""
 The map() function applies a given function
 to all items in an input list (or any other iterable)
 and returns a map object (an iterator).This is
 particularly useful for transforming data in a 
 list comprehensively. 
"""

def square(n):
    return n*n

numbers=[1,2,3,4,5]

squared_num=list(map(square,numbers))

print(squared_num)

# 😎😎 Lambda function with map 😎😎

number1=[2,5,7,10]

sqr_num=list(map(lambda x:x**2,number1))

print(sqr_num)

# 😎😎  map Multiple Iterables 😎😎

nums1=[1,2,3]
nums2=[4,5,6]

added_nums=list(map(lambda x,y:x+y,nums1,nums2))

print(added_nums)

# 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎

# 😎😎 map() to convert a list of strings to integers 😎😎

# use map() to convert strings to integers

str_numbers=["1","2","3","4","5"]

int_numbers=list(map(int,str_numbers))

print(int_numbers)

# 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎

words=['apple','banana','grapes','guava']

upper_words=list(map(lambda word:word.upper(),words))

print(upper_words)

# 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎 😎😎

def get_name(person):
    return person['name']

person={
    'name':'Abhinav',
    'age':20,
    'birth_year':2005,
    'address':'Bangalore',
    'branch':'CSE'
}

print(get_name(person))

people=[
    {'name':'Abhinav','age':20},
    {'name':'Shivam','age':19},
    {'name':'Apish','age':17},
    {'name':'Krishav','age':19}
]




people_name=list(map(get_name,people))

print(people_name)
