# 


# num = int(input("Enter an integer: "))

# if num % 2 == 0:
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")



# 2. Write a program that asks for years of service and qualification from the user and calculates the salary as per the following table:
# Years of Service	Qualifications	Salary
# >= 10	Masters	150,000
# >= 10	Bachelors	100,000
# < 10	Masters	100,000
# < 10	Bachelors	70,000


# qualification_user = input("Enter your Qualification :   ").lower()
# years_of_service = int(input("Input Your Years of Service :"))

# if (qualification_user == "bachelors" and years_of_service >= 10 ):
#     print("Your estimated Salary will be 100,000")
# elif (qualification_user == "masters" and years_of_service >= 10 ):
#     print("Your estimated Salary will be 150,000")
    
# elif (qualification_user == "masters" and years_of_service < 10 ):
#     print("Your estimated Salary will be 100,000")
    
# elif (qualification_user == "bachelors" and years_of_service < 10 ):
#     print("Your estimated Salary will be 70,000")
# else:
#     print ("invalid inputs")





age = int(input("Enter the person's age: "))
if age < 2:
    print("The person is a baby.")
elif 2 <= age < 4:
    print("The person is a toddler.")
elif 4 <= age < 13:
    print("The person is a kid.")
elif 13 <= age < 20:
    print("The person is a teenager.")
elif 20 <= age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
