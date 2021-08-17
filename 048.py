#https://twitter.com/e869120/status/1396960059796582400/photo/1
#上界と下界を見積もる
#類題 ABC141D, ARC115C, ARC119B
n,k = map(int,input().split())
ans = 0
l = []
for _ in range(n):
  a,b = map(int,input().split())
  l.append(b)
  l.append(a-b)
l.sort(reverse=True)
for i in range(k):
  ans += l[i]
print(ans)

"""
1分で獲得できる部分点(b)と，残りの1分で満点を取りにいく(a-b)で考えてリストを作成．→満点で考えるのではなく分割する．
降順にしたリストをk分で上から貪欲．
"""