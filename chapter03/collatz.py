def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    print(number)
    return number

while True:
    try:
        number = int(input("Please provide a positive integer: "))
    except:
        print("That was not an int.")
        continue

    if number < 0:
        print("That was not a positive int.")
    else:
        break

print(number)
while number != 1:
    number = collatz(number)
