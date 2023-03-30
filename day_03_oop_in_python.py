#Object-Oriented Programming
#Classes are used to create objects. Objects are instances of that class, essentially
#A class is a blueprint for creating objects. It defines the attributes and methods that the
#object will have.

#Creating a Person Object that has a name and age attribute and a 'greet' method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

#Now we can create a 'Person' object and call its greet method like this:

person = Person("Bright", 30)
person.greet()

#Another Example
class CountingClicker:
    """A class ca/should have a docstring, just like a function"""
    def __init__(self, count=0):
        self.count = count

#Commented out examples of objects
    # clicker1 = CountingClicker()
    # clicker2 = CountingClicker(100)
    # clicker3 = CountingClicker(count=100) #line 27 and this line does the same thing

# Another method like __init__ is the __repr__ which produces the string representation of a class instance:

    def __repr__(self):
        return f"CountingClicker(count={self.count})"
    #Implementing the public API of our class:

    def click(self, num_times = 1):
        """Click the clicker some number of times."""
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0

#Having defined it, let's use assert to write some test cases for our clicker:

clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"

#We can also occassionally create subclasses that inherit some of their functionality from a parent class.
#For example we could create a non-resetable clicker by using CountingClicker as the base class and overiding the reset method to do nothing.

#A subclass inherits all the behavior of its parent class.
class NoRestClicker(CountingClicker):
    #this class has all the same methods as CountingClicker
    #Except taht it has a reset method that does nothing.
    def reset(self):
        pass

clicker2 = NoRestClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"