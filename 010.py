#https://twitter.com/e869120/status/1380652465834532865/photo/1
"""
学籍番号L番からR番までの生徒の合計得点はS(R)-S(L-1)で計算できる
"""
n = int(input())
C = [0]*(n+1)
P = [0]*(n+1)
c1 = 0 #1組
c2 = 0 #2組
for i in range(n):
  c,p = map(int,input().split())
  if c == 1:
    c1 += p
  else:
    c2 += p
  C[i+1] = c1 #累積和
  P[i+1] = c2 #累積和
q = int(input())
for _ in range(q):
  l,r = map(int,input().split())
  print(C[r]-C[l-1], P[r]-P[l-1])