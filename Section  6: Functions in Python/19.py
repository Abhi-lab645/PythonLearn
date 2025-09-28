def greet(name="Guest"):
    print(f"Hello {name} Welcome to the paradise.")

greet("Apish")

def fn(*args):
    print(args)

fn(1,2,3,4,"Abhinav")


def print_numbers(*nums):
    print(nums)

    for num in nums:
        print(num)

print_numbers(1,2,3,4,5,10,"Golu")

def student_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

student_info(name="Abhinav",age=20,country="India")

def print_details(*args,**kwargs):

    print(f"postional args:{args}")

    for val in args:
        print(val)

    print(f"keyword args:{kwargs}")

    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_details(1,2,3,4,name="Apish",branch="CSE",address="Bangalore")
