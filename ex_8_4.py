fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.split()

    for res in line:
        if not res in lst:
            lst.append(res)
lst.sort()
print(lst)
