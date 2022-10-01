#! python3 
# Open Google Map with address form Buffer or CLI args
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from arguments of CLI
    address = ' '.join(sys.argv[1:])

else:
    # Get address from buffer
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address, autoraise=False) 