
#Write a python function which accepts a list of numbers and returns true, if 1, 2, 3 appears in sequence in the list.
#Otherwise, it should return false.

#Sample Input	Expected Output
#[1, 1, 2, 3, 1]	True
#[1, 1, 2, 4, 3]	False#

lt=input()
#def py1(lt):
value=1
for i in range(0,len(lt)):
    if lt[i]==value and value<4:
        value+=1
    else:
        pass
if value ==3:
    print(True)
else:
    print(False)
                   
        

