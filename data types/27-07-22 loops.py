#1.    Accept 10 numbers from the user and display their average.

'''

n = 10
sums = 0
avg = 0


for i in range(n):
    num = int(input())
    sums += num
    
avg = sums/n
print(avg)



i/p
21
22
23
24
25
26
27
28
29
30

o/p
25.5'''


#------------------------------------------------------------------------------------------------------------------



#2. Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)

'''

n1 = int(input("Enter 1st Number: "))
n2 = int(input("Enter 2nd Number: "))

evn = []
odd = []

for i in range(n1, n2+1):
    if i %2 ==0:
        evn.append(i)
    else:
        odd.append(i)
        
print(evn)
print(odd)

i/p
12
37
o/p
[12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
[13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]

'''



#------------------------------------------------------------------------------------------------------------------




#3.   Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.

'''
n1 = int(input())
n2 = int(input())

for i in range(n1, n2+1):
    if i %11 == 0 and i % 2 != 0:
        print(i, end = " ")

i/p
100
500
o/p
121 143 165 187 209 231 253 275 297 319 341 363 385 407 429 451 473 495 '''



#------------------------------------------------------------------------------------------------------------------



#4.    Write a program to print numbers from 1 to 20 except multiple of 2 & 3


'''
for i in range(1, 20+1):
    if i%2 == 0 and i % 3 == 0:
        print(i, end = " ")

6 12 18'''


#------------------------------------------------------------------------------------------------------------------



#5.  Write a program that keep on accepting number from the user until user enters Zero. Display the sum and average of all the numbers.

'''
num=1
i=-1
s=0

while(num!=0):
   num=int(input("Enter any number: "))
   s=s+num
   i=i+1
   
print("sum: ", s)
print("Average",s/i)


i/p
Enter any number: 12
Enter any number: 34
Enter any number: 56
Enter any number: 78
Enter any number: 1
Enter any number: 0
o/p
sum:  181
Average 36.2'''


#------------------------------------------------------------------------------------------------------------------



#6.  Write a program to accept decimal number and display its binary number. 


'''
num = int(input())

def binary_number(num):
    ls=[]
    while num>0:
        rem=num%2
        ls.append(rem)
        num=num//2
    #print(ls)
    return ls


x=binary_number(num)

for i in x:
    print(i,end="")

op/=5
101'''


#------------------------------------------------------------------------------------------------------------------



#7.   Convert the following loop into for loop : 


'''
x = 4 

while(x<=8): 

    print(x*10) 

    x+=2

40
60
80

x = 4
for i in range(1,x):
    if i <= 8:
        print(x* 10)
    x += 2

40
60
80'''


#------------------------------------------------------------------------------------------------------------------



#8.  What is nested loop?
'''
 A nested loop is a loop inside the body of the outer loop.
 The inner or outer loop can be any type, such as a while loop or for loop
'''


#------------------------------------------------------------------------------------------------------------------



#9. Write a program to convert temperature in Fahrenheit to Celsius.

'''
Fahrenheit= int(input("enter the fahrenheit value : "))

Celsius = ((Fahrenheit-32)*5)/9)

print("Temperature in Celsius is: ")
print(Celsius)

op/=enter the fahrenheit value : 98
Temperature in Celsius is: 
36.666666666666664'''
#------------------------------------------------------------------------------------------------------------------



#10.   Write a Python program to get the Fibonacci series between 0 to 50.  

'''Note : The Fibonacci Sequence is the series of numbers : 

0, 1, 1, 2, 3, 5, 8, 13, 21, .... 

Every next number is found by adding up the two numbers before it. 

Expected Output : 1 1 2 3 5 8 13 21 34


def fib(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fib(n-1) + fib(n-2)

for i in range(0,50):
    x=fib(i)
    print(x,end=" ")

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711
28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309
3524578 5702887 9227465 14930352 24157817'''

#------------------------------------------------------------------------------------------------------------------


#11.  Write a Python program which iterates the integers from 1 to 50.
#For multiples of three print "Fizz" instead of the number and for
#the multiples of five print "Buzz". For numbers which are multiples of both three and five print "Fizz Buzz". 

'''Sample Output : 

fizzbuzz 

1 

2 

fizz 

4 

Buzz


for i in range(1, 51):
    if i % 3 ==0 and i % 5 ==0:
        print("Fizz Buzz")

    elif i % 3 == 0:
        print("Fizz")
        
    elif i %5 == 0:
        print("Buzz")
        
    else:
        print(i)


1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz Buzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
Fizz Buzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
Fizz Buzz
46
47
Fizz
49
Buzz
''' 
    

#------------------------------------------------------------------------------------------------------------------



#12.  Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

'''Note : Use 'continue' statement. 

Expected Output : 0 1 2 4 5


for i in range(0, 6):
    if i == 3:
        continue
    
    print(i, end = " ")


0 1 2 4 5 '''





num = int(input())
def binary_number (num):
    ls = []
    while num>0:
        rem = num % 2
        ls.append(rem)
        num //= 2
    return ls
x = binary_number(num)
for i in x:
    print(i, end = "")
        
    
