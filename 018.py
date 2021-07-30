#三角関数
import math
t = int(input())
l,x,y = map(int, input().split())
q = int(input())
for i in range(q):
    e = int(input())
    theta = e / t * 360 #度数法
    e8_x, e8_y, e8_z = 0, -l / 2 * math.sin(math.radians(theta)), l / 2  - l / 2 * math.cos(math.radians(theta))
    dist = math.sqrt((e8_x - x) ** 2 + (e8_y - y) ** 2 + (e8_z - 0) ** 2)
    ans = math.degrees(math.asin(e8_z / dist))
    print(ans)

#https://twitter.com/e869120/status/1384276005330690049/photo/1
#類題 ABC168C,ABC197D,ABC144D
#https://note.nkmk.me/python-math-sin-cos-tan/