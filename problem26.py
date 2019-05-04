#Given a string, write a python function to return True if the strings "mat" and "jet" appear the same number of times in the given string, else return False.
#Note: Perform case insensitive string comparison wherever necessary.

#Sample Input	Expected Output
#Jet on the Mat but mat is too long	False
#mat jet Jet Mat	True
n =str(input()).split(' ')
def py(n):
    v=0
    v1=0
    for i in range(len(n)):
        if n[i].lower()=='Jet':
            v+=1
        elif n[i].lower()=='mat':
            v1+=1
    
    if v==v1:
        return True
    else:
        return False
print(py(n))
