#Write a python function to find out whether a number is divisible by the sum of its digits. If so return True,else return False.
#Sample Input	Expected Output
#42	True
#66	False
n=(str(input()))
l=int(n)
n=list(n)
def py(n):
    st=0
    for i in range(len(n)):
        st+=int(n[i])
    v=l%st
    v1=l/st
    if l%st==0 and v+v1*st==l:
        return True      
    else:
        return False
print(py(n))
