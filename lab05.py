# C.   Write Python programs for the following:

# 1.	Write a program that prints the first 10 natural numbers and their sum using ‘for loop’.
# Sample output:
#       The first 10 natural number are :
#       1 2 3 4 5 6 7 8 9 10 
#       The Sum is : 55
# sum = 0
# num = 1
# for num in range (1,11):
#      print ( num , end ="")
#      sum += num


# print("\nThe Sum is:", sum)
 

     
# 2.	Write a program to print the multiplication table of the number entered by the user. The table should get displayed in the following form.
# 29 x 1 =  29
# 29 x 2 =  58
# …
# 29 x 10 = 290

num = int(input("Enter a input for a table u want to print : "))
for i in range(1,11):
    print (num, "X", i , "=" , num * i)

 