#1. WAP to print middle charector of the string
'''
char = input()
length = len(char)
middle  = length //2
print(char[middle])'''

##praveen
##v

#2. WAP to print half reverse of the string 

##Input: KNOWLEDGE
##Output: EGDELKNOW
'''
n = input()
length = len(n)
middle = length//2

reverse = n[-1:(middle):-1]

stright = n[0:(middle)]
print(reverse + stright)'''


##KNOWLEDGE
##EGDEKNOW



#3. WAP to remove all the vouels from the given string

'''
n = input()
vow = "aeiouAEIOU"
for i in n:
    if i not in vow:
        print(i,end = "")'''

        

##praveen
##prvn





##4. WAP to insert * in front of every vouels in the string.
##
##Input: BANANA
##Output: B*AN*AN*A

'''
string=input("Enter the String: ")
new_String=""
for i in string:
    if i in "aeiouAEIOU":
        new_String+="*"+i
    else:
        new_String+=i
print(new_String)'''


##Enter the String: praveen
##pr*av*e*en

##5. WAP to count number of words in the string.

'''
n = input()
sums = 0
for i in n:
    sums +=1
print(sums)'''

##praveen
##7
##6. WAP to remove extra space from the given string

'''
n = "  praveen "
for i in n:
    if i == " ":
        continue
    print(i,end = "")
'''
##praveen


##7. WAP to insert string in between the given string
##Input: Ojas technologies 
##Output: Ojas innovative technologies 

'''
n = "ojas technology"
sp = n.index(" ")
for i in n:
    if i == " ":
        print(n[:sp] + " innovative" + n[sp:])'''
    
#ojas innovative technology


##8. WAP to find the ascci value of given char

'''
n = input("Enter String ")
        
for i in n:
    print(i," -> ",ord(i))'''

##Enter String pRaVeEn
##p  ->  112
##R  ->  82
##a  ->  97
##V  ->  86
##e  ->  101
##E  ->  69
##n  ->  110

    

##9. insert ojas in front of every string 


'''n = input()

print("ojas " + n)'''

##ojas innovative technology

    
##10. insert ojas in every extra space in the string



'''
strn=input("Enter the string")
c=0
st=""
for i in range(len(strn)):
    if strn[i]==" " and c==0:
        c+=1
        st+=strn[i]
    elif strn[i]==" " and c>=1:
        st+="Ojas "
    else:
        c=0
        st+=strn[i]
print(st)'''


##Enter the stringinnovative  technology
##innovative Ojas technology
