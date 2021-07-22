n,m = map(int, input().split())
ans = [0] * n
for i in range(m):
  a, b = map(int, input().split())
  if a < b:
    ans[b-1] += 1
  else:
    ans[a-1] += 1
print(ans.count(1))


#https://twitter.com/e869120/status/1409644684561944579/photo/1
#類題 ABC166C, ABC163C