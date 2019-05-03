#Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.
#It should return a list in which the first value should be letter count and second value should be digit count. Ignore the spaces or any other special character in the sentence.

#Sample Input	Expected Output
#Infosys 123	[7,3]
#ABCEFG	[6,0]




l1 =input().split(' ')

v=0
v1=0
Lt=[]
for I in range(len(l1)):
    if l1[I].isnumeric()==False:
            v+=len(l1[I])
            
    elif l1[I].isnumeric()==True:
            v1 +=len(l1[I])

Lt.append(v)
Lt.append(v1)
                
print(Lt)

