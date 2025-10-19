# class A():
#     def __init__(self, i):
#         self.i = i
# def main():
#     a = A()
#     print(a.i)
# main() # Call the main function


# class Dog:  
#     attr1 = "mamal"
#     def fun(self):
#         print("I'm a", self.attr1)


# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())


# class Person:  
#     # init method or constructor   
#     def __init__(self, name):  
#         self.name = name  
    
#     def say_hi(self):  
#         print('Hello, my name is', self.name)  
    
# p = Person('XXX')  
# p.say_hi()  


# class Dog:  
#     attr1 = "mamal"
#     def fun(self):
#         print("I'm a", self.attr1)


# print("Hello \b  World!")

# 1. Write a program that create  a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called infor_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the “restaurant is open”.


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type      
    
    def info_restaurant(self):
        print(f"{self.restaurant_name} offers a variety of {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for service.")

res1 = Restaurant("Shinwairi", "Desi")
res1.info_restaurant() 
res2 = Restaurant("chinese", "lichen")
res2.info_restaurant() 
res2.open_restaurant()  