import pyinputplus as pyip

while True:
    promt = 'Do you wanna know, how to keep busy a fool for a few hours?'
    response = pyip.inputYesNo(promt, yesVal='yes', noVal='no', default='no', limit=2)
    if response == 'no':
        break
print('Good by!')