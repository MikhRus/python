def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    return result

while True:
    try:
        print ('Insert your Value')
        value = int(input())
        while value != 1:
            value = collatz(value)
            print(value)
        print('End')

    except Exception:
        print('Enter Incorrect Value. Enter only numbers.')