varible = {}
n = []
print('Enter varibles and values')
while True:
    values = input()
    if values == '-1':
        break
    values = values.split(' = ')
    varible["{" + values[0] + "}"] + values[1]
print('Enter your program:')
while True:
    program = input()
    if program == '-1':
        break
    