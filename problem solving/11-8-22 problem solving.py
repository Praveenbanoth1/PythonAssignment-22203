##You're writing code to control your town's traffic lights.
##You need a function to handle each change from green, to yellow, to red, and then to green again.


##Complete the function that takes a string as an argument representing the current state of the light
##and returns a string representing the state the light should change to.


##For example, when the input is green, output should be yellow.


##Test Case 1
##Input
##Green
##Output
##Yellow


##Test Case 2
##Input
##Red
##Output
##Green


'''ls = list(map(str,input().split()))
v = input()
for i in ls:
    if v =="Green":
        if i == v:
            print("Yellow")
    elif v == "Red":
        if i == v:
            print("Green")
    elif v == "Yellow":
        if i == v:
            print("Red")
    else:
        print("Error")'''


##Red Yellw Green
##Green
##Yellow
