##Python Program to accept three distinct digits and print all possible combinations from the digits.
##
##Case 1:
##
##Enter first number:1
##Enter second number:2
##Enter third number:3
##                    1 2 3
##                    1 3 2
##                    2 1 3
##                    2 3 1
##                    3 1 2
##                    3 2 1
##
##Case 2:
##
##Enter first number:5
##Enter second number:7
##Enter third number:3
##                    5 7 3
##                    5 3 7
##                    7 5 3
##                    7 3 5
##                    3 5 7
##                    3 7 5   



d=[1,2,3]
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])


##1 2 3
##1 3 2
##2 1 3
##2 3 1
##3 1 2
##3 2 1
