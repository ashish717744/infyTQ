
#Write a python function that accepts a list of words and returns the list of integers representing the length of the corresponding words.

#Sample Input	Expected Output
#[cat, Come]   [3,4]
lt =['cat','Come']

def py(lt):
    lt1=[]
    for i in lt:
        length =len(i)
        lt1.append(length)
    return lt1
print(py(lt))
