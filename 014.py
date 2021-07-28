#ソートして貪欲法
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 0
for i in range(n):
  ans += abs(a[i]-b[i])
print(ans)

#https://twitter.com/e869120/status/1382478816627478530/photo/1
#類題 ABC091C, ABC131D