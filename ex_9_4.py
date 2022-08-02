#name = input("Enter file:")
#if len(name) < 1:
#    name = "mbox-short.txt"
handle = open("mbox-short.txt")

count = dict()
most1 = None
most2 = None

for line in handle:
    if not line.startswith('From ') : continue
    line = line.split()
    line = line[1]
    count[line] = count.get(line, 0) + 1

for most,most0 in count.items():
    if most2 is None or most2 < most0:
        most1 = most
        most2 = most0
print(most1, most2)
