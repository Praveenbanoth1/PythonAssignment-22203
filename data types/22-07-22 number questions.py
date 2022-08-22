#1.1 write a program to find sum of number


'''
number = int(input("Enter any nunber: "))
sum1 = 0
for i in range(number+1):
    sum1 += i
print("sum of number is: ",sum1)

#input  Enter any nunber: 5
#output sum of number is: 15
'''


#============================================================================================================================



#1.2

'''
number = (input("Enter any nunber: "))
sum1 = 0
for i in (number):
    sum1 += int(i)
print("sum of number is: ",sum1)

#input:  Enter any nunber: 12345
#output: sum of number is: 15
'''


#============================================================================================================================



#2. WAP to find number is strong number or not

'''
num = int(input("enter your number: "))
temp = num
sums = 0
while (num):
    i = 1
    fact = 1
    rem = num %10
    while(i <= rem):
        fact *= i
        i += 1
    sums +=fact
    num //= 10
if (sums == temp):
    print("Given number is a strong number")
else:
    print("Given number is not a strong number")



#input:    enter your number: 145
#output:   Given number is a strong number
    
#input:    enter your number: 135
#output:   Given number is not a strong number
'''


#============================================================================================================================



#3.1 to find square root for float values

'''
number = float(input(" Enter any number: "))
square_root = number ** 0.5
print((square_root))


#input:  Enter any number: 15.6
#output: 3.9496835316262997'''

#============================================================================================================================



#3.2 for integer values
'''number = int(input(" Enter any number: "))
square_root = number ** 0.5
print(int(square_root))


#input:  Enter any number: 16
#output: 4
'''


#============================================================================================================================



#4 to calculate Area of Triangle

'''
left_side_length = int(input("Enter Left side length: "))
right_side_length = int(input("Enter Right side length: "))
base_length = int(input("Enter Base length: "))

perimeter_triangle = ((left_side_length + right_side_length + base_length) /2)

area_of_triangle = (perimeter_triangle*(perimeter_triangle - left_side_length)
                    *(perimeter_triangle - right_side_length)
                    *(perimeter_triangle -base_length)) ** 0.5
print(round(area_of_triangle, 2))
'''


#============================================================================================================================



#5. Quadradic Equation

a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
c = int(input("Enter Third number: "))

d = (b **2) - (4 * a * c)
d1 = (-b - (d ** 0.5)) / (2 * a)
d2 = (-b + (d ** 0.5)) / (2 * a)
print(d1)
print(d2)

#============================================================================================================================



#6.Swap of two Variables
'''
first_variable = int(input("Enter First Number: "))
second_variable = int(input("Enter Seconf Number: "))

print("Before Swapping: ",first_variable)
print("Before Swapping: ",second_variable)

third_variable = first_variable
first_variable = second_variable
second_variable = third_variable

print("After Swapping: ",first_variable)
print("After Swapping: ",second_variable)

#inputs
Enter First Number: 13,
Enter Seconf Number: 21

#outputs
Before Swapping:  13
Before Swapping:  21

After Swapping:  21
After Swapping:  13
'''


#============================================================================================================================



#7. converts kilometers into miles

'''
kilometer = int(input("kilometers: "))
miles = kilometer * 0.621

print("miles: ",round(miles,3))


#input  kilometers: 4
#output miles:  2.484'''

#============================================================================================================================



#8. leap year

'''
year = int(input("Enter Year Name :"))

if year %400 ==0:
    print("It is a Leap Year")
elif year %100 == 0:
    print("It is not a Leap Year")
elif year % 4 ==0:
    print("It is a Leap Year")
else:
    print("It is not a Leap Year")


#input  Enter Year Name :2012
#output it is a leap year'''

#============================================================================================================================



#9.1 Given number Prime number or Not


'''number = int(input("Enter a Number: "))
prime_number = False

if number>1:
    for i in range(2, number):
        if number % i == 0:
            prime_number = True
            break
if prime_number:
    print("Given Number is Not a Prime Number")
else:
    print("Given Number is a Prime Number")
#input   Enter a Number: 5
#output  Given Number is a Prime Number'''


#============================================================================================================================


#9.2 range of prime number

'''
first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))

sums = 0

for i in range(first_number, second_number+1):
    prime = 0
    for j in range(2, i):
        if i % j == 0:
            prime = 1
    if prime == 0 and i != 1:
        sums += 1 
print("Number of Prime Numbers: ",sums)

#inputs
Enter First Number: 10
Enter Second Number: 20

#output
Number of Prime Numbers:  4'''



#============================================================================================================================



#10. Find Factorial of number

'''
number = int(input("Enter Your Number: "))
fact = 1
for i in range(1,number +1):
    fact *= i
print("Factorial of Given Number is: ",fact)

#input  Enter Your Number: 5
#output Factorial of Given Number is:  120'''

#============================================================================================================================


#11.1 Fibenocci Sequence




'''nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

else:
   print("Fibonacci sequence: ")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

# input   How many terms? 6
# output  Fibonacci sequence:
0
1
1
2
3
5'''


#============================================================================================================================

#11.2 list of sum of febinoccii number 


'''
def febinoccii(n):
    a = 0
    b = 1
    list_1 = []
    for i in range(0, n+1):
        c = a + b
        a = b
        b = c
        list_1.append(c)
    return list_1

value = int(input("Enter any Number: "))        
val = febinoccii(value)
print(val)

# input   Enter any Number: 5
# output  [1, 2, 3, 5, 8, 13]'''


#============================================================================================================================


#12. find an amstrong number

'''first_number = int(input("Enter First Number: "))

for i in range(first_number + 1):
    x = len(str(i))
    sum_1 = 0
    temp = i
while temp > 0:
    digits = temp % 10
    temp //= 10
    sum_1 += digits ** x 
if i == sum_1:
    print("The given number is a amstrong number")
else:
    print("the given number is not an amstrong number")


# input   Enter First Number: 122
# output  the given number is not an amstrong number

'''
#============================================================================================================================

#13.find an Amstrong number in the given intervals


'''first_number = int(input("Enter First Number: "))
second_number = int(input("Enter second Number: "))

for i in range(first_number, second_number + 1):
    x = len(str(i))
    sum_1 = 0
    temp = i
    while temp > 0:
        digits = temp % 10
        sum_1 += digits ** x
        temp //= 10
    if i == sum_1:
        print("the amstrong numbers in that given range is: ",i)


#input
Enter First Number: 100
Enter Second Number: 200
#output
the amstrong numbers in that given range is:  153'''


#============================================================================================================================



#14. to find sum of natural numbers

'''
number = int(input("Enter a number: "))
add = 0
for i in range(1, number + 1):
    add += i
print("The sum of Natural Numbers are: ",add)


# input    Enter a number: 5
# Outuput  The sum of Natural Numbers are:  15'''


#============================================================================================================================


#15. Factors of Given Number


'''
number = int(input("Enter a Number: "))
list_1 = []

for i in range(1, number + 1):
    if (number % i == 0):
        list_1.append(i)
print("Factors for Given Number is: ", list_1)


# input   Enter a Number: 20
# output  Factors for Given Number is:  [1, 2, 4, 5, 10, 20]'''


#============================================================================================================================



#16. convert binary to decimal, Hexadecimal and Octa decimal


'''def decimal_to_binary(num):
    if num >= 1:
        decimal_to_binary(num // 2)
        print(num % 2, end = '')
num = int(input())
num = decimal_to_binary(num)'''


#============================================================================================================================



#17. find LCM for the given number
'''
a = int(input("Enter first number: "))
b = int(input("Enter second Number: "))
if a > b:
    great = a
else:
    great = b
lcm = False
for i in range(great,(a*b +1)):
    if not lcm:
        if (i % a == 0) and (i % b == 0):
            lcm = True
            great = i
print("LCM of Guven Number is: ",great)


#input
Enter first number: 16
Enter second Number: 4
#output
LCM of Guven Number is:  16'''


#============================================================================================================================




#18. find HCF for the given number



'''a = int(input("Enter first number: "))
b = int(input("Enter second Number: "))
if a > b:
    great = a
else:
    great = b
lcm = False
for i in range(great,(a*b +1)):
    if not lcm:
        if (i % a == 0) and (i % b == 0):
            lcm = True
            great = i
gcd = a * b //great
print("The HCF of the given Number is: ",gcd)'''


'''#input
Enter first number: 77
Enter second Number: 7
#output
The HCF of the given Number is:  7'''

