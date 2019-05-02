#Write a python function which accepts a string containing a pattern of brackets and returns true if the pattern of brackets is correct. Otherwise it returns false.
#The string of brackets is correct if it satisfies the following conditions:
#1. Number of opening and closing brackets are equal.
#2. Pattern should not start with closing bracket and end with opening bracket.

#Sample Input	Expected Output
# 	False
#()((())())	True
n=str(input())
def bracket(str1):
    value=0
    value1=0
    for i in range(len(n)):
        if n[i]=='(':
            value+=1
        elif n[i]==')':
            value1+=1
    if value1==value:
        if n[0]==')' and n[-1]==')':
           return False
        else:
           return True
        return 'ok'
    
print(bracket(n))
