import random

class Colors:
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    blue = (0,0,255)
    green = (0,255,0)
    yellow = (255,255,0)
    orange = (255,102,0)
    grey = (220,220,220)

class Moves:
    U = 0
    Up = 1
    D = 2
    Dp = 3
    F = 4
    Fp = 5
    B = 6
    Bp = 7
    L = 8
    Lp = 9
    R = 10
    Rp = 11
    M_RL = 12 # hacia abajo
    M_RLp = 13 # hacia arriba
    M_FB = 14 # hacia derecha
    M_FBp = 15 #hacia izquierda
    M_UD = 16 # hacia derecha
    M_UDp = 17 # hacia izquierda

EdgesDone = dict(
A = 0,
B = 0,
C = 0,
D = 0,
E = 0,
F = 0,
G = 0,
H = 0,
I = 0,
J = 0,
K = 0,
L = 0,
M = 0,
N = 0,
O = 0,
P = 0,
Q = 0,
R = 0,
S = 0,
T = 0,
U = 0,
V = 0,
W = 0,
X = 0
)

Other_Letters_in_Piece_Edges = dict(
A = 'Q',
B = 'M',
C = 'I',
D = 'E',
E = 'D',
F = 'L',
G = 'X',
H = 'R',
I = 'C',
J = 'P',
K = 'U',
L = 'F',
M = 'B',
N = 'T',
O = 'V',
P = 'J',
Q = 'A',
R = 'H',
S = 'W',
T = 'N',
U = 'K',
V = 'O',
W = 'S',
X = 'G'
)

CornersDone = dict(
A = 0,
B = 0,
C = 0,
D = 0,
E = 0,
F = 0,
G = 0,
H = 0,
I = 0,
J = 0,
K = 0,
L = 0,
M = 0,
N = 0,
O = 0,
P = 0,
Q = 0,
R = 0,
S = 0,
T = 0,
U = 0,
V = 0,
W = 0,
X = 0
)

Other_Letters_in_Piece_Corners = dict(
A = ['E','R'],
B = ['N','Q'],
C = ['J','M'],
D = ['F','I'],
E = ['A','R'],
F = ['D','I'],
G = ['L','U'],
H = ['S','X'],
I = ['D','F'],
J = ['C','M'],
K = ['P','V'],
L = ['G','U'],
M = ['C','J'],
N = ['B','Q'],
O = ['T','W'],
P = ['K','V'],
Q = ['B','N'],
R = ['A','E'],
S = ['H','X'],
T = ['O','W'],
U = ['G','L'],
V = ['K','P'],
W = ['O','T'],
X = ['H','S']
)

Letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']

EdgeSwap = [Moves.R, Moves.U, Moves.Rp, Moves.Up, Moves.Rp, Moves.F, Moves.R, Moves.R, Moves.Up, Moves.Rp, Moves.Up, Moves.R, Moves.U, Moves.Rp, Moves.Fp]
CornerSwap = [Moves.R, Moves.Up, Moves.Rp, Moves.Up, Moves.R, Moves.U, Moves.Rp, Moves.Fp, Moves.R, Moves.U, Moves.Rp, Moves.Up, Moves.Rp, Moves.F, Moves.R]
Parity = [Moves.R, Moves.Up, Moves.Rp, Moves.Up, Moves.R, Moves.U, Moves.R, Moves.D, Moves.Rp, Moves.Up, Moves.R, Moves.Dp, Moves.Rp, Moves.U, Moves.U, Moves.Rp, Moves.Up]

EdgeSetupMoves = dict(
A = [Moves.L, Moves.L, Moves.M_RL, Moves.M_RL, Moves.Dp, Moves.L, Moves.L, Moves.M_RL, Moves.M_RL], #l2 D' l2
B = 'Buffer', #buffer
C = [Moves.L, Moves.L, Moves.M_RL, Moves.M_RL, Moves.D, Moves.L, Moves.L, Moves.M_RL, Moves.M_RL], #l2 D l2
D = 0, #none
E = [Moves.L, Moves.Dp, Moves.M_UDp, Moves.L], #L d' L
F = [Moves.Dp, Moves.M_UDp, Moves.L], #d' L
G = [Moves.Lp, Moves.Dp, Moves.M_UDp, Moves.L], #L' d' L
H = [Moves.D, Moves.M_UD, Moves.Lp], #d L'
I = [Moves.L, Moves.M_RL, Moves.Dp, Moves.L, Moves.L], #l D' L2
J = [Moves.D, Moves.D, Moves.M_UD, Moves.M_UD, Moves.L], #d2 L
K = [Moves.F, Moves.Lp, Moves.Fp], #F L' F'
L = [Moves.Lp], #L'
M = 'Buffer', #buffer
N = [Moves.D, Moves.M_UD, Moves.L], #d L
O = [Moves.Dp, Moves.F, Moves.Lp, Moves.Fp], #D' F L' F'
P = [Moves.Dp, Moves.M_UDp, Moves.Lp], #d' L'
Q = [Moves.Lp, Moves.M_RLp, Moves.D, Moves.L, Moves.L], #l' D L2
R = [Moves.L], #L
S = [Moves.Lp, Moves.M_RLp, Moves.Dp, Moves.L, Moves.L], #l' D' L2
T = [Moves.D, Moves.D, Moves.M_UD, Moves.M_UD, Moves.Lp], #d2 L'
U = [Moves.Dp, Moves.L, Moves.L], #D' L2
V = [Moves.D, Moves.D, Moves.L, Moves.L], #D2 L2
W = [Moves.D, Moves.L, Moves.L], #D L2
X = [Moves.L, Moves.L]  #L2
)

EdgeReverseSetupMoves = dict(
A = [Moves.L, Moves.L, Moves.M_RL, Moves.M_RL, Moves.D, Moves.L, Moves.L, Moves.M_RL, Moves.M_RL],
B = 'Buffer',
C = [Moves.L, Moves.L, Moves.M_RL, Moves.M_RL, Moves.Dp, Moves.L, Moves.L, Moves.M_RL, Moves.M_RL],
D = 0,
E = [Moves.Lp, Moves.M_UD, Moves.D, Moves.Lp],
F = [Moves.Lp, Moves.M_UD, Moves.D],
G = [Moves.Lp, Moves.M_UD, Moves.D, Moves.L],
H = [Moves.L, Moves.M_UDp, Moves.Dp],
I = [Moves.Lp, Moves.Lp, Moves.D, Moves.M_RLp, Moves.Lp],
J = [Moves.Lp, Moves.M_UDp, Moves.M_UDp, Moves.Dp, Moves.Dp],
K = [Moves.F, Moves.L, Moves.Fp],
L = [Moves.L],
M = 'Buffer',
N = [Moves.Lp, Moves.M_UDp, Moves.Dp],
O = [Moves.F, Moves.L, Moves.Fp, Moves.D],
P = [Moves.L, Moves.M_UD, Moves.D],
Q = [Moves.Lp, Moves.Lp, Moves.Dp, Moves.M_RL, Moves.L],
R = [Moves.Lp],
S = [Moves.Lp, Moves.Lp, Moves.D, Moves.M_RL, Moves.L],
T = [Moves.L, Moves.M_UDp, Moves.M_UDp, Moves.Dp, Moves.Dp],
U = [Moves.Lp, Moves.Lp, Moves.D],
V = [Moves.Lp, Moves.Lp, Moves.Dp, Moves.Dp],
W = [Moves.Lp, Moves.Lp, Moves.Dp],
X = [Moves.Lp, Moves.Lp]
)

CornerSetupMoves = dict(
A = 'Buffer',
B = [Moves.R, Moves.R],
C = [Moves.F, Moves.F, Moves.D],
D = [Moves.F, Moves.F],
E = 'Buffer',
F = [Moves.Fp, Moves.D],
G = [Moves.Fp],
H = [Moves.Dp, Moves.R],
I = [Moves.F, Moves.Rp],
J = [Moves.Rp],
K = [Moves.Fp, Moves.Rp],
L = [Moves.F, Moves.F, Moves.Rp],
M = [Moves.F],
N = [Moves.Rp, Moves.F],
O = [Moves.R, Moves.R, Moves.F],
P = [Moves.R, Moves.F],
Q = [Moves.R, Moves.Dp],
R = 'Buffer',
S = [Moves.D, Moves.Fp],
T = [Moves.R],
U = [Moves.D],
V = 0,
W = [Moves.Dp],
X = [Moves.D, Moves.D]
)

CornerReverseSetupMoves = dict(
A = 'Buffer',
B = [Moves.R, Moves.R],
C = [Moves.Dp, Moves.F, Moves.F],
D = [Moves.F, Moves.F],
E = 'Buffer',
F = [Moves.Dp, Moves.F],
G = [Moves.F],
H = [Moves.Rp, Moves.D],
I = [Moves.R, Moves.Fp],
J = [Moves.R],
K = [Moves.R, Moves.F],
L = [Moves.R, Moves.F, Moves.F],
M = [Moves.Fp],
N = [Moves.Fp, Moves.R],
O = [Moves.Fp, Moves.R, Moves.R],
P = [Moves.Fp, Moves.Rp],
Q = [Moves.D, Moves.Rp],
R = 'Buffer',
S = [Moves.F, Moves.Dp],
T = [Moves.Rp],
U = [Moves.Dp],
V = 0,
W = [Moves.D],
X = [Moves.D, Moves.D] 
)

def IdentifyEdgeLetter(sticker1, sticker2):

    if(sticker1 == Colors.white and sticker2 == Colors.blue):
        return 'A'
    elif(sticker1 == Colors.white and sticker2 == Colors.red):
        return 'B'
    elif(sticker1 == Colors.white and sticker2 == Colors.green):
        return 'C'
    elif(sticker1 == Colors.white and sticker2 == Colors.orange):
        return 'D'
    elif(sticker1 == Colors.orange and sticker2 == Colors.white):
        return 'E'
    elif(sticker1 == Colors.orange and sticker2 == Colors.green):
        return 'F'
    elif(sticker1 == Colors.orange and sticker2 == Colors.yellow):
        return 'G'
    elif(sticker1 == Colors.orange and sticker2 == Colors.blue):
        return 'H'
    elif(sticker1 == Colors.green and sticker2 == Colors.white):
        return 'I'
    elif(sticker1 == Colors.green and sticker2 == Colors.red):
        return 'J'
    elif(sticker1 == Colors.green and sticker2 == Colors.yellow):
        return 'K'
    elif(sticker1 == Colors.green and sticker2 == Colors.orange):
        return 'L'
    elif(sticker1 == Colors.red and sticker2 == Colors.white):
        return 'M'
    elif(sticker1 == Colors.red and sticker2 == Colors.blue):
        return 'N'
    elif(sticker1 == Colors.red and sticker2 == Colors.yellow):
        return 'O'
    elif(sticker1 == Colors.red and sticker2 == Colors.green):
        return 'P'
    elif(sticker1 == Colors.blue and sticker2 == Colors.white):
        return 'Q'
    elif(sticker1 == Colors.blue and sticker2 == Colors.orange):
        return 'R'
    elif(sticker1 == Colors.blue and sticker2 == Colors.yellow):
        return 'S'
    elif(sticker1 == Colors.blue and sticker2 == Colors.red):
        return 'T'
    elif(sticker1 == Colors.yellow and sticker2 == Colors.green):
        return 'U'
    elif(sticker1 == Colors.yellow and sticker2 == Colors.red):
        return 'V'
    elif(sticker1 == Colors.yellow and sticker2 == Colors.blue):
        return 'W'
    elif(sticker1 == Colors.yellow and sticker2 == Colors.orange):
        return 'X'
    else:
        return 0

def GetEdgeLetterByPosition(Cube, edge):

    if(edge == 'A'):
        return Cube[-1][1][0].color_U
    elif(edge == 'B'):
        return Cube[-1][-1][1].color_U
    elif(edge == 'C'):
        return Cube[-1][1][-1].color_U
    elif(edge == 'D'):
        return Cube[-1][0][1].color_U
    elif(edge == 'E'):
        return Cube[-1][0][1].color_L
    elif(edge == 'F'):
        return Cube[1][0][-1].color_L
    elif(edge == 'G'):
        return Cube[0][0][1].color_L
    elif(edge == 'H'):
        return Cube[1][0][0].color_L
    elif(edge == 'I'):
        return Cube[-1][1][-1].color_F
    elif(edge == 'J'):
        return Cube[1][-1][-1].color_F
    elif(edge == 'K'):
        return Cube[0][1][-1].color_F
    elif(edge == 'L'):
        return Cube[1][0][-1].color_F
    elif(edge == 'M'):
        return Cube[-1][-1][1].color_R
    elif(edge == 'N'):
        return Cube[1][-1][0].color_R
    elif(edge == 'O'):
        return Cube[0][-1][1].color_R
    elif(edge == 'P'):
        return Cube[1][-1][-1].color_R
    elif(edge == 'Q'):
        return Cube[-1][1][0].color_B
    elif(edge == 'R'):
        return Cube[1][0][0].color_B
    elif(edge == 'S'):
        return Cube[0][1][0].color_B
    elif(edge == 'T'):
        return Cube[1][-1][0].color_B
    elif(edge == 'U'):
        return Cube[0][1][-1].color_D
    elif(edge == 'V'):
        return Cube[0][-1][1].color_D
    elif(edge == 'W'):
        return Cube[0][1][0].color_D
    elif(edge == 'X'):
        return Cube[0][0][1].color_D
    else:
        return 0

def GetEdgeLetterChain(Cube):

    EdgeSolvingChain = []
    Chain_Broken = False
    Reset_Chain = False
    EdgeCounter = 0
    Buffer1 = 'B'
    Buffer2 = 'M'

    #This whole loop is to state edges that are already in place as done edges, so the chain does not include them
    for edge in Letters:
        if(IdentifyEdgeLetter(GetEdgeLetterByPosition(Cube, edge), GetEdgeLetterByPosition(Cube, Other_Letters_in_Piece_Edges[edge])) == edge):
            EdgesDone[edge] = 1
            EdgesDone[Other_Letters_in_Piece_Edges[edge]] = 1

    #Buffer piece for edges contains stickers B and M
    EdgeSolvingChain.append(IdentifyEdgeLetter(GetEdgeLetterByPosition(Cube, Buffer1), GetEdgeLetterByPosition(Cube,Buffer2)))

    #Keep track of analyzed pieces
    EdgesDone[EdgeSolvingChain[0]] = 1
    EdgesDone[Other_Letters_in_Piece_Edges[EdgeSolvingChain[0]]] = 1

    #Buffer pieces break the chain
    if (EdgeSolvingChain[-1] == Buffer1 or EdgeSolvingChain[-1] == Buffer2):
        EdgesDone[Buffer1] = 1
        EdgesDone[Buffer2] = 1
        EdgeSolvingChain.pop()
        Reset_Chain = True

    while(True):
        while(not Chain_Broken):

            if(not Reset_Chain):
                EdgeSolvingChain.append(IdentifyEdgeLetter(GetEdgeLetterByPosition(Cube,EdgeSolvingChain[-1]), GetEdgeLetterByPosition(Cube,Other_Letters_in_Piece_Edges[EdgeSolvingChain[-1]])))
            else:
                #New chain must be created with a random letter
                random_number = random.randint(0,23)
                random_letter = Letters[random_number]
                EdgeSolvingChain.append(random_letter)

            #Check if pieces have been analyzed before
            if (EdgesDone[EdgeSolvingChain[-1]] == 1 or EdgesDone[Other_Letters_in_Piece_Edges[EdgeSolvingChain[-1]]] == 1):
                Chain_Broken = True

            if(Reset_Chain):
                if(Chain_Broken):
                    #Prevents from messing up the chain
                    if(EdgeSolvingChain[-1] != Buffer1 and EdgeSolvingChain[-1] != Buffer2):
                        #Random letter was already donde
                        EdgeSolvingChain.pop()
                else:
                    #Random letter is good
                    Reset_Chain = False

            if(len(EdgeSolvingChain) != 0):
                #Buffer pieces break the chain
                if (EdgeSolvingChain[-1] == Buffer1 or EdgeSolvingChain[-1] == Buffer2):
                    EdgesDone[Buffer1] = 1
                    EdgesDone[Buffer2] = 1
                    EdgeSolvingChain.pop()
                    Chain_Broken = True
                else:
                    #Keep track of analyzed pieces
                    EdgesDone[EdgeSolvingChain[-1]] = 1
                    EdgesDone[Other_Letters_in_Piece_Edges[EdgeSolvingChain[-1]]] = 1

        #Check for done edges
        for DoneEdges in EdgesDone:
            if(EdgesDone[DoneEdges] == 1):
                EdgeCounter += 1

        #If all of the edges are done, end the chain
        if (EdgeCounter == len(EdgesDone)):
            break
        else:
            #If not, start a new chain
            EdgeCounter = 0
            Chain_Broken = False
            Reset_Chain = True

    return EdgeSolvingChain

def IdentifyCornerLetter(sticker1, sticker2, sticker3):

    if((sticker1 == Colors.white and sticker2 == Colors.blue and sticker3  == Colors.orange) or (sticker1 == Colors.white and sticker2 == Colors.orange and sticker3  == Colors.blue)):
        return 'A'
    elif((sticker1 == Colors.white and sticker2 == Colors.blue and sticker3  == Colors.red) or (sticker1 == Colors.white and sticker2 == Colors.red and sticker3  == Colors.blue)):
        return 'B'
    elif((sticker1 == Colors.white and sticker2 == Colors.green and sticker3  == Colors.red) or (sticker1 == Colors.white and sticker2 == Colors.red and sticker3  == Colors.green)):
        return 'C'
    elif((sticker1 == Colors.white and sticker2 == Colors.green and sticker3  == Colors.orange) or (sticker1 == Colors.white and sticker2 == Colors.orange and sticker3  == Colors.green)):
        return 'D'
    elif((sticker1 == Colors.orange and sticker2 == Colors.white and sticker3  == Colors.blue) or (sticker1 == Colors.orange and sticker2 == Colors.blue and sticker3  == Colors.white)):
        return 'E'
    elif((sticker1 == Colors.orange and sticker2 == Colors.white and sticker3  == Colors.green) or (sticker1 == Colors.orange and sticker2 == Colors.green and sticker3  == Colors.white)):
        return 'F'
    elif((sticker1 == Colors.orange and sticker2 == Colors.yellow and sticker3  == Colors.green) or (sticker1 == Colors.orange and sticker2 == Colors.green and sticker3  == Colors.yellow)):
        return 'G'
    elif((sticker1 == Colors.orange and sticker2 == Colors.yellow and sticker3  == Colors.blue) or (sticker1 == Colors.orange and sticker2 == Colors.blue and sticker3  == Colors.yellow)):
        return 'H'
    elif((sticker1 == Colors.green and sticker2 == Colors.white and sticker3  == Colors.orange) or (sticker1 == Colors.green and sticker2 == Colors.orange and sticker3  == Colors.white)):
        return 'I'
    elif((sticker1 == Colors.green and sticker2 == Colors.white and sticker3  == Colors.red) or (sticker1 == Colors.green and sticker2 == Colors.red and sticker3  == Colors.white)):
        return 'J'
    elif((sticker1 == Colors.green and sticker2 == Colors.yellow and sticker3  == Colors.red) or (sticker1 == Colors.green and sticker2 == Colors.red and sticker3  == Colors.yellow)):
        return 'K'
    elif((sticker1 == Colors.green and sticker2 == Colors.yellow and sticker3  == Colors.orange) or (sticker1 == Colors.green and sticker2 == Colors.orange and sticker3  == Colors.yellow)):
        return 'L'
    elif((sticker1 == Colors.red and sticker2 == Colors.white and sticker3  == Colors.green) or (sticker1 == Colors.red and sticker2 == Colors.green and sticker3  == Colors.white)):
        return 'M'
    elif((sticker1 == Colors.red and sticker2 == Colors.white and sticker3  == Colors.blue) or (sticker1 == Colors.red and sticker2 == Colors.blue and sticker3  == Colors.white)):
        return 'N'
    elif((sticker1 == Colors.red and sticker2 == Colors.yellow and sticker3  == Colors.blue) or (sticker1 == Colors.red and sticker2 == Colors.blue and sticker3  == Colors.yellow)):
        return 'O'
    elif((sticker1 == Colors.red and sticker2 == Colors.yellow and sticker3  == Colors.green) or (sticker1 == Colors.red and sticker2 == Colors.green and sticker3  == Colors.yellow)):
        return 'P'
    elif((sticker1 == Colors.blue and sticker2 == Colors.white and sticker3  == Colors.red) or (sticker1 == Colors.blue and sticker2 == Colors.red and sticker3  == Colors.white)):
        return 'Q'
    elif((sticker1 == Colors.blue and sticker2 == Colors.white and sticker3  == Colors.orange) or (sticker1 == Colors.blue and sticker2 == Colors.orange and sticker3  == Colors.white)):
        return 'R'
    elif((sticker1 == Colors.blue and sticker2 == Colors.yellow and sticker3  == Colors.orange) or (sticker1 == Colors.blue and sticker2 == Colors.orange and sticker3  == Colors.yellow)):
        return 'S'
    elif((sticker1 == Colors.blue and sticker2 == Colors.yellow and sticker3  == Colors.red) or (sticker1 == Colors.blue and sticker2 == Colors.red and sticker3  == Colors.yellow)):
        return 'T'
    elif((sticker1 == Colors.yellow and sticker2 == Colors.green and sticker3  == Colors.orange) or (sticker1 == Colors.yellow and sticker2 == Colors.orange and sticker3  == Colors.green)):
        return 'U'
    elif((sticker1 == Colors.yellow and sticker2 == Colors.green and sticker3  == Colors.red) or (sticker1 == Colors.yellow and sticker2 == Colors.red and sticker3  == Colors.green)):
        return 'V'
    elif((sticker1 == Colors.yellow and sticker2 == Colors.blue and sticker3  == Colors.red) or (sticker1 == Colors.yellow and sticker2 == Colors.red and sticker3  == Colors.blue)):
        return 'W'
    elif((sticker1 == Colors.yellow and sticker2 == Colors.blue and sticker3  == Colors.orange) or (sticker1 == Colors.yellow and sticker2 == Colors.orange and sticker3  == Colors.blue)):
        return 'X'
    else:
        return 0

def GetCornerLetterByPosition(Cube, corner):

    if(corner == 'A'):
        return Cube[-1][0][0].color_U
    elif(corner == 'B'):
        return Cube[-1][-1][0].color_U
    elif(corner == 'C'):
        return Cube[-1][-1][-1].color_U
    elif(corner == 'D'):
        return Cube[-1][0][-1].color_U
    elif(corner == 'E'):
        return Cube[-1][0][0].color_L
    elif(corner == 'F'):
        return Cube[-1][0][-1].color_L
    elif(corner == 'G'):
        return Cube[0][0][-1].color_L
    elif(corner == 'H'):
        return Cube[0][0][0].color_L
    elif(corner == 'I'):
        return Cube[-1][0][-1].color_F
    elif(corner == 'J'):
        return Cube[-1][-1][-1].color_F
    elif(corner == 'K'):
        return Cube[0][-1][-1].color_F
    elif(corner == 'L'):
        return Cube[0][0][-1].color_F
    elif(corner == 'M'):
        return Cube[-1][-1][-1].color_R
    elif(corner == 'N'):
        return Cube[-1][-1][0].color_R
    elif(corner == 'O'):
        return Cube[0][-1][0].color_R
    elif(corner == 'P'):
        return Cube[0][-1][-1].color_R
    elif(corner == 'Q'):
        return Cube[-1][-1][0].color_B
    elif(corner == 'R'):
        return Cube[-1][0][0].color_B
    elif(corner == 'S'):
        return Cube[0][0][0].color_B
    elif(corner == 'T'):
        return Cube[0][-1][0].color_B
    elif(corner == 'U'):
        return Cube[0][0][-1].color_D
    elif(corner == 'V'):
        return Cube[0][-1][-1].color_D
    elif(corner == 'W'):
        return Cube[0][-1][0].color_D
    elif(corner == 'X'):
        return Cube[0][0][0].color_D
    else:
        return 0

def GetCornerLetterChain(Cube):
    CornerSolvingChain = []
    Chain_Broken = False
    Reset_Chain = False
    CornerCounter = 0
    Buffer1 = 'E'
    Buffer2 = 'A'
    Buffer3 = 'R'

    #This whole loop is to state corners that are already in place as done corners, so the chain does not include them
    for corner in Letters:
        if(IdentifyCornerLetter(GetCornerLetterByPosition(Cube,corner), GetCornerLetterByPosition(Cube,Other_Letters_in_Piece_Corners[corner][0]), GetCornerLetterByPosition(Cube, Other_Letters_in_Piece_Corners[corner][1])) == corner):
            CornersDone[corner] = 1
            CornersDone[Other_Letters_in_Piece_Corners[corner][0]] = 1
            CornersDone[Other_Letters_in_Piece_Corners[corner][1]] = 1

    #Buffer piece for edges contains stickers B and M
    CornerSolvingChain.append(IdentifyCornerLetter(GetCornerLetterByPosition(Cube, Buffer1), GetCornerLetterByPosition(Cube,Buffer2), GetCornerLetterByPosition(Cube,Buffer3)))

    #Keep track of analyzed pieces
    CornersDone[CornerSolvingChain[0]] = 1
    CornersDone[Other_Letters_in_Piece_Corners[CornerSolvingChain[0]][0]] = 1
    CornersDone[Other_Letters_in_Piece_Corners[CornerSolvingChain[0]][1]] = 1

    #Buffer pieces break the chain
    if (CornerSolvingChain[-1] == Buffer1 or CornerSolvingChain[-1] == Buffer2 or CornerSolvingChain[-1] == Buffer3):
        CornersDone[Buffer1] = 1
        CornersDone[Buffer2] = 1
        CornersDone[Buffer3] = 1
        CornerSolvingChain.pop()
        Reset_Chain = True

    while(True):
        while(not Chain_Broken):

            if(not Reset_Chain):
                CornerSolvingChain.append(IdentifyCornerLetter(GetCornerLetterByPosition(Cube,CornerSolvingChain[-1]), GetCornerLetterByPosition(Cube,Other_Letters_in_Piece_Corners[CornerSolvingChain[-1]][0]), GetCornerLetterByPosition(Cube,Other_Letters_in_Piece_Corners[CornerSolvingChain[-1]][1])))
            else:
                #New chain must be created with a random letter
                random_number = random.randint(0,23)
                random_letter = Letters[random_number]
                CornerSolvingChain.append(random_letter)

            #Check if pieces have been analyzed before
            if (CornersDone[CornerSolvingChain[-1]] == 1 or CornersDone[Other_Letters_in_Piece_Corners[CornerSolvingChain[-1]][0]] == 1 or CornersDone[Other_Letters_in_Piece_Corners[CornerSolvingChain[-1]][1]] == 1):
                Chain_Broken = True

            if(Reset_Chain):
                if(Chain_Broken):
                    #Prevents from messing up the chain
                    if(CornerSolvingChain[-1] != Buffer1 and CornerSolvingChain[-1] != Buffer2 and CornerSolvingChain[-1] != Buffer3):
                        #Random letter was already done
                        CornerSolvingChain.pop()
                else:
                    #Random letter is good
                    Reset_Chain = False

            if(len(CornerSolvingChain) != 0):
                #Buffer pieces break the chain
                if (CornerSolvingChain[-1] == Buffer1 or CornerSolvingChain[-1] == Buffer2 or CornerSolvingChain[-1] == Buffer3):
                    CornersDone[Buffer1] = 1
                    CornersDone[Buffer2] = 1
                    CornersDone[Buffer3] = 1
                    CornerSolvingChain.pop()
                    Chain_Broken = True
                else:
                    #Keep track of analyzed pieces
                    CornersDone[CornerSolvingChain[-1]] = 1
                    CornersDone[Other_Letters_in_Piece_Corners[CornerSolvingChain[-1]][0]] = 1
                    CornersDone[Other_Letters_in_Piece_Corners[CornerSolvingChain[-1]][1]] = 1

        #Check for done corners
        for DoneCorners in CornersDone:
            if(CornersDone[DoneCorners] == 1):
                CornerCounter += 1

        #If all of the corners are done, end the chain
        if (CornerCounter == len(CornersDone)):
            break
        else:
            #If not, start a new chain
            CornerCounter = 0
            Chain_Broken = False
            Reset_Chain = True

    return CornerSolvingChain

def GetSolveChain(Cube):

    SolveChain = []
    
    EdgeChain = GetEdgeLetterChain(Cube)
    CornerChain = GetCornerLetterChain(Cube)

    print("Edge Letter Chain: ", EdgeChain)
    print("Corner Letter Chain: ", CornerChain)

    for i in range(len(EdgeChain)):
        if(EdgeSetupMoves[EdgeChain[i]] == 0):
            for j in range(len(EdgeSwap)):
                SolveChain.append(EdgeSwap[j])
        elif(EdgeSetupMoves[EdgeChain[i]] != 'Buffer'):
            for k in range(len(EdgeSetupMoves[EdgeChain[i]])):
                SolveChain.append(EdgeSetupMoves[EdgeChain[i]][k])

            for j in range(len(EdgeSwap)):
                SolveChain.append(EdgeSwap[j])

            for l in range(len(EdgeReverseSetupMoves[EdgeChain[i]])):
                SolveChain.append(EdgeReverseSetupMoves[EdgeChain[i]][l])

    if (((len(EdgeChain) % 2) != 0) or ((len(CornerChain) % 2) != 0)):
        for i in range(len(Parity)):
            SolveChain.append(Parity[i])

    for i in range(len(CornerChain)):
        if(CornerSetupMoves[CornerChain[i]] == 0):
            for j in range(len(CornerSwap)):
                SolveChain.append(CornerSwap[j])
        elif(CornerSetupMoves[CornerChain[i]] != 'Buffer'):
            for k in range(len(CornerSetupMoves[CornerChain[i]])):
                SolveChain.append(CornerSetupMoves[CornerChain[i]][k])

            for j in range(len(CornerSwap)):
                SolveChain.append(CornerSwap[j])

            for l in range(len(CornerReverseSetupMoves[CornerChain[i]])):
                SolveChain.append(CornerReverseSetupMoves[CornerChain[i]][l])

    print("Total Moves of Solution: ", len(SolveChain))

    return SolveChain