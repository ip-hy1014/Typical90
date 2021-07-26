#二分探索
from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]
a.sort() #二分探索をするために昇順にソートする
for i in range(q):
  index = bisect_left(a,b[i])
  if index == 0: #最小値
    print(a[0]-b[i])
  elif index == n: #最大値
    print(b[i]-a[-1])
  else:
    print(min(b[i]-a[index-1],a[index]-b[i]))

#https://twitter.com/e869120/status/1379565222541680644/photo/1
#類題 ABC077C,AOJ ALDS1-4-B
#https://qiita.com/ta7uw/items/d6d8f0ddb215c3677cd3