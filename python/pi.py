# Calculating Pi for fun

# only for calculating error
import math

# Gregory-Leibniz Series:
# not precise enough
def GLSpi(x):

    odd = []
    pi_div_4 = []

    for i in range(x):
        if i % 2 == 1:
            odd.append(i)

    for i in range(len(odd)):
        if i % 2 == 0:
            odd[i] = odd[i]
        else:
            odd[i] = -odd[i]

    for i in range(len(odd)):
        pi_div_4.append(1/odd[i])

        print(str(i/len(odd)*100) + "% done calculating GL series")

    return sum(pi_div_4) * 4


# Nilakantha Series
def NSpi(x):

    even = []
    vals = []

    n = {
        0:0,
        1:0,
        2:0
    }

    pi = 3

    for i in range(1,x):
        if i % 2 == 0:
            even.append(i)

    for i in even:
        n[0] = i
        n[1] = i+1
        n[2] = i+2

        vals.append(n.copy())

    for i in range(len(even)):
        if i % 2 == 0:
            pass
        else:
            vals[i][0] *= -1

    for i in range(len(vals)):

        x = 1

        for j in range(3):
            x *= vals[i][j]

        pi += 4 / x
        
        print (str(i/len(vals)*100) + "% done calculating N series")


    return pi


x = int(input())


GLSpi = GLSpi(x)
NSpi = NSpi(x)


print("Gregory-Leibniz Series PI: " + str(GLSpi) + " error " + str(100 - (GLSpi/math.pi)*100) + "%")
print("Nilakantha Series PI: " + str(NSpi) + " error " + str(abs(100 - (NSpi/math.pi)*100)) + "%")
