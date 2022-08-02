# Use the file name mbox-short.txt as the file name
#굳이 2중 for문 써서 삽질한 문제
fname = input("Enter file name: ")
fh = open(fname)

total = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line[20:]
    total = total + float(line)
    count = count + 1
print('Average spam confidence:',total/count)
