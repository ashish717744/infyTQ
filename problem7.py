#Given two numbers, write a python function which returns true if first number is a seed of second number. Otherwise it returns false.
#A number X is said to be a seed of number Y, if multiplying X by its each digit equates to Y

#For example, 123 is a seed of 738 as 123*1*2*3 = 738.


#Sample Input	Expected Output
#123,738	True
#45,1000	False
n =str(input())
n1=int(n)
n=list(n)
m =int(input())


def py(n1,n,m):
   count=0
   for i in range(len(n)):
       count +=n1*int(n[i])
   if count==m:
        return ( 'it is a seed of second no')
   else:
        return('its not a seed of second no')
print(py(n1,n,m))
