#1.Write a program to print the following Patterns
'''
1 2 3 4 5 
1 2 3 4 5  
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5



a = int(input())
for i in range(1, a+1,1):
    for j in range(1,a +1,1):
        print(j, end = " ")
    print()


input
5
output

1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 '''



#2.Write a program to print the following Pattern
'''
5 4 3 2 1 
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1 
  

a = int(input())
for i in range(a, 0, -1):
    for j in range(1,a+1, -1):
        print(j, end = " ")
    print()


input
5
output
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 '''


#3. Write a program to print the following Pattern
'''
5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1

a = int(input())

for i in range(a,0,-1):
    val = (str(i)  + " ") * a
    print(val)


inout
5
output

5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1'''



#4. Write a program to print the following Pattern
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

  
a = int(input())
b = int(input())
for i in range(1, b+1):
    pattern = ""
    for j in range(1, i+1):
        pattern = pattern + str(j) + " "
    print(pattern)

input
1
5
output
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 '''



#5. Write a program to print the following Pattern
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

  
a = int(input())
b = int(input())
for i in range(1, b+1):
    pattern = ""
    for j in range(1, i+1):
        pattern = pattern + str(i) + " "
    print(pattern)


input
1
5
output
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5'''


#6. Write a program to print the following Pattern
'''
1 
2 3  
4 5 6 
7 8 9 10 
11 12 13 14 15

a = int(input())
b = int(input())

k = a
for row in range(1, b+1):
    pattern = ""
    for col in range(row):
        pattern = pattern + str(k) + " "
        k +=1
    print(pattern)

input
1
5
output
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15'''



#7.  Write a program to print the following Pattern
'''5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1


n = int(input())
for i in range(n):
    for j in range(i+1):
        print(n-i, end = " ")
    print()

5

5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1
'''




#8.Write a program to print the following Pattern
'''
1 
2 3 
3 4 5 
4 5 6 7 
5 6 7 8 9



number=int(input("Enter the number"))
for rows in range(1,number+1):
    temp=rows
    for columns in range(0,rows):
        print(temp ," ",end="")
        temp+=1
    print("")

Enter the number5
1  
2  3  
3  4  5  
4  5  6  7  
5  6  7  8  9 '''

#9.Write a program to print the following Pattern

'''
A  
B  C  
D  E  F  
G  H  I  J  
K  L  M  N  O 
number=int(input("Enter the number"))
temp=65
for rows in range(1,number+1):
    for columns in range(0,rows):
        print(chr(temp)," ",end="")
        temp+=1
    print("")


Enter the number5
A  
B  C  
D  E  F  
G  H  I  J  
K  L  M  N  O '''




#10. Write a program to print the following Pattern
'''* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *'''



'''n = int(input())
for i in range(1, n+1):
    print(n * "* ")


input
5
output

* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *
'''



#11. Write a program to print the following Pattern
'''
* 
* * 
* * * 
* * * * 
* * * * *


n = int(input())
for i in range(1, n+1):
    print("* " * i)



#input
    5

#output
* 
* * 
* * * 
* * * * 
* * * * *
'''


#12. Write a program to print the following Pattern
'''
* * * * * 
*       * 
*       * 
*       * 
* * * * *


n = int(input())
for i in range(n):
    if (i == 0)or (i == (n - 1)):
        print("* " * n)
    else:
        no_of_spaces = "  " * (n -2)
        print("* " + no_of_spaces + "* ")


input
5
output
* * * * * 
*       * 
*       * 
*       * 
* * * * *
'''


#13.Write a program to print the following Pattern
'''   * 
    * * * 
  * * * * * 
* * * * * * *




n = int(input())
for i in range(1, n+1):
    if i %2 !=0:
        spaces = " " * (n -i)
        stars = "* " * i
        print(spaces + stars)

input
7
output

      * 
    * * * 
  * * * * * 
* * * * * * * 
'''


#14.Display Multiplication Table in given range using Nested for loop


'''
for rows in range(1,5):
       for columns in range(1,5):
           print(rows*columns," ",end="")
       print("")


1  2  3  4  
2  4  6  8  
3  6  9  12  
4  8  12  16   '''   

#15.Display Prime Numbers in the given range using nested for loops 

'''
print("List of prime numbers from 1 to 100 :")
for n in range (1, 44):
    count = 0
    t = n//2
    for i in range(2, (t + 1)):
        if(n % i == 0):
            count = count + 1
            break
    if (count == 0 and n > 1):
        print(" %d" %n, end = '  ')

List of prime numbers from 1 to 100 :
 2   3   5   7   11   13   17   19   23   29   31   37   41   43  '''

#16  .Write a program to print the following Pattern
'''
       1
     3 2    
   6 5 4
10 9 8 7'''
'''
m = int(input())
n = int(input())
k = m
for i in range(1,n+1):
    for j in range(1, i+1):
        print(" ", end = " ")
    for j in range(i,0,-1):
        print(k, end = " ")
        k +=1
    print()


1
4
      1 
    2 3 
  4 5 6 
7 8 9 10''' 


#17. Write a program to print the following Pattern
'''
10 9 8 7
   6 5 4
     3 2
       1



t=10
s=0
for i in range(4,0,-1):
    print(' '*s*2,end=' ')
    for j in range(1,i+1):
        print(t,end=' ')
        t-=1
    s=s+1
    print()


10 9 8 7 
   6 5 4 
     3 2 
       1 '''



n = int(input())
for i in range(0, n):
    if i == 0 and i == (n -1):
        print("* " * n)
    else:
        spaces = "  " * (n -2)
        print("* " + spaces + "* ")
        
        



    
