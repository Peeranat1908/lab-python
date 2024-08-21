string = input().split()
ls = []
lenght = len(string) - 2
for i in string:
    for ch in i:
        ans = ch[0] + str(lenght) + ch[-1]
print(ans)