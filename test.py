import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

for cellObj in tuple(sheet.columns)[1]:
    print(cellObj.value)

# tuple(sheet['A1':'C3'])

# for rowOfCellObjects in sheet['A1':'C3']:
#     row = ''
#     for cellObj in rowOfCellObjects:
#         row = ' '.join([row, str(cellObj.value)])
#     print(row)
#     print('---END OF ROW---')