#Write a python function to print the given number of diagonal lines of stars.
#Sample input: 5

#Expected output: 
#* 
#.* 
#..* 
#...* 
#....*
n=int(input())
def py(n):
    for i in range(n):
        if i==0:
            print('*')
        print('.' * i,'*')
print(py(n))
