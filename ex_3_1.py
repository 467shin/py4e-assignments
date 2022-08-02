hrs = input("Enter Hours:")
rat = input("Enter rate:")
h = float(hrs)
r = float(rat)
if h > 40:
    h = 40 + float(h - 40) * 1.5
print(h * r)
