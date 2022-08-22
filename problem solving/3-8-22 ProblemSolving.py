##Write a program to check whether the given password is valid or not .

##conisder the password to be valid if it contain at least one digit ands one capital.

##input:it will be a single line containng string

##output: valid password or invalid password

##ex:GJ22191gopi

##ouput:valid password

'''
n = input("Enter your password: ")
caps = ""
sml = ""

for i in n:
    if i.isupper():
        caps += i
    elif i.islower():
        sml += i
    elif i.isdigit():
        v = i
    
if caps and sml and v:
    print("Valid password")
else:
    print("Invalid password")'''


##Enter your password: pRavEeN29
##Valid password
