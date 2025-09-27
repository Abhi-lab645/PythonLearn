# 😎😎 Dictionaries 😎😎

"""
Dictionaries are unordered collections of items.They store data in key-value pairs.keys must be 
unique and immutable (eg: strings,numbers, or tuples), while values can be of any type.
"""

# 😎😎 Creating Dictionaries 😎😎

empty_dic={}
print(type(empty_dic))

empty_dic1=dict()
print(empty_dic1)

student={
    "name":"Abhinav",
    "age":20,
    "grade":10
}

print(student)

# 😎😎 Single key is always used 😎😎

student1={
    "name":"Abhinav",
    "age":20,
    "grade":10,
    "name":24
}

print(student1)

# 😎😎 Accessing Dictionary Elements 😎😎

student3={
    "name":"Golu",
    "branch":"CSE",
    "age":20,
    "marks":{
        "maths":97,
        "science":98,
        "sst":93,
        "english":92,
        "sanskrit":97
    }
}

print(student3)

print(student3["marks"])

"""

for subject,mark in student3["marks"].items():
    print(f"{subject}:{mark}")

def cal_percentage(score):
    obtained_marks=0
    for subject,mark in score.items():
        obtained_marks+=mark
    
    percentage=(obtained_marks*100)/500

    return percentage

result=cal_percentage(student3["marks"])

print(result)

"""

print(student3["name"])

print(student3["age"])

# 😎😎 Accessing using get() method 😎😎

print(student3.get("marks"))

print(student3.get("branch"))

print(student3.get("address"))

print(student3.get("father_name","Not available"))

# 😎😎 Modifying Dictionary Elements 😎😎

# Dictionary are mutable,so you can add,update or delete elements

student4={
    "name":"Apish",
    "branch":"CSE",
    "address":"Haryana",
    "color":"fair",
    "semester":1,
    "age":18
}


print(student4)

student4["semester"]=3 ## update value for the key

print(student4)

student4["College"]="NST" ## Added a new key and value

print(student4)

del student4["color"] ## delete key and value pair

print(student4)

# 😎😎 Dictionary Methods😎😎

keys=student4.keys() ## get all the keys

print(keys)

values=student4.values() ## get all the values

print(values)

items=student4.items() ## get all key value pairs 

print(items)

# 😎😎 Shallow Copy😎😎

student4_copy=student4

print(student4_copy)

student4["name"]="Krishav"

print(student4)

print(student4_copy)

student4_copy1=student4.copy() ## Shallow copy

print(student4_copy1)

print(student4)

student4["name"]="Shivam"

print(student4)

print(student4_copy1)

# 😎😎 Iterating Over Dictionaries 😎😎
# 😎😎 You can use loops to iterate over dictionaries,keys,values,or items😎😎

#😎😎 Iterating over keys 😎😎

student5={
    "name":"Abhinav",
    "address":"Bangalore",
    "Branch":"CSE",
    "age":20,
    "occupation":"CEO",
    "birth_year":2005
}

print(student5)

for key in student5.keys():
    print(key)

# 😎😎 Iterate over values 😎😎

for value in student5.values():
    print(value)

# 😎😎 Iterate over key value pairs  😎😎

for key,value in student5.items():
    print(f"{key}:{value}")

