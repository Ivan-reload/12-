with open(r'/storage/emulated/0/Download/yUJ1meZIf.txt') as f:
    data = [int(y) for y in f]

mdata = max([y for y in data if len(str(y)) == 5 and str(y)[-1] == '3'])

data1 = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = str(num1)[-1] == '3'
    u2 = str(num2)[-1] == '3'
    u3 = str(num3)[-1] == '3'
    if u1 or u2 or u3:
        n = num1 + num2 + num3
        if n <= mdata:
            data1 += [n]
print(len(data1), max(data1))
