#Write a python function which accepts a list of numbers and returns true if the list contains a 2 next to a 2. Otherwise it should return false.
#Sample Input	Expected Output
#[ 1,2,1,2,3,4,5,2,2]	True
#[3,2,5,1,2,1,2]	False
n=[3,2,5,1,2,1,2]
def py(n):
    c=0
    for i in range(0,len(n)-1):
        print(n[i],n[i+1])
        if n[i]==2 and n[i+1]==2:
            c+=1
            return True
    if c!=1:
        return False
            
print(py(n))
