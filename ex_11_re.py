import re
h = open('py4e-data.txt')
num = list()

for line in h:
    line = re.findall('[0-9]+', line)
    for n in line:
        n = int(n)
        num.append(n)

print(sum(num))
