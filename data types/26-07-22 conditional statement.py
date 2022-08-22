#1.Print First 10 natural numbers using while loop
'''i=1
while i<=10:
    print(i)
    i+=1'''
#2.Calculate the sum of all numbers from 1 to a given number
'''i=1
total=0
while i<=10:
    total+=i
    i+=1
print(total)
op/=55'''
#3.Write a program to print multiplication table of a given number

'''num=int(input("enter a num you want: "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

op/=enter a num you want: 9
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90'''

#4.Display numbers from a list using loop

'''lst=[2,4,8,9,6,7,5]
for i in lst:
    print(i)'''

#5.Count the total number of digits in a number

'''num=input("enter a num you want: ")
count=0
for i in num:
    count+=1
print(count)
op/enter a num you want: 456
3'''

#6Print list in reverse order using a loop

'''lst=[2,4,9,6,7,5,1]
lst1=[]
for i in range(len(lst)):
    x=lst.pop()
    lst1.append(x)
print(lst1)
op/=[1, 5, 7, 6, 9, 4, 2]'''

#7.numbers from -10 to -1 using for loop Display

'''for i in range(-10,0):
    print(i)'''

#8.Use else block to display a message “Done” after successful execution of for loop

'''for i in range(1,5):
    print("you r not done!!!")
else:
    print("Done!!!")'''


#9.Write a program to display all prime numbers within a range

'''def prime(num):
    fact=[]
    for i in range(1,num+1):
        if num%i==0:
            fact.append(i)

    if len(fact)==2:
        return "prime"
    else:
        return "notprime"

lower=int(input("the range from  :"))        
upper=int(input(" To :"))
prim=[]
for i in range(lower,upper+1):
    d=prime(i)
    if d == "prime":
        prim.append(i)
print(prim)

op/=the range from  :20
To :100
[23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]'''


#10.Display Fibonacci series up to 10 terms

'''def fib(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fib(n-1) + fib(n-2)

user_no=int(input("enter a num you want :"))
print(fib(user_no))

op/=enter a num you want :6
8'''

#11.Find the factorial of a given number

'''num=int(input("enter a num you want: "))
factorial=1
for i in range(1,num+1):
    factorial*=i
print(factorial)

op/=enter a num you want: 4
24'''

#12. Reverse a given integer number

'''num=int(input("enter a num you want: "))
x=str(num)
print(x[::-1])
y=int(x)
print(type(y))

op/=enter a num you want: 45
54
<class 'int'>'''

#13.Find the sum of the series upto n terms

'''num=int(input("enter a num: "))
total=0
for i in range(num+1):
    total+=i
print("sum of series of num is",total)
op/=enter a num: 45
sum of series of num is 1035'''


#14.Calculate the cube of all numbers from 1 to a given number
'''num=int(input("enter a num for range: "))

for i in range(1,num+1):
    cube=i**3
    print(cube)
op/=enter a num for range: 6
1
8
27
64
125
216'''

#15.Use a loop to display elements from a given list present at odd index positions

'''lst=[4,5,6,8,9,7,2,51,24,58]
for i in range(len(lst)):
    if i%2!=0:
        print(lst[i])

op/=5
8
7
51
58'''

#16.Name the keyword which helps in writing code involves condition.

#if ,elif,else,

#17.Write the syntax of simple if statement.

'''i=5
if i==5:
    print(i)'''

#18.Is there any limit of statement that can appear under an if block.

#19.Write a program to check whether a person is eligible for voting or not. (accept age from user)

'''age=float(input("enter the age of the person: "))
if age>=18:
    print("person is eligible for voting")
else:
    print("person is not eligible for voting")
op/=enter the age of the person: 45
person is eligible for voting'''


#20.Write a program to check whether a number entered by user is even or odd.

'''num=int(input("enter a num: "))
if num%2==0:
    print("the num is even")
else:
    print("the num is odd")
op/=enter a num: 58
the num is even'''

#21.a program Write to check whether a number is divisible by 7 or not.

'''num=int(input("enter a num: "))
if num%7==0:
    print("the num is divisible by 7")
else:
    print("the num is not divisible by 7")

op/=enter a num: 56
the num is divisible by 7'''

#22.Write a program to display "Hello" if a number entered by user is a multiple of five otherwise print "Bye". 

'''num=int(input("enter a num: "))
if num%5==0:
    print("Hello")
else:
    print("Bye")

op/=enter a num: 45
Hello'''

'''23.Write a program to calculate the electricity bill (accept number of unit from user) according to the following
criteria : 

            Unit                                                     Price   

First 100 units                                               no charge 

Next 100 units                                              Rs 5 per unit 

After 200 units                                             Rs 10 per unit 

(For example if input unit is 350 than total bill amount is Rs2000) '''


'''ut = int(input("Enter number of units: "))
if ut <=100:
    amt = "no charge"
elif ut >100 and ut <= 200:
    amt = (ut-100) *5
else:
    amt = 500 + (ut - 200)*10

print("Total amount to pay is ", amt)

op/=Enter number of units: 350
Total amount to pay is  2000'''

#24.Write a program to display the last digit of a number. 
#(hint : any number % 10 will return the last digit)

'''num=int(input("enter a num: "))
lstdig=num%10
print("last digit is :",lstdig)

op/=enter a num: 56
last digit is : 6'''

#25.Write a program to check whether the last digit of a number( entered by user ) is  divisible by 3 or not. 

'''num=int(input("enter a num: "))
lstdig=num%10
print("the last digit of num is: ",lstdig)
if lstdig%3==0:
    print("yes last digit is divisible by 3")
else:
    print("no last digit is not divisible by 3")

op/=enter a num: 45
the last digit of num is:  5
no last digit is not divisible by 3'''

#25.Write a program to accept percentage from the user and display the grade according to the following criteria: 
'''Marks                                    Grade 

         > 90                                         A 

         > 80 and <= 90                       B 

        >= 60 and <= 80                       C 

         below 60                                  D 



perc=int(input("enter the percentage: "))
if perc > 90:
    print("grade A")
elif perc > 80 and perc <= 90:
    print("your grade is : B")
elif perc >=60 and perc <= 80:
    print("your grade is : C")
elif perc < 60 :
    print("your grade is : D")
else:
    print("please insert currect input")

op/=enter the percentage: 45
your grade is : D'''


#26.Write a program to accept the cost price of a bike and display the road tax to be paid according to
#the following criteria : 
'''Cost price (in Rs)                                       Tax 

        > 100000                                                  15 % 

        > 50000 and <= 100000                          10% 
        <= 50000                                                  5%'''



'''bike_mrp=int(input("enter the amount of bike: "))
if bike_mrp>100000:
    print(f"the road tax is paid by the owner is {bike_mrp*(15/100)}")
elif bike_mrp>50000 and bike_mrp<=100000:
    print(f"the road tax is paid by the owner is {bike_mrp*(10/100)}")
elif bike_mrp<=50000:
    print(f"the road tax is paid by the owner is {bike_mrp*(5/100)}")

op/=enter the amount of bike: 1000
the road tax is paid by the owner is 50.0'''


#28.Write a program to check whether an years is leap year or not. 
'''year = int(input('Enter year : '))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print(year, "is a leap year.")
else :
    print(year, "is not a leap year.")

op/=Enter year : 2000
2000 is a leap year.'''

#29.Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday ,
#2 for Monday and so on. 

'''num=(1,2,3,4,5,6,7)
days=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
x=zip(num,days)
print(tuple(x))

op/=((1, 'sunday'), (2, 'monday'), (3, 'tuesday'), (4, 'wednesday'),
     (5, 'thursday'), (6, 'friday'), (7, 'saturday'))'''

#30.Write a program to accept a number from 1 to 12 and display name of the month and days in that month
#like 1 for January and number of days 31 and so on.
'''i=int(input("enter a number : "))
if i==1:
    print("january number of days is 31")
elif i==2:
    print("february number of days is 28")
elif i==3:
    print("march number of days is 31")
elif i==4:
    print("April number of days is 30")
elif i==5:
    print("may number of days is 31")
elif i==6:
    print("june number of days is 30")
elif i==7:
    print("july number of days is 31")
elif i==8:
    print("August number of days is 31")
elif i==9:
    print("september number of days is 30")
elif i==10:
    print("october number of days is 31")
elif i==11:
    print("november number of days is 30")
elif i==12:
    print("December number of days is 31")
else:
    print("please enter 1 to 12")

op/=enter a number : 6
june number of days is 30'''
    

#31.What do you mean by statement?
'''A statement is an instruction that a Python interpreter can execute.
So, in simple words, we can say anything written in Python is a statement.
Python statement ends with the token NEWLINE character.
It means each line in a Python script is a statement.
For example, a = 10 is an assignment statement.'''

#32.Write the logical expression for the following: A is greater than B and C is greater than D

#A > B and C >D

#33.Accept any city from the user and display monument of that city. 

'''City                                 Monument 

Delhi                               Red Fort 

Agra                                Taj Mahal 

Jaipur                              Jal Mahal'''

'''city=input("enter a city name: ")

if city=="Delhi":
    print("Red Fort")
elif city=="Agra":
    print("Taj mahal")
elif city=="Jaipur":
    print("jal mahal")
else:
    print("not in the list")

op/=enter a city name: Delhi
Red Fort'''

#34.Write the output of the following if a = 9 
'''a=9
if (a > 5 and a <=10):     
    print("Hello")     
else:     
    print("Bye") 

#op Hello'''

#35.Write a program to check whether a number entered is three digit number or nonum=input("enter a num : ")
'''if len(num)==3:
    print("its a 3 digit num")
else:
    print("its not a 3 digit num")

op/=enter a num : 45
its not a 3 digit num'''

#37.Write a program to check whether a person is senior citizen or not.

'''age=int(input("enter the age of the person : "))
if age>=60:
    print("the person is a senior citizen")
else:
    print("the person is not a senior citizen")

op/=enter the age of the person : 89
the person is a senior citizen'''

#38.Write a program to find the lowest number out of two numbers excepted from user.

'''num1=int(input("enter 1st num : "))
num2=int(input("enter 2nd num : "))
if num1>num2:
    print(f"{num2} is lower")
else:
    print(f"{num1} is lower")

op/=enter 1st num : 45
enter 2nd num : 12
12 is lower'''

#39.Write a program to find the largest number out of two numbers excepted from user. 

'''num1=int(input("enter 1st num : "))
num2=int(input("enter 2nd num : "))
if num1>num2:
    print(f"{num1} is greater")
else:
    print(f"{num2} is greater")

op/=enter 1st num : 45
enter 2nd num : 21
45 is greater'''

#40.Write a program to check whether a number (accepted from user) is positive or negative. 

'''num=int(input("enter a num : "))
if num>0:
    print("it is possitive num")
else:
    print("its a negetive num")

op/=enter a num : 45
it is possitive num'''

#41.Write a program to check whether a number is even or odd. 

'''num=int(input("enter a num : "))
if num%2==0:
    print("even")
else:
    print("odd")

op/=enter a num : 45
odd'''

#42.Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

'''num=int(input("enter a num : "))
if num%2==0 and num%3==0:
    print("it is divisible by 2 and 3")
else:
    print("it is not divisible by 2 and 3")

op/=enter a num : 5
it is not divisible by 2 and 3'''

#43.Write a program to find the largest number out of three numbers excepted from user.

'''num1=int(input("enter 1st num : "))
num2=int(input("enter 2nd num : "))
num3=int(input("enter 3rd num : "))
if num1>num2 and num1>num3:
    print(f"{num1} is greater")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")

op/=enter 1st num : 45
enter 2nd num : 89
enter 3rd num : 5
89 is greater'''

#44.Accept the temperature in degree Celsius of water and check whether it is boiling or not
#(boiling point of water in 100 oC.

'''temp=int(input("enter the temperetur : "))
if temp>=100:
    print("the water is boiling")
else:
    print("the water is not boiling")

op/=enter the temperetur : 102
the water is boiling'''

#45.the age of 4 people and display the youngest one and oldest one?
'''people=input("enter the 4 people name using cumma separate :").split(",")
print("the oldest people age is :",max(people))
print("the youngest people age is :",min(people))'''

#46.Accept the following from the user and calculate the percentage of class attended: 
'''a.Total number of working days 
b.Total number of days for absent 
After calculating percentage show that, If the percentage is less than 75,
than student will not be able to sit in exam.'''

'''work_day=int(input("enter the total working day : "))
absent=int(input("enter the total absent day : "))
present=work_day - absent
per=(present/work_day)*100
if per<75:
    print("you are not able to sit  in the exam")
else:
    print("you r able to sit in the examS")

op/=enter the total working day : 100
enter the total absent day : 27
you are not able to sit  in the exam'''

#47.Accept three sides of a triangle and check whether it is an equilateral,
#isosceles or scalene triangle.

'''side1=int(input("enter the first side of tringle :"))
side2=int(input("enter the second side of tringle :"))
side3=int(input("enter the third side of tringle :"))

if side1==side2 and side1==side3:
    print("it is a equilateral triangle")
elif side1==side2 and side2!=side3:
    print("it is a isoscele or scalene triangle")
else:
    print("it is a scalene triangle")
    
op/=enter the first side of tringle :4
enter the second side of tringle :8
enter the third side of tringle :9
it is a scalene triangle'''


































































































































































































#1.Print First 10 natural numbers using while loop
'''i=1
while i<=10:
    print(i)
    i+=1'''
#2.Calculate the sum of all numbers from 1 to a given number
'''i=1
total=0
while i<=10:
    total+=i
    i+=1
print(total)
op/=55'''
#3.Write a program to print multiplication table of a given number

'''num=int(input("enter a num you want: "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

op/=enter a num you want: 9
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90'''

#4.Display numbers from a list using loop

'''lst=[2,4,8,9,6,7,5]
for i in lst:
    print(i)'''

#5.Count the total number of digits in a number

'''num=input("enter a num you want: ")
count=0
for i in num:
    count+=1
print(count)
op/enter a num you want: 456
3'''

#6Print list in reverse order using a loop

'''lst=[2,4,9,6,7,5,1]
lst1=[]
for i in range(len(lst)):
    x=lst.pop()
    lst1.append(x)
print(lst1)
op/=[1, 5, 7, 6, 9, 4, 2]'''

#7.numbers from -10 to -1 using for loop Display

'''for i in range(-10,0):
    print(i)'''

#8.Use else block to display a message “Done” after successful execution of for loop

'''for i in range(1,5):
    print("you r not done!!!")
else:
    print("Done!!!")'''


#9.Write a program to display all prime numbers within a range

'''def prime(num):
    fact=[]
    for i in range(1,num+1):
        if num%i==0:
            fact.append(i)

    if len(fact)==2:
        return "prime"
    else:
        return "notprime"

lower=int(input("the range from  :"))        
upper=int(input(" To :"))
prim=[]
for i in range(lower,upper+1):
    d=prime(i)
    if d == "prime":
        prim.append(i)
print(prim)

op/=the range from  :20
To :100
[23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]'''


#10.Display Fibonacci series up to 10 terms

'''def fib(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fib(n-1) + fib(n-2)

user_no=int(input("enter a num you want :"))
print(fib(user_no))

op/=enter a num you want :6
8'''

#11.Find the factorial of a given number

'''num=int(input("enter a num you want: "))
factorial=1
for i in range(1,num+1):
    factorial*=i
print(factorial)

op/=enter a num you want: 4
24'''

#12. Reverse a given integer number

'''num=int(input("enter a num you want: "))
x=str(num)
print(x[::-1])
y=int(x)
print(type(y))

op/=enter a num you want: 45
54
<class 'int'>'''

#13.Find the sum of the series upto n terms

'''num=int(input("enter a num: "))
total=0
for i in range(num+1):
    total+=i
print("sum of series of num is",total)
op/=enter a num: 45
sum of series of num is 1035'''


#14.Calculate the cube of all numbers from 1 to a given number
'''num=int(input("enter a num for range: "))

for i in range(1,num+1):
    cube=i**3
    print(cube)
op/=enter a num for range: 6
1
8
27
64
125
216'''

#15.Use a loop to display elements from a given list present at odd index positions

'''lst=[4,5,6,8,9,7,2,51,24,58]
for i in range(len(lst)):
    if i%2!=0:
        print(lst[i])

op/=5
8
7
51
58'''

#16.Name the keyword which helps in writing code involves condition.

#if ,elif,else,

#17.Write the syntax of simple if statement.

'''i=5
if i==5:
    print(i)'''

#18.Is there any limit of statement that can appear under an if block.

#19.Write a program to check whether a person is eligible for voting or not. (accept age from user)

'''age=float(input("enter the age of the person: "))
if age>=18:
    print("person is eligible for voting")
else:
    print("person is not eligible for voting")
op/=enter the age of the person: 45
person is eligible for voting'''


#20.Write a program to check whether a number entered by user is even or odd.

'''num=int(input("enter a num: "))
if num%2==0:
    print("the num is even")
else:
    print("the num is odd")
op/=enter a num: 58
the num is even'''

#21.a program Write to check whether a number is divisible by 7 or not.

'''num=int(input("enter a num: "))
if num%7==0:
    print("the num is divisible by 7")
else:
    print("the num is not divisible by 7")

op/=enter a num: 56
the num is divisible by 7'''

#22.Write a program to display "Hello" if a number entered by user is a multiple of five otherwise print "Bye". 

'''num=int(input("enter a num: "))
if num%5==0:
    print("Hello")
else:
    print("Bye")

op/=enter a num: 45
Hello'''

'''23.Write a program to calculate the electricity bill (accept number of unit from user) according to the following
criteria : 

            Unit                                                     Price   

First 100 units                                               no charge 

Next 100 units                                              Rs 5 per unit 

After 200 units                                             Rs 10 per unit 

(For example if input unit is 350 than total bill amount is Rs2000) '''


'''ut = int(input("Enter number of units: "))
if ut <=100:
    amt = "no charge"
elif ut >100 and ut <= 200:
    amt = (ut-100) *5
else:
    amt = 500 + (ut - 200)*10

print("Total amount to pay is ", amt)

op/=Enter number of units: 350
Total amount to pay is  2000'''

#24.Write a program to display the last digit of a number. 
#(hint : any number % 10 will return the last digit)

'''num=int(input("enter a num: "))
lstdig=num%10
print("last digit is :",lstdig)

op/=enter a num: 56
last digit is : 6'''

#25.Write a program to check whether the last digit of a number( entered by user ) is  divisible by 3 or not. 

'''num=int(input("enter a num: "))
lstdig=num%10
print("the last digit of num is: ",lstdig)
if lstdig%3==0:
    print("yes last digit is divisible by 3")
else:
    print("no last digit is not divisible by 3")

op/=enter a num: 45
the last digit of num is:  5
no last digit is not divisible by 3'''

#25.Write a program to accept percentage from the user and display the grade according to the following criteria: 
'''Marks                                    Grade 

         > 90                                         A 

         > 80 and <= 90                       B 

        >= 60 and <= 80                       C 

         below 60                                  D 



perc=int(input("enter the percentage: "))
if perc > 90:
    print("grade A")
elif perc > 80 and perc <= 90:
    print("your grade is : B")
elif perc >=60 and perc <= 80:
    print("your grade is : C")
elif perc < 60 :
    print("your grade is : D")
else:
    print("please insert currect input")

op/=enter the percentage: 45
your grade is : D'''


#26.Write a program to accept the cost price of a bike and display the road tax to be paid according to
#the following criteria : 
'''Cost price (in Rs)                                       Tax 

        > 100000                                                  15 % 

        > 50000 and <= 100000                          10% 
        <= 50000                                                  5%'''



'''bike_mrp=int(input("enter the amount of bike: "))
if bike_mrp>100000:
    print(f"the road tax is paid by the owner is {bike_mrp*(15/100)}")
elif bike_mrp>50000 and bike_mrp<=100000:
    print(f"the road tax is paid by the owner is {bike_mrp*(10/100)}")
elif bike_mrp<=50000:
    print(f"the road tax is paid by the owner is {bike_mrp*(5/100)}")

op/=enter the amount of bike: 1000
the road tax is paid by the owner is 50.0'''


#28.Write a program to check whether an years is leap year or not. 
'''year = int(input('Enter year : '))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print(year, "is a leap year.")
else :
    print(year, "is not a leap year.")

op/=Enter year : 2000
2000 is a leap year.'''

#29.Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday ,
#2 for Monday and so on. 

'''num=(1,2,3,4,5,6,7)
days=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
x=zip(num,days)
print(tuple(x))

op/=((1, 'sunday'), (2, 'monday'), (3, 'tuesday'), (4, 'wednesday'),
     (5, 'thursday'), (6, 'friday'), (7, 'saturday'))'''

#30.Write a program to accept a number from 1 to 12 and display name of the month and days in that month
#like 1 for January and number of days 31 and so on.
'''i=int(input("enter a number : "))
if i==1:
    print("january number of days is 31")
elif i==2:
    print("february number of days is 28")
elif i==3:
    print("march number of days is 31")
elif i==4:
    print("April number of days is 30")
elif i==5:
    print("may number of days is 31")
elif i==6:
    print("june number of days is 30")
elif i==7:
    print("july number of days is 31")
elif i==8:
    print("August number of days is 31")
elif i==9:
    print("september number of days is 30")
elif i==10:
    print("october number of days is 31")
elif i==11:
    print("november number of days is 30")
elif i==12:
    print("December number of days is 31")
else:
    print("please enter 1 to 12")

op/=enter a number : 6
june number of days is 30'''
    

#31.What do you mean by statement?
'''A statement is an instruction that a Python interpreter can execute.
So, in simple words, we can say anything written in Python is a statement.
Python statement ends with the token NEWLINE character.
It means each line in a Python script is a statement.
For example, a = 10 is an assignment statement.'''

#32.Write the logical expression for the following: A is greater than B and C is greater than D

#A > B and C >D

#33.Accept any city from the user and display monument of that city. 

'''City                                 Monument 

Delhi                               Red Fort 

Agra                                Taj Mahal 

Jaipur                              Jal Mahal'''

'''city=input("enter a city name: ")

if city=="Delhi":
    print("Red Fort")
elif city=="Agra":
    print("Taj mahal")
elif city=="Jaipur":
    print("jal mahal")
else:
    print("not in the list")

op/=enter a city name: Delhi
Red Fort'''

#34.Write the output of the following if a = 9 
'''a=9
if (a > 5 and a <=10):     
    print("Hello")     
else:     
    print("Bye") 

#op Hello'''

#35.Write a program to check whether a number entered is three digit number or nonum=input("enter a num : ")
'''if len(num)==3:
    print("its a 3 digit num")
else:
    print("its not a 3 digit num")

op/=enter a num : 45
its not a 3 digit num'''

#37.Write a program to check whether a person is senior citizen or not.

'''age=int(input("enter the age of the person : "))
if age>=60:
    print("the person is a senior citizen")
else:
    print("the person is not a senior citizen")

op/=enter the age of the person : 89
the person is a senior citizen'''

#38.Write a program to find the lowest number out of two numbers excepted from user.

'''num1=int(input("enter 1st num : "))
num2=int(input("enter 2nd num : "))
if num1>num2:
    print(f"{num2} is lower")
else:
    print(f"{num1} is lower")

op/=enter 1st num : 45
enter 2nd num : 12
12 is lower'''

#39.Write a program to find the largest number out of two numbers excepted from user. 

'''num1=int(input("enter 1st num : "))
num2=int(input("enter 2nd num : "))
if num1>num2:
    print(f"{num1} is greater")
else:
    print(f"{num2} is greater")

op/=enter 1st num : 45
enter 2nd num : 21
45 is greater'''

#40.Write a program to check whether a number (accepted from user) is positive or negative. 

'''num=int(input("enter a num : "))
if num>0:
    print("it is possitive num")
else:
    print("its a negetive num")

op/=enter a num : 45
it is possitive num'''

#41.Write a program to check whether a number is even or odd. 

'''num=int(input("enter a num : "))
if num%2==0:
    print("even")
else:
    print("odd")

op/=enter a num : 45
odd'''

#42.Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

'''num=int(input("enter a num : "))
if num%2==0 and num%3==0:
    print("it is divisible by 2 and 3")
else:
    print("it is not divisible by 2 and 3")

op/=enter a num : 5
it is not divisible by 2 and 3'''

#43.Write a program to find the largest number out of three numbers excepted from user.

'''num1=int(input("enter 1st num : "))
num2=int(input("enter 2nd num : "))
num3=int(input("enter 3rd num : "))
if num1>num2 and num1>num3:
    print(f"{num1} is greater")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")

op/=enter 1st num : 45
enter 2nd num : 89
enter 3rd num : 5
89 is greater'''

#44.Accept the temperature in degree Celsius of water and check whether it is boiling or not
#(boiling point of water in 100 oC.

'''temp=int(input("enter the temperetur : "))
if temp>=100:
    print("the water is boiling")
else:
    print("the water is not boiling")

op/=enter the temperetur : 102
the water is boiling'''

#45.the age of 4 people and display the youngest one and oldest one?
'''people=input("enter the 4 people name using cumma separate :").split(",")
print("the oldest people age is :",max(people))
print("the youngest people age is :",min(people))'''

#46.Accept the following from the user and calculate the percentage of class attended: 
'''a.Total number of working days 
b.Total number of days for absent 
After calculating percentage show that, If the percentage is less than 75,
than student will not be able to sit in exam.'''

'''work_day=int(input("enter the total working day : "))
absent=int(input("enter the total absent day : "))
present=work_day - absent
per=(present/work_day)*100
if per<75:
    print("you are not able to sit  in the exam")
else:
    print("you r able to sit in the examS")

op/=enter the total working day : 100
enter the total absent day : 27
you are not able to sit  in the exam'''

#47.Accept three sides of a triangle and check whether it is an equilateral,
#isosceles or scalene triangle.

'''side1=int(input("enter the first side of tringle :"))
side2=int(input("enter the second side of tringle :"))
side3=int(input("enter the third side of tringle :"))

if side1==side2 and side1==side3:
    print("it is a equilateral triangle")
elif side1==side2 and side2!=side3:
    print("it is a isoscele or scalene triangle")
else:
    print("it is a scalene triangle")
    
op/=enter the first side of tringle :4
enter the second side of tringle :8
enter the third side of tringle :9
it is a scalene triangle'''

#############################################################################

#1.WAP to reverse a number
'''num=input("enter a number : ")
for i in num:
    x=num[::-1]
print("the reverse of the num is ",int(x))

op/=enter a number : 456
the reverse of the num is  654'''

#2.WAP to count  the number  occurrence/frequency  of a 
#each character in a string .

'''st=input("enter a string : ")
count=0
for i in st:
    x=st.count(i)
    print(x,end="")

op/=enter a string : anil kumar nahak
4211221141224142'''

#3. WAP  to check length of two string is equal or not.
'''st1=input("enter 1st string : ")
st2=input("enter 2nd string : ")
if len(st1)==len(st2):
    print("equal")
else:
    print("not equal")

op/=enter 1st string : aill
enter 2nd string : anil
equal'''

#4.Python program to print even numbers up to 100

'''for i in range(1,100):
    if i%2==0:
        print(i,end=",")

op/=2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,
70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,'''

#5.Write a program in python to find greatest among three integers
      
'''num1=int(input("enter 1st num : "))
num2=int(input("enter 2nd num : "))
num3=int(input("enter 3rd num : "))
if num1>num2 and num1>num3:
    print(f"{num1} is greater")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")

op/=enter 1st num : 45
enter 2nd num : 89
enter 3rd num : 5
89 is greater'''

###########################################################################

#problem statement 26 july

'''n = int(input("enter an input : "))
if n% 2 != 0:
    print("Wierd")
elif n % 2 == 0:
    if 2<=n <=5:
        print("Not Wierd")
    elif 6<=n <20:
        print("Wierd")
    elif n>= 20:
        print("Not Wierd")

op/=enter an input : 24
Not Wierd'''
















































































































































































































        
































        


















































































    








































    





















        
        




























    
    




















        
































        


















































































    








































    





















        
        




























    
    
