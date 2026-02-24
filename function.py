# print("I am Groot")

# def iamGroo():
#     print("I am Groot")

# for i in range(0,10):
#     iamGroo()
#function with arguments/parameters and return types
#function with arguments/parameters and only  return types
#function with arguments/parameters and no return types
#function with No arguments and no return types
# name=input("Please enter your name to Continue:")
# greet_someone
# def gree_someone(name):
#     print(f"Hello,{name}!")
#     print("Welcome to my Python Script")

# greet_someone("Dennis")

# def sum(*args):
#     result=a+b
#     return result

# a=int(input("Please enter value A:"))
# b=int(input("Please enter value B:"))
# c=int(input("Please enter value C:"))
# #help(sum)
# print(f"Sum of {a} + {b} =",sum{a,b,c})

def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

display_info(name="Dennis",age=20,sex="Male",married=False)
