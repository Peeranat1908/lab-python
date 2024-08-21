txt = input()
num = int(input())

lenght = len(txt)
if num > 0:
    num_str = txt[-num:] + txt[:-num]
elif num < 0:
    num = abs(num)
    num_str = txt[num:] + txt[:num]
else:
    num_str = txt

print(num_str)
