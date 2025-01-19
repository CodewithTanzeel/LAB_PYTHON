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

lst=["a","b","c","d","e"]
n =input("Enter the element you want to search on the list :")
def search(n,lst):
    for n in lst:
            print(lst.index(n),"is found on the following index")
    
         

search(n,lst)
    



