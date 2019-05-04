
#Write a Python function which accepts a string and returns a string made of the first 2 and the last 2 characters of the given string.
#If the string length is less than 2, return -1.

#Note: If the string length is equal to 2, consider the 2 characters to be the first as well as the last two characters.


#Sample Input	Expected Output
#w3resource	w3ce
#w3	w3w3
#A	-
n =str(input())
def py(n):
    st=''
    if len(n)==2:
        st+=n*2
        return st
    elif len(n)<2:
        return -1
    else:
        st+= n[:2]+n[-2::]
        return st
print(py(n))
        
            
