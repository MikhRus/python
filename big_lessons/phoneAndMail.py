#! python3
# Finding phone number and email in copied data in buffer.

import pyperclip, re

phoneRegex = re.compile(r'''(       # phone Regex
    (\d{3}|\(\d{3}\))?              # Region code (not required)
    (\s|-|\.)?                      # Delimeter (not required)
    (\d{3})                         # First 3 digits
    (\s|-|\.)                       # Delimeter (required)
    (\d{4})                         # Second 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Added number
)''', re.VERBOSE)

emailRegex = re.compile(r'''        # email Regex
    ([a-zA-Z0-9._%+-]+)             # username
    (@)                             # @
    ([a-zA-Z0-9.-]+)                # Before .com-like part of domain name
    (\.[a-zA-Z]{2,4})               # .com-like part of domain name
''', re.VERBOSE)

        # Find values in copied text
text = str(pyperclip.paste())       # copy text form buffer to var 

matches = []
# Insert correct for of phoneNumbers to list
matches.append('Phones:')
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
# Insert emails to list
matches.append('E-mails:')
for groups in emailRegex.findall(text):
    joinEmailAddress = ''.join(groups)
    matches.append(joinEmailAddress)

# Copy to buffer
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied into buffer')
    print('\n'.join(matches))
else:
    print('Phone numbers or emails doesn\'t finded.')