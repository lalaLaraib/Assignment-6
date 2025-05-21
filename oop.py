# # Project 06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# # 1.Using self:
# # Assignment:
# # Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")


student1 = Student("Efza",83)
student1.display()


# # 2. Using cls
# # Assignment:
# # Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1


    @classmethod
    def display_counter(cls):
        print(f"My total created objects are: {cls.count}")


obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()

Counter.display_counter()



# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...!")

my_car = Car("Mercedes")
print(my_car.brand)
my_car.start()


# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "HBL Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder


    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder} , Bank: {self.bank_name}")


account1 = Bank("Yazdan")
account2 = Bank("Hamdan")

account1.display()
account2.display()



# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b
    
result = MathUtils.add(14,70)
print("Sum of my 2 numbers are:", result)



# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger Object Created.")  # constructor message

    def __del__(self):
        print("Logger Object Destructor.")


log = Logger()
del log



# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# . a public variable name

# . a protected variable _salary, and

# . a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn


    def get_ssn(self):
        return self.__ssn
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("salary must be positive in number")

    def display(self):
        print(f"Name: {self.name}") # public
        print(f"Salary: {self._salary}") # protected
        print(f"SSN: {self.__ssn}") # private

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")
        print(f"Acessing SSN via getter command: {self.get_ssn()}") # private variable


m = Manager("HAMDAN", "23000", "555-657-2025", "Information Technology")
m.show_manager_info()
m.set_salary(45000)
print("Update Salary:", m._salary)

# print(m.__ssn)
print("Private SSN via managed: ", m._Employee__ssn)

        

# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with the name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher teaches: {self.subject}")

t = Teacher("Sana","ARTIFICIAL INTELLIGENCE Course.")



# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectuangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
rect = Rectuangle(9,8)
print("Area of Rectangle:", rect.area())


# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says : Ruff!! Rrrruff!!!")

dog1 = Dog("Rosa" , "Poodle")
dog1.bark()


# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_cocunt() to increase the count when a new book is added

class Book:
    total_books = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author

        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


book1 = Book("Head First Programming" "David Griffiths Paul Barry" , "2009")
book2 = Book("Think Python" , "2012")
book3 = Book("Effective Python" , "2015")
book4 = Book("Python Crash Course" , "2015")


print("Total books:", Book.total_books)



# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 13/9) + 32


temp_c = 45
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is equal to {temp_f}°F")



# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine  

    def start_car(self):
        return self.engine.start()  

# Example usage:
engine = Engine()
my_car = Car(engine)
print(my_car.start_car())



# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.


class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  

    def show_employee(self):
        return f"Department: {self.dept_name}\n{self.employee.get_details()}"

emp1 = Employee("HAMDAN", 2348965345)
dept1 = Department("HR", emp1)

print(dept1.show_employee())


# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# . A with a method show(),

# . B and C that inherit from A and override show(),

# . D that inherits from both B and C.

# . Create an object of D and call show() to observe MRO



class A:
    def show(self):
        print("A.show() called")


class B(A):
    def show(self):
        print("B.show() called")


class C(A):
    def show(self):
        print("C.show() called")


class D(B, C):
    pass


d = D()
d.show()  



print("Method Resolution Order (MRO):")
for cls in D.__mro__:
    print(cls.__name__)



# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello()


def log_function_call(fun):
    def wrapper():
        print("Function is being called")
        return fun()
    return wrapper


@log_function_call
def say_hello():
    print("Hello!")


say_hello()


# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.


def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls


@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

person = Person("EFZALARAIB")
print(person.greet())


# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self, price):
        self._price = price  

    @property
    def price(self):
        """Getter for price"""
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price"""
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative")

    @price.deleter
    def price(self):
        """Deleter for price"""
        print("Deleting price...")
        del self._price


product = Product(300)
print(product.price)      

product.price = 450        
print(product.price)

del product.price 

# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  

    def __call__(self, value):
        return value * self.factor  


double = Multiplier(6)


print(callable(double))  

result = double(20)
print(result) 



# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 17:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Age is valid.")


try:
    check_age(15)
except InvalidAgeError as e:
    print("Exception caught:", e)



# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current < 0:
            raise StopIteration  
        value = self.current
        self.current -= 1
        return value


for number in Countdown(5):
    print(number)

