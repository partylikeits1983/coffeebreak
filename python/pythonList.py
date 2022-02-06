#!/usr/bin/env python

L = []

# N = int(raw_input())
N = int(input("# of commands: "))

# delete this function for hacker rank
def raw_input():
    command = input()
    return command

for i in range(0, N):
    tokens = raw_input().split()
    n = 0
    
    if tokens[0] == 'insert':
        L.insert(int(tokens[1]), int(tokens[2]))
         
    elif tokens[0] == 'print':
         print(L)
            
    elif tokens[0] == 'remove':
        L.remove(int(tokens[1]))
         
    elif tokens[0] == 'append':
        tokens.remove(tokens[0])

        for i in tokens:
            L.append(int(tokens[n]))
            n += 1
             
    elif tokens[0] == 'sort':
        L.sort()
         
    elif tokens[0] == 'pop':
        L.pop()
         
    elif tokens[0] == 'reverse':
        L.reverse()
        
    else:
        print("command not recognized")
        
