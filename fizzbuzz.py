import datetime

p1 = datetime.datetime.now()
fizzbuzz = 0

def num(x):
    for i in range(1,x):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "fizzbuzz")
            global fizzbuzz
            fizzbuzz += 1 

        elif i % 3 == 0:
            print(i, "fizz")
        elif i % 5 == 0:
           print(i, "buzz")

def define():
    x = input()
    x = int(x)
    num(x)

define()

print("the number of fizzbuzzes in the set:", fizzbuzz)

p2 = datetime.datetime.now()
time = p2 - p1

print(time)
