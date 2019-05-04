#Given two positive integers. Write a python function to return the greatest common divisor of the given numbers.
#Sample Input	Expected Output
#14 and 35	7
#800 and 2800	400

n1 =int(input())
n2=int(input())
def py(n1,n2):
    lt=[]
    if n1<n2:
       for i in range(1,n1+1):
            if n1%i==0 and n2%i==0:
                lt.append(i)
    elif n2<n1:
       for i in range(1,n2+1):
            if n1%i==0 and n2%i==0:
                lt.append(i)
    else: 
        return n1
    return lt[-1]
print(py(n1,n2))
            
    
