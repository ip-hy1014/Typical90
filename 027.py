n = int(input())
l = set()
for i in range(n):
  s = input()
  if not s in l:
    l.add(s)
    print(i+1)

#別解
n = int(input())
l = set()
ans = []
for i in range(n):
  s = input()
  if s not in l:
    ans.append(i+1)
  l.add(s)
print(*ans, sep="\n")