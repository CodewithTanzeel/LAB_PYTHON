# t = (1, 2, 3)
# t.append(4)
# t.remove(0)
# del t[0]
# 1user_0=['username':'efermi','first':'enrico','last':'fermi',]
# for key, value in 1user_0.items():
#     print("\nKey: " ,key)
#     print("Value: " ,value)


# tuple1 = ("green", "red", "blue")
# tuple2 = tuple([7, 1, 2, 23, 4, 5])
# tuple3 = tuple1 + tuple2 
# print(tuple3)
# tuple3 = 2 * tuple1 
# print(tuple3)
# print(tuple2[2 : 4]) 
# print(tuple1[-1])


# def main():
#     d = {"red":4, "blue":1, "green":14, "yellow":2}
#     print(d["red"])
#     print(list(d.keys()))
#     print(list(d.values()))
#     print("blue" in d)
#     print("purple" in d)
#     d["blue"] += 10
#     print(d["blue"])
# main() # Call the main function  


# 1. Write a program that create a buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple. (Hint:Use a for loop to print each food the restaurant offers. Also the restaurant changes its menu, replacing two of the items with different foods and display the menu again.


# buffet = ("Pasta","Prawnkarahai","Chickenpulao","wontong","Biryani")
# for i in range(len(buffet)):
#     print(buffet[i]," is availble at the restaurant")
# x =list(buffet)
# print(x)
# x.pop(3)
# x.pop(3)
# x.append("friedchicken")
# x.append("MalaiBoti")
# tuple(x)
# for i in range(len(buffet)):
#     print(f" {x[i]} is available at the restrautant")



# 2. Write a program for “Guess the capitals” using a dictionary to store the pairs of states and capitals so that the questions are randomly displayed. The program should keep a count of the number of correct and incorrect responses.

# GTC = {"Pakistan":"islamabad","America":"WashingtonDc","Germany":"Berlin","China":"bejing","Japan":"tokyo"}

# userguess=input("enter your guess")


   

                
import random

def guess_the_capitals():
    capitals = {
        "California": "Sacramento",
        "Texas": "Austin",
        "Florida": "Tallahassee",
        "New York": "Albany",
        "Illinois": "Springfield",
    }

    correctans = 0
    incorrecyans = 0
    userinput = input(f"   



guess_the_capitals()



# 3. Write a pogram that make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store three favorite places for each person through list. Loop through the dictionary, and print each person’s name and their favorite places.
# Output look alike: 
# abc likes the following places:
# - Bear Mountain
# - Death Valley
# - Tierra Del Fuego 

# favourite_places={"Arfin":"sicili","hasnain":"Japan","FahadButt":"America"}

# for key,value in favourite_places.items():
#     print(f"{key} favourite place is {value}")
#


