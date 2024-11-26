# 1.Write a program to add first seven terms twice of the following series:
# Program to add first seven terms twice of a series
result = 0
for i in range(1, 8):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    result += i / factorial
result *= 2
print("Result:", result)



# 2.Write a program to print all prime numbers from 900 to 1000. [Hint: Use nested loops, break and continue]

for num in range(900, 1001):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")


# # 3.Write a program to display multiplication table (1-5) using nested looping Sampled output: [hint: '{ } ' .format(value)]
# # 02 X 01 = 02

for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()
