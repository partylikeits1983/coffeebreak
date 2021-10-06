"""
You are given n words. Some words may repeat. 
For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. 
See the sample input/output for clarification. 


Sample input:

4
bcdef
abcdefg
bcde
bcdef


Sample output:

3
2 1 1

"""

from collections import Counter

def convert(string):
    l = list(string.split(" "))
    l = l[:-1]
    
    x = list(Counter(l).keys())
    unique = len(x)
    print(unique)
    
    f = list(Counter(l).values())
    frequency = ' '.join(str(i) for i in f)
    print(frequency)
    
n = int(input())
lines = ""

for i in range(0,n):
    lines+=input()+" "

convert(lines)
