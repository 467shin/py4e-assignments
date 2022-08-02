def computepay(h, r):
    if int(h) > 40:
        h = 40 + (int(h) - 40) * 1.5
    return float(h) * float(r)

hrs = input("Enter Hours:")
rte = input("Enter rate:")
p = computepay(hrs, rte)
print("Pay", p)