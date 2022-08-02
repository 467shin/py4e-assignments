name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
res = list()

for line in handle:
    if not line.startswith('From ') : continue
    line = line.split()
    line = line[5]
    line = line.split(':')
    line = line[0]
    count[line] = count.get(line, 0) + 1

for k,v in sorted(count.items()):
    tupp = (k,v)
    res.append(tupp)
    print(k,v)
    
# for k,v in count.items():
#     tupp = (k,v)
#     res.append(tupp)
#     res.sort()
#
# for kk, vv in res:
#     print(kk, vv)
