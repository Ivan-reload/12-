# 23747
with open(r'5SgcHpmEiG.txt') as f:
    data = [list(map(int, x.split(','))) for x in f]

for line in data[::-1]:
    if sorted([line.count(x) for x in set(line)]) == [1, 1, 1, 1, 3]:
        if sum((x for x in line if line.count(x) == 1))/4 <= [x for x in line if line.count(x) == 3][0]:
            print(sum(line))
            break



# 4697
with open(r'PUSCp2_bp.txt') as f:
    data = [list(map(int, x.split(','))) for x in f]

k = 0
for line in data:
    if sorted([line.count(x) for x in set(line)]) == [1, 1, 1, 1, 2]:
        if sum((x for x in line if line.count(x) == 1))/4 <= sum((x for x in line if line.count(x) == 2)):
            k += 1
print(k)



# 19241
with open(r'OZyftw5RLF.txt') as f:
    data = [list(map(int, x.split(','))) for x in f]

k = 1
for line in data:
    if sorted([line.count(x) for x in set(line)]) == [1, 3, 3]:
        if sum(x for x in line if line.count(x) == 3)/6 < [x for x in line if line.count(x) == 1][0]:
            print(k)
    k += 1
