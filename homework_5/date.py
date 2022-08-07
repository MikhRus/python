from hashlib import new
import re
# Find date DD/MM/YYYY in correct form
dates = '21/12/2005, 33/01/2000, 31/04/2010, 20/10/999, 31.4.1244, 30/02/2014, 29/2/2020, 29/2/2021, 20.10.2022, 0.11.2011, 1/1/2000, 20/02/2020, 30/4/2020'
#dates = '30/4/2020'

dateRegex = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')
newDates = []
for date in dateRegex.findall(dates):
    # Date from Tuple to List
    date = list(date)

    # Leap YEAR status
    leapYear = False
    # 30 days month status
    thirtyDayMonth = False
    # February status
    februaryMonth = False

    # Start check YEAR -> MONTH -> DAY
    # Check YEAR
    if int(date[2]) not in range(1000, 3000): # If incorrect range -> go next
       continue
    else:
        if int(date[2]) % 4 == 0 and not (int(date[2]) % 100 == 0 and not int(date[2]) % 400 == 0):
            leapYear = True

    # Check Month info
    if int(date[1]) in range(1, 13):
        # Add 0 in short format Month
        if len(date[1]) == 1:
            date[1] = '0' + date[1]
        # Check 30 days month
        if date[1] in ['04', '06', '09', '11']:
            thirtyDayMonth = True
        # Check Fabruary
        if date[1] in ['02']:
            februaryMonth = True        
    else:
        continue

    # Check Day info
    if int(date[0]) in range(1,32):
        # Add 0 in short format Day
        if len(date[0]) == 1:
            date[0] = '0' + date[0]
        # If 29 feb and leap year (default False (not leap)) OR >29 days -> go next
        if int(date[0]) == 31:
            if thirtyDayMonth:
                continue
        if (int(date[0]) == 29 and februaryMonth and not leapYear) or (int(date[0]) > 29 and februaryMonth): 
            continue     
    else:
        continue

    newDates.append(date)
print(newDates)
    

#print(dateRegex.findall())