#https://twitter.com/e869120/status/1395148057730187265/photo/1
#見かけ上の変化をメモ
#類題 ABC199C, ABC189E

from collections import deque
n,q = map(int,input().split())
a = deque(list(map(int,input().split())))
for i in range(q):
  t,x,y = map(int,input().split())
  if t == 1:
    a[x-1],a[y-1] = a[y-1],a[x-1]
  elif t == 2:
    b = a.pop() #末尾を削除し，その要素を返す
    a.appendleft(b) #先頭に要素を挿入
  else:
    print(a[x-1])


#TLE
from collections import deque
n,q = map(int,input().split())
a = list(map(int,input().split()))
for i in range(q):
  t,x,y = map(int,input().split())
  if t == 1:
    a[x-1],a[y-1] = a[y-1],a[x-1]
  elif t == 2:
    a = deque(a)
    a.rotate(1)
  else:
    print(a[x-1])


