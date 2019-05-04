#Given a list of numbers, write a python function to exchange the first n/2 elements of a list with the last n/2 elements. The function should return the new list.
#n represents the number of elements in the list. Assume that it will always be even.


#Sample Input	Expected Output
#[1,2,3,4,5,6,7,8,9,10]	[10,9,8,7,6,1,2,3,4,5]
n=input()
def py(n):
    n1=[]
    l=len(n)/2
    n1.append(l)
    n1.append(n[:l])
    return n1
print(py(n))
