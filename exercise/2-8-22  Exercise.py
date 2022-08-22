##1.
##Calculate income tax for the given income by adhering to the below rules
##Taxable Income    Rate (in %)
##First $10,000    0
##Next $10,000    10
##The remaining    20
##Expected Output:
##
##For example, suppose the taxable income is 45000 the income tax payable is
##
##10000*0% + 10000*10%  + 25000*20% = $6000.



'''
income=int(input("enter your income : "))
if income<10000:
    print("tax is : 0")
elif income > 10000 and income < 20000:
    print(f"{(10000*(0/100))+((income-10000)*(10/100))}")
else:
    print(f"{(10000*(0/100))+(10000*(10/100))+(income-20000)*(20/100)}")'''


##enter your income : 45000
##6000.0


    
#2.Count the length of list with out using any inbuilt function.

'''
lst=input("enter the list of element :").split(",")
print(lst)
count=0
for i in lst:
    count+=1
print(count)
'''

##enter the list of element :12,45,2,11,4,66,8,9
##['12', '45', '2', '11', '4', '66', '8', '9']
##8


#3.Write a Python program to create a histogram from a given list of integers.

'''
lst = list(map(int,input().split()))
for i in lst:
    print("* "  * i)'''

##5 6 4 2 9
'''
* * * * * 
* * * * * * 
* * * * 
* * 
* * * * * * * * *
'''

###4. Take input from user and if input is string print String
##if input is integer/float print integer
##if input is mix of string and integer print Error
##HINT Can be done using ASCII code



#5.Python program to check if a string is palindrome or not

'''
n = input()
if n == n[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")'''

##praveen
##Not a palindrome

