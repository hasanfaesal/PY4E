smallest = None
largest = None

while True:
    num = input('Enter a number: ')
    if num == "done":
        break
    
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue

    if largest is None and smallest is None:
        largest = num
        smallest = num

    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)