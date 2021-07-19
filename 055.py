import itertools


n,p,q = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      for l in range(k+1,n):
        for m in range(l+1,n):
          if a[i]*a[j]%p * a[k]%p * a[l]%p * a[m]%p % p == q:
            ans += 1
print(ans)

#別解
from itertools import combinations #組み合わせ重複なし
n,p,q = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for a,b,c,d,e in combinations(a,5):
  if a%p * b%p * c%p * d%p * e%p == q:
    ans += 1
print(ans)