# Finish that
import re

def checkPassword(password):
    passwordRegex = re.compile(r'[a-zA-Z0-9!@#$]{8,}')
    result = passwordRegex.search(password).group()
    return result
print(checkPassword(str(input())))

