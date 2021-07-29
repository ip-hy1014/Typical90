#全探索
n = int(input())
a,b,c = map(int, input().split())
ans = 9999
for i in range(10**4):
  for j in range(10**4):
    k = n-(a*i+b*j)
    if k>=0 and k%c==0:
      ans = min(ans,i+j+(k//c))
print(ans)

#https://twitter.com/e869120/status/1383189464650981378/photo/1
#類題 ABC051B,ABC085C,ABC095C,ABC112C