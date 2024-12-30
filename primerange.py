def prime(n):
    fc=0
    for i in range(1,n+1):
        if(n%i==0):
            fc+=1
    if fc==2:
        return True
    else:
        return False
#print(10)
#prime(10)
def primerange(s,e):
    for i in range(s,e+1):
        if(prime(i)==True):
            print(i,end=' ')
s = int(input())
e = int(input())
primerange(s,e)
