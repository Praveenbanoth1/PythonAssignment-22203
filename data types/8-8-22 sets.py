##1.  Add a list of elements to a given set



'''
list_1 = list(map(int, input().split()))  #[1,6,7,8,9]

sets = set(map(int, input().split()))  #{1,2,3,4,5}

for i in list_1:
    sets.add(i)
print(sets)'''

##1 2 3 4
##{1, 2, 3, 4, 5, 7, 9}



##2. Return a set of identical items from a given two Python

'''
set_1 = {1,2,3,4,5,6}
set_2 = {2,4,6,8,10}
print(set_1.intersection(set_2))'''


##{2, 4, 6}


##3.Returns a new set with all items from both sets by removing duplicates


'''
set_1 = {1,2,3,4,5,6,7,8,9,10}
set_2 = {3,5,6,7,8,9,11,12,15}

print(set_1.union(set_2))'''

##{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15}

'''
set_1 = {1,2,3,4,1,5,3,6,7,3,9,6}
print(set_1)'''

##{1, 2, 3, 4, 5, 6, 7, 9}


##4.Given two Python sets, update first set with items that exist only in the first set and not in the second set.


'''
set_1={"HITMAN","GABBAR","KING","CLASSY","SPIDY","KUNGFU"}
set_2={"KUNGFU","SPIDY","CLASSY"}
for i in set_2:
    if i in set_1:
        set_1.remove(i)
print(set_1)'''


##{'HITMAN', 'KING', 'GABBAR'}


##5.Remove 10, 20, 30 elements from a following set at once

'''
n = {10,20,30,40,50,60}
n2 = {10,20,30}
n1 = n.difference(n2)
print(n1)'''

##{40, 50, 60}


##6.Return a set of all elements in either A or B, but not both



'''set_1={"HITMAN","GABBAR","KING","CLASSY","SPIDY","KUNGFU"}
set_2={"KUNGFU","SPIDY","CLASSY"}

set_3 = set_1.symmetric_difference(set_2)
print(set_3)'''


##{'HITMAN', 'GABBAR', 'KING'}


##7.Determines whether or not the following two sets have any elements in common. If yes display the common elements

'''
set1={"HITMAN","GABBAR","KING","CLASSY","SPIDY","KUNGFU"}
set2={"KUNGFU","SPIDY","CLASSY"}
if set1.isdisjoint(set2):
    print("Two sets have no items in common")
else:
    
    print(set1.intersection(set2))'''


##{'KUNGFU', 'SPIDY', 'CLASSY'}


##8. Update set1 by adding items from set2, except common items



'''
set_1={"HITMAN","GABBAR","KING","CLASSY","SPIDY","KUNGFU"}
set_2={"KUNGFU","SPIDY","CLASSY"}

set_3 = set_1.difference(set_2)
print(set_3)

set_3 = set_1 - set_2
print(set_3)'''


##{'KING', 'GABBAR', 'HITMAN'}
##{'GABBAR', 'HITMAN', 'KING'}

##9. Remove items from set1 that are not common to both set1 and set2


'''
set_1={"HITMAN","GABBAR","KING","CLASSY","SPIDY","KUNGFU"}
set_2={"KUNGFU","SPIDY","CLASSY"}

set_3 = set_1.intersection(set_2)
print(set_3)'''

##{'CLASSY', 'SPIDY', 'KUNGFU'}



##10.Write a Python program to check if a given set is superset of itself and superset of another given set


'''
set1 = {1,2,3,4,5,6,7,8,9}
set2= {3,4,1,4,6,8,6}

if set1.issuperset(set2):
    print("Yes")
else:
    print("No")'''

##Yes



##11.Write a Python program to check a given set has no elements in common with other given set



'''set1={"HITMAN","GABBAR","KING","CLASSY","SPIDY","KUNGFU"}
set2={"KUNGFU","SPIDY","CLASSY"}
set3 = {"SIRAJ"}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))'''


##False
##True

##12.Write a Python program to remove the intersection of a 2nd set from the 1st set.


'''
set1={"HITMAN","GABBAR","KING","CLASSY","SPIDY","KUNGFU"}
set2={"KUNGFU","SPIDY","CLASSY"}

set1.difference_update(set2)
print(set1)'''


{'HITMAN', 'KING', 'GABBAR'}

##13. Perform all sets methods by taking an example of your own.





