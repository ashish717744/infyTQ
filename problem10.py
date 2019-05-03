#Write a Python function which generates and returns a dictionary where the keys are numbers between 1 and n (both inclusive) and the values are square of keys.
#Sample Input	Expected Output
#10	{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
n=int(input())
dt={}
for i in range(n+1):
      dt[i]=i*i
print(dt)
