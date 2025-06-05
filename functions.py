# functions
def greet():
    print("hello")

greet()

# functions with arguments
def greet(name):
    return (f"hello  {name} welcome! ")

names=greet("vishnu") 
print(names)

# function with *args
def add(*args):
    total=0
    for num in args:
        total+=num
    return total

print(add(1,2,3,4))

# functions with **kwargs(here key value pair is used)
def  create_profile(**kwargs):
    print("user profile")
    for key,value in kwargs.items():
        print(f"{key} :{value}")
    
create_profile(name="vishnu",age=25,job="software engineer")

