# CLASS

## Class:
- Class is a blue print for creating objects.
- It binds the attributes and methods together.
- To create a class 'class' keyword is used. For example
    class Myname

## Object:
- To acess the attributes in the class , an object is created.
    object = class()
- We can acess the attributes and method of an object using . operator

## Example for class:
class add:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def get_number(self):
        return (self.num1 + self.num2)
    
a =  add(5, 6)
print(a.get_number())

- Here add is the class name.
- __init__() is a function used to initialize the attributes in the class.
- a is the object in the class, which acess the mehod in the class.

