import re

censoreRegex = re.compile(r'agent (\w)\w+', re.I)

test = censoreRegex.sub(r'\1****', 'Agent Ann is very secret dude. Help agent Bob find important docs.')

print(test)