#bit全探索
n = int(input())
ans = []
for bit in range(2**n):
  res = ""
  tmp = 0
  for i in range(n):
    if (bit >> i) & 1:
      res += "("
      tmp += 1
    else:
      res += ")"
      tmp -= 1
    if tmp < 0:
      break
  if tmp == 0:
    ans.append(res)
ans.sort()
for i in range(len(ans)):
  print(ans[i])

"""
候補となる括弧列をresとしてbitが1なら"("、0なら")"を加えていきます。

あわせて正しい括弧列の条件は"("と")"の数が同じで、左から見ていって"("の数が")”の数以上であることが挙げられます。
したがって、"("ときtmpに1を足し、")"のとき1を引いて上記の条件を見ていきました。

ループの途中でtmpが0より小さくなれば正しい括弧列にならないのでbreakして次の探索を行います。
Ｎ文字の追加が終わったあとでtmpが0なら"("と")"の数が等しいのでansにresを追加しました。
"""

#https://twitter.com/e869120/status/1377391097836544001
#類題 ABC190C,ABC197C,ABC064D
#https://www.javadrive.jp/python/num/index4.html#section1-6