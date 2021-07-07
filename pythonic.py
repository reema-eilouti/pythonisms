# Task1
class CountFromTen:
    def __init__(self, limit):
        self.limit = limit
 
    def __iter__(self):
        self.x = 10
        return self
 
    def __next__(self):
        x = self.x
 
        if x > self.limit:
            raise StopIteration
 
        self.x = x + 1;
        return x

for i in CountFromTen(15):
    print(i)  # should print numbers from 10 to 15
 


#Task2
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 
  
def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 
  
@decor1
@decor
def num(): 
    return 10
  
print(num()) # should be 400



#Task3
class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'''
\\\\
(o>
//\\
V_/__
||
||\n\n This is {self.name}, {self.age} years old. \n\n'''

parrot = Parrot('romeo', 2)
print(parrot) # should print the parrot and its name and age
