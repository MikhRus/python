coordLitera = ['a','b','c','d','e','f','g','h']
coordNumber = ['1','2','3','4','5','6','7','8']

chessArray = {
    'wking':1,
    'bking':1,
    'wqueen':1,
    'bqueen':1,
    'wrook':2,
    'brook':2,
    'wbishop':2,
    'bbishop':2,
    'wknight':2,
    'bknight':2,
    'wpawn':8,
    'bpawn':8
}

coordDesk = []

for i in range(8):
    for j in range(8):
        coordDesk.append(str(coordNumber[i])+str(coordLitera[j]))

desk = {'1h':'brook', '9h':'wpawn'}

for k in desk:
    if k not in coordDesk:
        print('Invalid')
    else:
        print('Ok')
wcount = 0
bcount = 0
for v in desk.values():
    if v in chessArray:
        wcount += 1
    else:
        bcount += 1
print(wcount, bcount)