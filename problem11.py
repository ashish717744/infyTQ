#Write a python function which accepts a sentence and returns a list in which first value is the count of upper case letters and second value is the count of lower case letters in the sentence. Ignore spaces, numbers and other special characters if any.

#Sample Input	Expected Output
#Hello world!	[1,9]
#Welcome to Mysore	[2,13]
y =str(input())
def py(y):
  lt=[]
  upper =0
  lower =0
  for i in range(len(y)):
     
      if y[i].isnumeric()!=True:
          if y[i].isupper()==True:
                upper+=1
                #return upper
          elif y[i].islower()==True:
                lower+=1
               # return lower
          else:
              pass
              
  lt.append(upper)
  lt.append(lower)
  print(lt)
print(py(y))
