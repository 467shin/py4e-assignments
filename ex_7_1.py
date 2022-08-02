# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fh = fh.read()
for line in fh:
    fh = fh.rstrip()
print(fh.upper())
