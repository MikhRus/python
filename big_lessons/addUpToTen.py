import pyinputplus as pyip

def addUpToTen(numbers):
    numbersList = list(numbers)

    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('Sum must be equals 10, not %s!' % (sum(numbersList)))
    return int(numbers)

response = pyip.inputCustom(addUpToTen)
print(response)