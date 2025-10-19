# try:
#   a = "PYTHON"
#   a[0] = "x"
# except TypeError:
#   a = "PYTHON"
#   a[0] =a = "PYTHON"

# a = "PYTHON"
# a[0] = "x"

# a = STRING
# i = 0
# while i < len(b):
#     c = a[i]
#     print(c)
#     i+=i + 1

# s= "Welcome"
# for i in range(0, len(s), 2):
#     print(s[i], end = '')


# s = input("Enter a string: ")
# if "Python" in s:
#     print("Python", "is in", s)
# else:
#     print("Python", "is not in", s)

# Def 1my_function(x):
# return x[::-1]

# mytxt = 1my_function("I wonder how this text looks like backwards")
# print(mytxt)

# eliyas

# str='cold'
# list_enumerate=list(enumerate(str))
# print("list enumerate:", list_enumerate)
# print("list length:", len(str))
# s1 = "Welcome to Python"
# s2 = s1.replace("o","abc")
# print(s2)
# a = "Python" + "String"
# b = "<" + a*3 + ">"
# print(b)

# 1.	Write a program that Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(),rstrip(), and strip().

# def name(Name):
#     edit_name=f'\t{Name}\t\n'
#     print(edit_name)
#     nameOne=edit_name.lstrip()
#     print(nameOne)
#     nameTwo=edit_name.rstrip()
#     print(nameTwo)
#     nameThree=edit_name.strip()
#     print(nameThree)
# Name=input('enter your name :')
# name(Name)
#2
color=input('enter your favouriate color: ')
end=9
for i in range(3):
    for j in range(end):
        if i == 0 or i==2 or j == 0 or j==end-1:
            print(color,end='')
        else:
            for k in range(len(color)):
              print(' ',end='')
    print()



