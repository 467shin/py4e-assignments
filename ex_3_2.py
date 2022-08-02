hrs = input("Enter Hours:")
rat = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rat)
except:
    print('Error, please enter numeric input.')
    quit()

if h > 40:
    h = 40 + float(h - 40) * 1.5
print(h * r)
