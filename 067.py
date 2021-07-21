#方針: 8進法を10進法に変換後，10進法を9進法に変換する
def ToNine(num): #10進数を9進数に変換する
    nine = ""
    while num > 0:
        nine += str(num % 9)
        num //= 9
    return int(nine[::-1])

n,k = map(int,input().split()) # ８進数の数字と交換回数
if n == 0: #コーナーケース
    exit(print(0))
eight = n
for i in range(k):
    # 8進数を10進数に変換する
    a = int(str(eight), 8)

    # 10進数を9進数に変換する
    b = ToNine(a)

    # 変換した9進数の中に8があれば、5に直す
    c = ""
    for j in range(len(str(b))):
        if str(b)[j] == "8":
            c += "5"
        else:
            c += str(b)[j]
    # intに戻す
    c = int(c)
    eight = c
print(eight)

#類題
#ABC186C
#ABC171C
#ABC105C