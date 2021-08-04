#順列全探索
import sys
input = sys.stdin.readline
from itertools import permutations
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
xy = [list(map(int,input().split())) for _ in range(m)]

grid = [[True] * n for _ in range(n)]
# 仲の悪い組だけFalseにする
for i in range(m):
    grid[xy[i][0] - 1][xy[i][1] - 1] = False
    grid[xy[i][1] - 1][xy[i][0] - 1] = False

ans = 10 ** 18

for i in permutations(range(n)):
    Bool = True
    for j in range(n - 1):
        if not grid[i[j]][i[j + 1]]:
            Bool = False
            break

    cnt = 0 # リレーが可能な時の合計時間
    if Bool:
        for j in range(n):
            cnt += a[i[j]][j]
        ans = min(ans, cnt)

if ans == 10 ** 18:
    print(-1)
else:
    print(ans)

#別解
import itertools

n = int(input())

A = []
for i in range(n):
    array = list(map(int, input().split()))
    A.append(array)

m = int(input())

disc = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    x, y = map(int,input().split())
    disc[x-1][y-1] = 1
    disc[y-1][x-1] = 1

# nまでの順列を作成
per_list = list(itertools.permutations(range(n)))

ans = int(1e9)
flag = False
for i in per_list:
    tmp = 0
    for j in range(n):
        if j < n-1 and disc[i[j]][i[j+1]] == 1:
            break
        tmp += A[i[j]][j]
    else:
        ans = min(ans, tmp)
        flag = True

if flag:
    print(ans)
else:
    print(-1)

#https://twitter.com/e869120/status/1390074137192767489/photo/1
#類題 ABC183C, ABC145C, ABC150C, ABC054C
