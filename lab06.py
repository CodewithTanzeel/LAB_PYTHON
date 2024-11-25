# 1.Write a program to add first seven terms twice of the following series:



# 2.Write a program to print all prime numbers from 900 to 1000. [Hint: Use nested loops, break and continue]



# 3.Write a program to display multiplication table (1-5) using nested looping Sampled output: [hint: '{ } ' .format(value)]
# 02 X 01 = 02

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()
