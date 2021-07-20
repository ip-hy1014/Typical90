q = int(input())
d = []
for i in range(q):
  t,x = map(int, input().split())
  if t == 1:
    d.insert(0,x) #第一引数に0を指定することでリストの先頭に要素を追加
  elif t == 2:
    d.append(x)
  else:
    print(d[x-1])

#別解
from collections import deque
q = int(input())
d = deque()
for i in range(q):
  t,x = map(int, input().split())
  if t == 1:
    d.appendleft(x)
  elif t == 2:
    d.append(x)
  else:
    print(d[x-1])