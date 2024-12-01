# define sub(x, y) 
# return x + y

# define describe_pet(pet_name, animal_type='dog'): 
# print("\nI have a " , animal_type ,".")
# print("My " , animal_type + "'s name is " , pet_name +
# ".")

def type_of_int(i):
     if i // 2 == 0:
       return 'even'
     else:
       return 'odd'
type_of_int(9)

# def test(a):
#    def add(b):
#     a =+ 1
#     return a+b 
#    return add
# func = test(4)
# print(func(4))


# def return_none(): 
#   return
# print(return_none())

# def test_range(n):
#    if n in range(3,9):
#     print( n,"is in the range") 
#    else :
#     print("The number is outside the given range.") 
# test_range(7)
# test_range(10)
# test_range(4)


# 1.	Write a user-defined function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.
# part c
# def favourite_book(title):
#     print(f"One of my Favourite book is {title}")

# booktitle = "silenthill"
# favourite_book(booktitle)

# 2.	Write a user-defined function called max( ), that returns the maxium of three integer numbers.

# def max(x,y,z):
#     if x >= y and x >= z:
#         return x
    
#     elif y >= x and y >= z:
#         return y
#     else:
#         return z

# print(f"The maximum value is : ",max(4,6,9))

#Euclids theorm
# a = b * x + a % b
# we can also import predefined gcd module from math
#import math
# gcd(2,6)

# def gcd_program(a,b):
#     if b==0:
#         return a 
#     else:
#         return gcd_program(b,a%b)

# num1 = int(input("enter the first number: "))
# num2 = int(input("enter the second number: "))
  
# print(gcd_program(num1,num2))

# 4.	Write a user-defined function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city,country="pakistan"):
    print(f"{city} is a part of {country}")

describe_city("karachi")
describe_city("lahore")
describe_city("Los angleous","USA")

