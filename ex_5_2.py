largest = 0
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if largest < num:
            largest = num
        if smallest is None:
            smallest = num
        elif smallest > num:
            smallest = num
    except:
        print('Invalid input')
        
print("Maximum is", largest)
print("Minimum is", smallest)
