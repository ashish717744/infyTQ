
#Write a python function which accepts a list of strings containing details of deposits and withdrawals made in a bank account and returns the net amount in the account.
#Suppose the following input is supplied to the function 
#["D:300","D:300","W:200","D:100"] where D means deposit and W means withdrawal,
#then the net amount in the account is 500.


#Sample Input	Expected Output
C=["D:300","D:200","W:200","D:100"]
print(', '.join(C))
#["D:350","W:100","W:500","D:1000"]	750
dt=dict(D=300,G=100)

def py(dt):
    deposit=0
    withdrawal=0
    for i in dt:
        if i=='D':
           deposit+=dt[i]
        else:
            withdrawal+=dt[i]
    print('the net amount in the account is',deposit-withdrawal)
print(py(dt))


         
