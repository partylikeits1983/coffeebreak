# leet code medium (this could be an easy problem)
# obviously there are optimizations that could be made...
class Solution:
    def reverse(self, x: int) -> int:
        
        # init empty str
        y = ""

        # init bool
        negative = False

        # negative check and convert to str
        if x < 0:
            negative = True
            x *= -1
            x = str(x)

        else:
            negative = False
            x = str(x)

        # reverse str
        for i in range(len(x)):
            z = len(x)
            n = z - i
            n -= 1
            y += x[n]

        # convert to int
        y = int(y)

        # if negative multiply by -1
        if negative == True:
            y *= -1
            
        # if reversal is larger than 2**31 - 1 return as 0
        if abs(y)>2147483647:
            return 0
        else:
            return y
          
