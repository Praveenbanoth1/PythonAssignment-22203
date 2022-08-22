# 1. WAP for eligibility of a canditate voter id,

'''voter_age = int(input("Enter Your Age: "))

if voter_age >= 18  and voter_age <= 80:
    print("You Are Eligeble")
else:
    print("You are NOt Eligeble")


#input   Enter Your Age: 55
#output  You Are Eligeble'''

#======================================================================================================================================================


#2. WAP for calculating student marks in 5-subjects,and find grades,(suppose grade A,B,C and Fail)

#model-1

'''sub_1 = int(input("Subject 1: "))
sub_2 = int(input("Subject 2: "))
sub_3 = int(input("Subject 3: "))
sub_4 = int(input("Subject 4: "))
sub_5 = int(input("Subject 5: "))

if ((sub_1>= 80)and(sub_2>= 80)and(sub_3>= 80)and(sub_4 >= 80)and(sub_5>= 80)) :
    print("A Grade")
elif ((sub_1>= 60)and(sub_2>= 60)and(sub_3>= 60)and(sub_4 >= 60)and(sub_5>= 60)) :
    print("B Grade")
elif ((sub_1>= 40)and(sub_2>= 40)and(sub_3>= 40)and(sub_4 >= 40)and(sub_5>= 40)) :
    print("C Grade")
else:
    print("Fail")


#inputs
Subject 1: 67
Subject 2: 44
Subject 3: 66
Subject 4: 34
Subject 5: 11
#output
Fail'''

#model-2


'''sub_1 = int(input("Subject 1: "))
sub_2 = int(input("Subject 2: "))
sub_3 = int(input("Subject 3: "))
sub_4 = int(input("Subject 4: "))
sub_5 = int(input("Subject 5: "))

total_marks = sub_1 + sub_2 + sub_3 + sub_4 + sub_5

if total_marks >= 400:
    print("A grade  Keep doing that")

elif total_marks >= 300:
    print("B grade work hard")
elif total_marks >= 250 :
    print("c Grade poor concentrate on studies")
else:
    print("Fail Give your college address")
'''


#======================================================================================================================================================



#3. WAP for finding  even or odd number using (if .. else ... condition)?

'''number = int(input("Enter a NUmber : "))

if number % 2==0:
    print("Even")
else:
    print("Odd")

#input   Enter a NUmber : 77
#output  Odd'''


#======================================================================================================================================================



#4. WAP calculating area of a circle, result in positive integers only not in float values


'''radius = int(input("Enter Your Number: "))

pi = 3.14

area_of_circle = pi * (radius **2)
print("Area of Circle is: ",int(area_of_circle))

#input   Enter Your Number: 33
#output  Area of Circle is:  3419'''




#======================================================================================================================================================



#5. WAP for finding  variables A and B are having the same memory location?


'''a = int(input("Enter your code: "))
b = int(input("Enter your code: "))
if id(a) == id(b):
    print("Same Location")
else:
    print("No")


#input
Enter your code: 12
Enter your code: 89
#output
No'''



#======================================================================================================================================================



# Problem statement.


'''number = int(input("Enter A Number in between 1 to 20: "))
if 1 <= number < 20:
    for i in range(number):
        print(i ** 2)
else:
    print("Given number is outof range. please enter a proper number.")


#input    Enter A Number in between 1 to 20: 78
#output   Given number is outof range. please enter a proper number.'''


#======================================================================================================================================================



