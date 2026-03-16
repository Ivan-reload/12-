with open(r'/storage/emulated/0/Download/J2bkK30N669.txt') as f:
    data = [int(y) for y in f]

mdata = max([y for y in data if str(y)[-2:] == '30'])

data1 = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    n = [num1, num2, num3]
    if [len(str(abs(y))) for y in n].count(4) == 0 and sum(n) > mdata:
            data1 += [sum(n)]
print(len(data1), max(data1))
