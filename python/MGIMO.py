
location = "home"
sleeping = False


def code():
    print("code")

def think():
    print("think")

def sleep():
    print("sleep")

for i in range (0, 365):
    if (location != "mgimo") & (sleeping != True):
        code()
    elif (location == "mgimo"):
        think()
    else:
        sleeping = True
        sleep()

    