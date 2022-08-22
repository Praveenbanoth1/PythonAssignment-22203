##1.Python Program to Print the Natural Numbers Summation Pattern
##
##Python Program to Print the Natural Numbers Summation Pattern

##Output:

##Case 1:
##Enter a number: 4
##1 = 1
##1 + 2 = 3
##1 + 2 + 3 = 6
##1 + 2 + 3 + 4 = 10
 
##Output:
##Case 2:
##Enter a number: 5
##1 = 1
##1 + 2 = 3
##1 + 2 + 3 = 6
##1 + 2 + 3 + 4 = 10
##1 + 2 + 3 + 4 + 5 = 15


'''
n = int(input())
for i in range(1, n+1):
    c = 0
    for j in range(1, i+1):
        c +=j
        if  j < i:
            print(j, " + ", sep = "", end = "")
        else:
            print(j, sep = "", end = "")
    print("=", c , sep = "")'''


##4

##1=1
##1 + 2=3
##1 + 2 + 3=6
##1 + 2 + 3 + 4=10
