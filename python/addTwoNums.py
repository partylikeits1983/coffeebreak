def arraySum(a1,a2):
    l1 = len(a1)
    l2 = len(a2)
    
    val1 = ""
    val2 = ""
    
    for i in range(l1):
        val1 += str(a1[i])
        
    for i in range(l2):
        val2 += str(a2[i])
        
    i1 = int(val1[::-1])
    i2 = int(val2[::-1])
    
    result = i1 + i2
    result = stringToArray(result)
    
    return result

def stringToArray(x):
    r = str(x)
    
    reversed = r[::-1]
    
    a = []
    
    for i in reversed:
        a.append(int(i))
        
    return a

l1 = [3,5,6,2]
l2 = [3,6,4,1]

arraySum(l1,l2)
