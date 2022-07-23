from pyrsistent import b


chessBoard = []
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
coordLitera = ['a','b','c','d','e','f','g','h']
coordNumber = ['1','2','3','4','5','6','7','8']
coordDesk = []
for i in range(8):
    for j in range(8):
        coordDesk.append(str(coordNumber[i])+str(coordLitera[j]))



def isValidChessBoard(board):
    for k in board:
        if k not in coordDesk:
            print('False')
            break
    