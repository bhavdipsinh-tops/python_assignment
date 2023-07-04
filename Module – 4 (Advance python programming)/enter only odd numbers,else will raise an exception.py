
try:
    num = int(input("Enter a number: "))
    mod = num % 2
    if mod > 0:
        print("This is an odd number.")
except:
    print("This is an even number.")
