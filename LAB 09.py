# 'apple' is in ['orange', 'apple', 'grape']
# def countX(lst, x): 
#     return lst.count(x)
# strs = ['aa', 'BB', 'zz', 'CC']
# print (sorted(strs)) 
# print (sorted(strs, reverse=True))   
# test_list = [1, 4, 5, 8, 10] 
# print ("Original list : " , test_list) 
  
# # check sorted list  

# if(test_list == sorted(test_list)):
#     print ("Yes, List is sorted.") 
# else : 
#     print ("No, List is not sorted.")


# 1. Write a program that take function which implements linear search. It should take a list and an element as a parameter, and return the position of the element in the list. The algorithm consists of iterating over a list and returning the index of the first occurrence of an item once it is found. If the element is not in the list, the function should return ‘not found’ message. 

# lst=["a","b","c","d","e"]
# n =input("Enter the element you want to search on the list :")
# def search(n,lst):
#     for n in lst:
#             print(lst.index(n),"is found on the following index")
    
         

# search(n,lst)
    

# def linearsearch(list,n,x)

# 1. Write a program that take function which implements linear search. It should take a list and an element as a parameter, and return the position of the element in the list. The algorithm consists of iterating over a list and returning the index of the first occurrence of an item once it is found. If the element is not in the list, the function should return ‘not found’ message.

# list=["a","b","c","d","e","f"]
# e =input("Enter the element u want to search in the list :").lower()
# def linear(list,e):
#       for i in range(len(list)):
#             if list[i]==e:
#                   return print(f"Your element {e} is found on ", list.index(e))
            
#       return print("not found")
# linear(list,e)

# 2. Write a program that create function that takes two lists and returns True if they have at least one common member. Call the function with atleast two data set for searching.

# list=["Ali",1,"norm"]
# list1=["Sam",1,"Josh"]

# def doublelinear(list,list1):
#     for i in range(len(list)):
#         if list1[i] == list[i]:
#             return print("True")
#     return print("False")
# doublelinear(list,list1)



# 3. Write a program that create function that merges two sorted lists and call two list with random numbers.

# list2 = [1,2,5,6,11,3,4]
# list1 = [90,45,23,67,34]
# x1=sorted(list2)
# x2=sorted(list1)
# print(f"Sorted list: {x1} ")
# print(f"Sorted list: {x2} ")

# def extender(x1,x2):
#      x1.extend(x2)
#      return print(f"Combined extendedsorted list :{x1}")
    
# extender(x1,x2)
