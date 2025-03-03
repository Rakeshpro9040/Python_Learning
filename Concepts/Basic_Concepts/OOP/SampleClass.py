# class SampleClass():
#     pass
#
# my_sample = SampleClass()
# print(type(my_sample)) # <class '__main__.SampleClass'>
#
# class Dog():
#     def __init__(self,breed,color):
#         self.breed = breed
#         self.color = color
#
# Dog = Dog(breed = 'Lab', color = 'Black')
# print(type(Dog)) # <class '__main__.Dog'>
# print(Dog.breed) # Lab
# print(Dog.color) # Black

# class Circle:
#     pi = 3.14 # Class Object Attribute
#
#     # Circle gets instantiated with a radius (default is 1)
#     def __init__(self, radius=1): # __init__ Method gets called automatically whend you create instance fo this class
#         self.radius = radius # Attributes
#         self.area = radius * radius * Circle.pi # Reference to Class Object Attribute
#
#     # Method for resetting Radius
#     def setRadius(self, new_radius): # Methods
#         self.radius = new_radius
#         self.area = new_radius * new_radius * self.pi
#
#     # Method for getting Circumference
#     def getCircumference(self):
#         return self.radius * self.pi * 2
#
# c = Circle()
# print('Radius is: ',c.radius) # Radius is:  1
# print('Area is: ',c.area) # Area is:  3.14
# print('Circumference is: ',c.getCircumference()) # Circumference is:  6.28
#
# d = Circle(2)
# print('Radius is: ',d.radius) # Radius is:  2
# print('Area is: ',d.area) # Area is:  12.56
# print('Circumference is: ',d.getCircumference()) # Circumference is:  12.56
#
# c.setRadius(new_radius=3)
# print('Radius is: ',c.radius) # Radius is:  3
# print('Area is: ',c.area) # Area is:  28.26
# print('Circumference is: ',c.getCircumference()) # Circumference is:  18.84

# ############ Inheritance ############
# class Animal:
#     def __init__(self):
#         print("Animal created")
#     def whoAmI(self):
#         print("Animal")
#     def eat(self):
#         print("Eating")
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self) # Derived Class Inherits the Base class
#         print("Dog created")
#     def whoAmI(self): # Method Override
#         print("Dog")
#     def bark(self):
#         print("Woof!")
#
# d = Dog() # Animal created /n Dog created
# d.whoAmI() # Dog
# d.eat() # Eating  ---> Here we are calling a method from Base class
# d.bark() # Woof

# ############ Polymorphism ############
# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return self.name + ' says Woof!'
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return self.name + ' says Meow!'
#
# def pet_speak(pet):
#     print(pet.speak())
#
# niko = Dog('Niko')
# felix = Cat('Felix')
#
# pet_speak(niko) # Niko says Woof!
# pet_speak(felix) # Felix says Meow!

# ############ Abstract Class ############
# class Animal:
#     def __init__(self, name):  # Constructor of the class
#         self.name = name
#     def speak(self):  # Abstract method, defined by convention only
#         raise NotImplementedError("Subclass must implement abstract method")
#
# class Dog(Animal):
#     def speak(self):
#         return self.name + ' says Woof!'
#
# class Cat(Animal):
#     def speak(self):
#         return self.name + ' says Meow!'
#
# fido = Dog('Fido')
# isis = Cat('Isis')
#
# print(fido.speak()) # Fido says Woof!
# print(isis.speak()) # Isis says Meow!

############ Special Methods ############
class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book is destroyed")

book = Book("Python Rocks!", "Jose Portilla", 159) # A book is created

#Special Methods
print(book) # Title: Python Rocks!, author: Jose Portilla, pages: 159
print(len(book)) # 159
del book # A book is destroyed