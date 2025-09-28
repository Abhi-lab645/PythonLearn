# 😎😎 Introduction to Tuples 😎😎

# Explanation:

"""
Tuples are ordered collections of items that are immutable.They are similar to Lists,
but their immutability makes them different.
"""

# 😎😎 Creating a tuple 😎😎

empty_tuple=()

print(empty_tuple)

print(type(empty_tuple))

lst=list()

print(lst,type(lst))

tpl=tuple()

print(tpl,type(tpl))

numbers=tuple([1,2,3,4,5,6])

print(numbers)

num_lst=list((1,3,4,6,7))

print(num_lst)

mixed_tuple=(1,"Hello",2.3,True)

print(mixed_tuple)

# 😎😎 Accessing Tuple Elements 😎😎

nums=(1,2,4,5,7,8,9,10)

print(nums[0])

print(nums[-1])

print(nums[0:4])

print(nums[::2])

print(nums[::-1])

# 😎😎 Tuples Operations 😎😎

nums1=(1,2,3,4,5)

nums2=(2,"Hello",3.5,True)

concatenation_tuple=nums1+nums2

print(concatenation_tuple)

print(nums2*3)

print(nums1*3)

# 😎😎 Immutable Nature of Tuples 😎😎

"""
Tuples are immutable,meaning their elements cannot be changed once assigned.
"""

lst1=[1,2,3,4,5]

print(lst1)

lst1[1]="Abhinav"

print(lst1)

nums3=(2,5,6,3,8)

print(nums3)

# nums3[1]="Abhinav"

# print(nums3) ## 😭😭TypeError: 'tuple' object does not support item assignment😭😭

# 😈😈 Tuples Methods 😈😈

nums4=(2,3,4,5,6,7,3,3,3)

print(nums4.count(2))
print(nums4.count(3))

print(nums4.index(5)) # it tells index of element

# 😈😈 Packing and Unpacking Tuple😈😈

# Packing

packed_tuple=1,"Hello",3.14

print(packed_tuple)

# Unpacking a tuple

a,b,c=packed_tuple

print(a)
print(b)
print(c)

# Unpacking with *

nums6=(1,2,3,4,5,6)
first,*middle,last=nums6

print(first)
print(middle)
print(last)

# 😈😈 Nested Tuple 😈😈

# 😈😈 Nested List😈😈

lst2=[[1,2,3,4],[6,7,8],[10,'Hello',True,23]]

print(lst2)
print(lst2[2][1])

# for i in lst2:
#     print(i)
#     for j in i:
#         print(j)

print(lst2[2][1:]) ## slicing operation in nested list

lst3=[(1,3.14,3,5),[56,"Hello",True],(20,10,True)]

print(lst3[2][2])


print(lst3[0][1:])

nested_tuple=((1,2,3),("a","b","c"),(True,False))

# 😈😈 Access the elements inside a tuple 😈😈

print(nested_tuple[0])

print(nested_tuple[2][1])

print(nested_tuple[1][1:])

# 😈😈 Iterating over nested tuples 😈😈

for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item,end=" ")
    print()    




