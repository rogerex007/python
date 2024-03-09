
# Reserved Words

# False      class      finally    is         return
# None       continue   for        lambda     try
# True       def        from       nonlocal   while
# and        del        global     not        with
# as         elif       if         or         yield
# assert     else       import     pass
# break      except     in         raise

# Int
a = 1
# Float
b = 1.2
# Complex
c = 1 + 2j

# String
d = "Hello World"

# List
e = [1, 2, 3]


# Tuple
f = (1, 2, 3)


# Dictionary
g = {
    "name": "John",
    "age": 30,
    "single": True,
    "hobbies": ["Football", "Reading", "Coding"],
}

# Set
h = {1, 2, 3}

# Frozen Set
i = frozenset({1, 2, 3})

# Boolean
j = True
k = False

# Nones
l = None

# Bytes
m = b"Hello World"

# format
n = f"Hello, my name is {g['name']} and I am {g['age']} years old."

# Functions

def my_function():
    print("Hello World")

def my_function_with_params(name, age):
    print(f"Hello {name}")
    print(f"You are {age} years old")

def welcomeMessage(name, age):
    return f"Hello {name}, you are {age} years old"

def error_message():
    return "Invalid username or password"

def login(username, password):
    if username == "admin" and password == "admin":
        print(welcomeMessage(username, 30))
        return True
    else:
        print(error_message())
        return False

# lambda
# lambda parameters: expression

x = lambda name: print(f"Hello {name}")

# Cicles and conditionals

# if - else
# while
# for
# do while


# classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def welcome(self):
        return f"Hello {self.name}, you are {self.age} years old"

    def is_adult(self):
        return self.age >= 18

Person1 = Person("John", 30)

print(Person1.welcome())

Person2 = Person("Jane", 15)

print(Person2.welcome())