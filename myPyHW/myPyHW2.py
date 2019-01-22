#印出小於10000的質數
def is_prime(n):
    i=2
    if(n==2):
        print('2')
    while(i <= n):
        if(n%i == 0):
            return
        if(i*i >= n):
            print(n)
            return
        i=i+1

j=2
while(j<10000):
    is_prime(j)
    j=j+1
