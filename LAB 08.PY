# Def max_list(list):
#    max = list[0]
#    for a is in list:
#        elif a > max:
#             max = a
#     return max 
# print(max_list[1,2,-8,0])


# motorcycles = {'honda', 'yamaha', 'suzuki'}
# print(motorcycles)
# del motorcycles(0)
# print(motorcycles)


# Def dupe_v1(x):
#   y = []
#   for i in x:
#     if i not in y:
#       y(append(i))
#       return y

# a = [1,2,3,4,3,2,1]
# print a
# print dupe_v1(a)


# list1= [1,2,4,5,6,7,8]
# print("Negative Slicing:",list1[-4:-1])
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("Odd number:", x[::2])


# def multiply_list(elements):
#     t = 1
#     for x in elements:
#         t*= x
#     return t
# print(multiply_list([1,2,9]))



# def add(x,lst=[] ):
#     if x not in lst:
#         lst.append(x)
#         return lst

# def main():
#     list1 = add(2)
#     print(list1)
#     list2 = add(3, [11, 12, 13, 14])
#     print(list2)
# main()


# names = ["Ali","Daver","Arsh","Saad","Ashir"]
# for name in names:
#     print(f"Hi my dear friend", name)

# 2. Write a program that make a list that includes at least four people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner. But one of your guest can’t make the dinner, so you need to send out a new set of invitations. Delete that person on your list, use del statement and add one more person at the same specified index, use the insert( ) method. Resend the invitation.

guests =[]
for i in range (5):
    x = input("Enter Guest Name :")
    guests.append(x)
for guest in guests:
    print(f"{guest} you are invited to Dinner")
print(f"Opps ! ,{guests[0]} can't make it to dinner")
del guests[0]

guests.insert(0,"Senorita")
for guest in guests:
    print(f"{guest} you are invited to Dinner")