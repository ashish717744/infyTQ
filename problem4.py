#Given a list of numbers, write a python function which returns true if one of the first 4 elements in the list is 9. Otherwise it should return false.
#The length of the list can be less than 4 also.

#Sample Input	Expected Output
#[1, 2, 9, 3, 4]	True
#[1, 2, 9]	True
#[1, 2,3,4]	False
import sys
value=[1,4,3,3,4,5,6]
def easy(value):
    count=0
    for i in range(len(value)):
        if i<=4:
            if value[i]==9:
                return True
        else :
            return False
print(easy(value))
        
