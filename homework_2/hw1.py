spam = ['яблоки', 'бананы', 'тофу', 'коты']
print(len(spam))

def split(list):
    if list == []:
        return ('List is empty')
        
    exitString = ''
    for i, item in enumerate(list):
        if i == 0:
            exitString += item
        elif i != len(list) - 1:
            exitString += ', ' + item
        else:
            exitString += ' и ' + item
    return exitString

print(split(spam))