def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    return result

while True:
    try:
        print(collatz(int(input())))
    except Exception:
        print('Enter Incorrect Value. Enter only numbers.')