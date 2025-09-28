"""
fruits=["apple","banana","guava","strawberry","grapes"]
print(fruits)

# Remove and return the last element
popped_fruit=fruits.pop()

print(popped_fruit)

print(fruits)

fruit_index=fruits.index("banana")

print(fruit_index)

fruits.insert(1,"banana")
print(fruits)

count_num=fruits.count("banana")

print(count_num)

# sorts the list in ascending order
fruits.sort() 

print(fruits)

# Reverse the list
fruits.reverse()

print(fruits)

#Remove all items from the list
fruits.clear()

print(fruits)

"""

"""
# Slicing List

numbers=[1,2,3,4,5,6,7,8,9,10]

print(numbers[2:5])

print(numbers[:5])

print(numbers[5:])

print(numbers[::2])

print(numbers[::-1])

print(numbers[::])

print(numbers[::1])

print(numbers[::3])

print(numbers[::-2])

"""

"""
# Iterating Over List

names=["Abhinav","Shivam","Krishav","Rahul","Krishna","Aman"]

# for name in names:
#     print(f"{names.index(name)+1}:{name}")

for index,nam in enumerate(names):
    print(f"{index+1}:{nam}")

"""

# List comprehension

# ls=[]
# for x in range(10):
#     ls.append(x**2)

# print(ls)

# lst=[x**2 for x in range(10)]

# print(lst)

# 😍😍 List Comprehension😍😍

#  Basic Syntax            [expression for item in iterable]

#  With Conditional logic  [expression for item in iterable if condition]

# Nested List Comprehension [expression for item1 in iterable1 for item2 in iterable2]

#  Basic List Comprehension

# square=[num**2 for num in range(10)]

# print(square)

# List Comprehension with Condition

# even_n=[]

# for num in range(1,11):
#     if num%2==0:
#         even_n.append(num)
# print(even_n)

# even_num=[i for i in range(1,11) if i%2==0]

# print(even_num)


# ❤️❤️Nested List Comphrension❤️❤️

# lst1=[1,2,3,4]
# lst2=["a","b","c","d"]
# combine=[]

# for i in lst1:
#     for j in lst2:
#         combine.append([i,j])

# print(combine)



# pair=[[i,j] for i in lst1 for j in lst2]

# print(pair)

# 💕💕 List Comprehension with function calls💕💕

# words=["hello","world","python","list","comprehension"]

# lengths=[len(word) for word in words]

# print(lengths)