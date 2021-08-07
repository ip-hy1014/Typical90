#https://twitter.com/e869120/status/1392612322410057729/photo/1
#類題 ABC169B, ABC185C
#オーバーフロー

import math
a,b  = map(int,input().split())
def my_lcm(x, y):
  return (x * y) // math.gcd(x, y)
if my_lcm(a, b) > 10**18:
  print("Large")
else:
  print(my_lcm(a, b))

#別解
import math
a,b = map(int,input().split())
ans = a*b // math.gcd(a,b)
if ans > 10**18:
  print("Large")
else:
  print(ans)