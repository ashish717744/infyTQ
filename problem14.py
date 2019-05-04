#Write a python function to find and display the five digit number in which the first digit is two more than the second,
#the second digit is two more than the third, the fourth digit is two less than the third, and the last digit is two more than the fourth.
#The sum of the third, fourth, and fifth digits equals the first. The sum of all the digits is 19.

def py():
   for i in range(10000,99999,1):
      n =list(str(i))
      if int(n[0])==int(n[2])+int(n[3])+int(n[4]):
         if int(n[0])==int(n[1])+2:
            if int(n[1])==int(n[2])+2:
               if int(n[2])-2==int(n[3]):
                   if int(n[4])==int(n[3])+2: 
                       return i
print(py())
        
