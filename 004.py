h,w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
list_h = [sum(i) for i in a]
list_w = [sum(i) for i in zip(*a)]
for i in range(h):
  for j in range(w):
    print(list_h[i] + list_w[j] - a[i][j])