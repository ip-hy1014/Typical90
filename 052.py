#https://twitter.com/e869120/status/1398409831044632576/photo/1
#因数分解
#類題 ARC107A, ABC190D
n = int(input())
a = [sum(list(map(int,input().split()))) for _ in range(n)]
mod = 10**9+7
ans = 1
for i in a:
  ans *= i
  ans %= mod
print(ans)