#https://twitter.com/e869120/status/1395873457259225091/photo/1
#同じ意味のものをまとめて考える
#類題 ABC089C, ABC200C, ABC194C, ABC164D, AGC023A

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
ans = 0
a_l,b_l,c_l = [0]*46,[0]*46,[0]*46
for i in range(n):
  A = a[i]%46
  B = b[i]%46
  C = c[i]%46
  a_l[A] += 1
  b_l[B] += 1
  c_l[C] += 1
for i in range(46):
  for j in range(46):
    for k in range(46):
      if (i+j+k)%46 == 0:
        ans += a_l[i] * b_l[j] * c_l[k]
print(ans)