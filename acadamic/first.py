# দ্বীঘাত সমীকরণের মূলসমূহ নির্ণয়র প্রোগ্রাম

import math
from operator import le
from re import L
from reprlib import recursive_repr
from tkinter import PIESLICE
from turtle import pen, up

a = int( input("Enter the value of a: "))
b = int( input("Enter the value of b: "))
c = int( input("Enter the value of c: "))

d = (b*b) - (4*a*b)

if (d==0):
    x = -b/(2*a)     
    print("Roots are real & equal & are :", x,x)
elif (d > 0):
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d)) / (2*a)
    print("Roots are real & unrqual & are:",x1,x2)
else:
    print("THe Roots are imaginary")



# শর্তসাপেক্ষে বিষমবাহু ত্রিভুজের ক্ষেত্রফল নির্ণয়ের প্রোগ্রাম


import math
a = int( input("Enter the value of a: "))
b = int( input("Enter the value of b: "))
c = int( input("Enter the value of c: "))

if ((a+b)>b and (a+c) > b and (b+c) > a ):
    s = (a+b+c) / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of the Triangle is:", area)
else:
    print("Triangle is not possible")


# Check Leap year

year = int(input("Please Enter the value of year:"))
if (year%4==0 and year%100 != 0) or (year%400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")



# Check prime number using loop

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print("Beacuse",i, "times", num// i, "is", num)
            break
    else:
        print(num, 'is a prime number')
else:
    print(num, "is not a prime numbner")



# factorial using loop

num = int(input("Enter a number"))
factorial = 1

if num < 0:
    print("Sorry, factorial does not exist for nagative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial *i
    print("The facotorial of", num, "is", factorial)


# febonacci serices using loop
Terms = int(input("How many terms:"))
n1 = 0
n2 = 1
count = 0
if Terms <= 0:
    print("Please enter  a positive number")
elif Terms == 1:
    print("Fibonacci sequence upto", Terms, ":")
    print(n1)
else:
    print("Fibonacci sequence upto", Terms,":")
    while count < Terms:
        print(n1, end=",")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


# find the greatest and smallest number

input_set = []
input_num = 0
while (input_num >= 0):
    input_num = int(input("Please enter a number or -1 to finish:"))
    if (input_num < 0):
        break
    input_set.append(input_num)
print(input_set)


largest = input_set[0]

for i in range(len(input_set)):
    if input_set[i] > largest:
        greatest = input_set[i]
print("Largest number is ", greatest)

smallest = input_set[0]

for i in range(len(input_set)):
    if input_set[i] < largest:
        smallest = input_set[i]
print("Smallest number is :", smallest)



# find prime number in specific range 

lower = int( input("Enter lower range: "))
upper = int( input("Enter upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# sum of digit 

sum = 0
number = int(input("Please enter the value number:"))

while number > 0:
    x = number % 10
    number = number // 10
    sum = sum + x
print("Summation of the digits is = ", sum)


# check is armstrong 

num = int( input("Enter a number:"))

sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")




# count vowels in string 

vowels = "aeiou"

string = input("Enter a string:").casefold()

count = {}.fromkeys(vowels, 0)

for char in string:
    if char in count:
        count[char] += 1
print(count)


# print pattern 

k = 8
for i in range(0, 5):
    for j in range(0, k):
        print(end=" ")
    k = k-2
    for j in range(0, i+1):
        print("*", end="")
    print()



# print floyads trangle  

while True:
    print("Enter 'x' for exit")
    ran = input("Upto how many line ?")
    if ran == "x":
        break
    else:
        rang = int(ran)
        k = 1
        for i in range(1, range+1):
            for j in range(1, i+1):
                print(k, end="")
                k = k+1
            print()
        print()


# sort list in acending order 

data_list = [5, -2, 15, 30, -6,27,47]

new_list = []

while data_list:
    minimum = data_list[0]
    for x in data_list:
        if x < data_list:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)
print(new_list)


# sum of matrix 

x = [
    [12,7,3],
    [4,5,6],
    [7,8,9]
]

y = [
    [5,8,1],
    [6,7,8],
    [7,8,9]
]

result = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]



for i in range(len(x)):
    # iterate through columns 
    for j in  range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
for r in result:
    print(r)




# multiplecation of matrix 

x = [
    [12,7,3],
    [4,5,6],
    [7,8,9]
]

# 3*4 matrix
y = [
    [5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]
]


# result is 3 * 4
result = [[sum(a*b for a,b in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]

for x in result:
    print(r)



# substrct of matrix 

matrix1 = [
    [10,11,12],
    [13,14,15],
    [16,17,18]
]
matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rmatrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        rmatrix[i][j] = matrix1[i][j] - matrix2[i][j]

for r in rmatrix:
    print(r)


# transpose of matrix 

matrix = [
    [1,2],
    [3,4],
    [5,6]
]

rmatrix = [
    [0,0,0],
    [0,0,0]
]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        rmatrix[i][j] = matrix[i][j]

for r in rmatrix:
    print(r)

# test prime number using function 

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2, n):
            if (n % x ==0):
                return False
        return True
print(test_prime(13))




# fibonacci using function 

def rec_fibo(n):
    if n <= 0:
        return n
    else:
        return rec_fibo(n-1) - rec_fibo(n-2)

Terms = int(input("Enter how many terms:"))

if Terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(Terms):
        print(rec_fibo(i))
    


# factorial using recurtion 


def rec_fact(n):
    if n <= 1:
        return 1

    else:
        return n * rec_fact(n - -1)

n = int(input("Enter a number:"))

if n < 0:
    print("Sorry, factorial does not exist fpr negative numbers")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    print("factorial of ", num, "is ", rec_fact(n))


# sum of natural number 

def recu_sum(n):
    if n <= 1:
        return n
    else:
        return n + recu_sum(n-1)


num = int(input("Enter a number:"))

if num < 0:
    print("Enter a positive number")
else:
    print("The sum is", recu_sum(num))


# find how many line have in a file

def file_lengthy(fname):
    with open(fname) as f:
        for i, j in enumerate(f):
            pass
        return i + 1


print("Numbe rof lines in the file:", file_lengthy("text.txt"))











