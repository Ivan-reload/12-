with open(r'/storage/emulated/0/Download/WuT6YIZf_.txt') as f:
    data = [int(y) for y in f]

data1 = []
for num1, num2 in zip(data, data[1:]):
    u1 = abs(num1) % 3 == 0
    u2 = abs(num2) % 3 == 0
    if u1 or u2:
        data1 += [num1 + num2]
print(len(data1), max(data1))
