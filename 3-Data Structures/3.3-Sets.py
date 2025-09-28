# ❤️❤️ Sets❤️❤️

# Create  a set

# my_set={1,2,3,4,5}

# print(my_set)

# print(type(my_set))

# my_empty_set=set()

# print(type(my_empty_set))

# set1=set([1,2,3,4,5])

# print(set1)

# set2=set([1,2,2,3,3,4,5])

# print(set2)

# 👀 👀  Basic Sets Operation 👀 👀

# 😜😜 Adding and Removing elements😜😜
"""
set3=set([3,4,5,6,7,8,9])

set3.add(10)

print(set3)

set3.add(10)

print(set3)

"""

# ✌🏼✌🏼 Removing the elements from a set✌🏼✌🏼

set4={3,2,5,6,0,8}

set4.remove(3)

print(set4)

# set4.remove(11)

# Give KeyError: 11

# print(set4)

set4.discard(11)

print(set4)


# ☺️☺️ pop method☺️☺️

removed_element=set4.pop()
print(removed_element)
print(set4)


# 😎😎 clear all the elements 😎😎

set4.clear()
print(set4)

# 😎😎 Set Membership test 😎😎

set5={1,2,3,4,5}

print(3 in set5)

print(10 in set5)

# 😎😎 Mathematical Operation😎😎

set6={1,2,3,4,5,6}
set7={4,5,6,7,8,9}

# 😎 Union 😎

union_set=set6.union(set7)

print(union_set)

# 😎 Intersection 😎

intersection_set=set6.intersection(set7)

print(intersection_set)

# set6.intersection_update(set7)

# print(set6)

# 😎 Difference 😎

set8={1,2,3,4,5,6}
set9={4,5,6,7,8,9}

print(set8.difference(set9))

# set8.difference_update(set9)

# print(set8)

print(set9.difference(set8))

# 😎 Symmetric Difference 😎

print(set8.symmetric_difference(set9))

# 😎 Sets Methods😎

set10={1,2,3,4,5}
set11={3,4,5}

# 😎😎 is subset 😎😎

print(set10.issubset(set11))

print(set10.issuperset(set11))

lt=[1,2,2,3,4,4,5]
set12=set(lt)
print(set12)

# 😎😎 Counting Unique words in text 😎😎

text="In this tutorial we are discussing about sets"

words=text.split()

print(words)

# Convert list of words to set to get unique words

unique_word_set=set(words)

print(unique_word_set)

print(len(unique_word_set))







