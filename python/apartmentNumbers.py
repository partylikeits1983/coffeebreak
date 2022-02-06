def split(string):
    return [char for char in string]

for i in range(10,101):
    a = str(i)
    vals = split(a)
    x = int(vals[1]) - int(vals[0])
    if x > 0:
        print(i)
