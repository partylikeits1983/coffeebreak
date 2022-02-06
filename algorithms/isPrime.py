import datetime 

def isPrime(n):
    flag = True
    for i in range(2, n):

        if (n % i) == 0:
            # if factor is found, set flag to True
            flag = False
            # break out of loop
    return flag

t1 = datetime.datetime.now()
r = isPrime(int(input("Enter a positive integer: \n")))
t2 = datetime.datetime.now()

time = t2 - t1
print(r)
print(time.microseconds)