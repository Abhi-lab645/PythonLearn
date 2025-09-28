 # 😈😈 Example 1: Temperature Conversion 😈😈


# This function converts temperature between Celsius and Fahrenheit

"""
def convert_temperature(temp,unit):

    if unit=="C":
        return temp*9/5+32 # Celsius to Fahrenheit
    elif unit=="F":
        return (temp-32)*5/9 # Fahrenheit to celsius
    else:
        return None
    
print(convert_temperature(25,"C"))
print(convert_temperature(77,"F"))
    
"""

# 😈😈 Example 2:Password Strength Checker 😈😈

# password="strong123"

# res=not any(char.isdigit() for char in password)

# print(res)


"""
def is_strong_password(password):

    #This function checks if the password is strong or not

    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True

# Calling the function

print(is_strong_password("Weakpwd"))

print(is_strong_password("Str0ngpwd!"))

"""

# 🪴🪴 Example 3: Calculate the Total Cost of Items 
# in a Shopping Cart 🪴🪴

"""

def calculate_total_cost(cart):
    total_cost=0

    for item in cart:
        total_cost+=item['price']*item['quantity']
    
    return total_cost   

# Example cart data

cart=[
    {'name':'Apple','price':10,'quantity':3},
    {'name':'Banana','price':5,'quantity':8},
    {'name':'Orange','price':8,'quantity':5}
]

total_cost=calculate_total_cost(cart)

print(total_cost)

"""

# Example 4:Check If a String is Palindrome

# s="A man a plan a canal Panama"

# s=s.lower().replace(" ","")

# print(s)

"""
def is_palindrome(s):
    s=s.lower().replace(" ","")

    return s==s[::-1]

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome('Hello'))

print(is_palindrome('12321'))
"""

# s1="100"

# print(int(s1[::-1]))


# 😁😁 Example 5: Calculate the Factorials of a number using recursion😁😁

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))


