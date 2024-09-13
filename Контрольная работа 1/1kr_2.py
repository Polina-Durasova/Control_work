"""2. По данному числу n вычислите сумму 1+1/2^2+1/3^2+...+1/n^2."""
n=int(input())
if n<0:
    print('')
else:
    counter=1
    sum=0
    while counter<=n:
        sum+=1/counter**2
        counter+=1
    print(sum)