# 2048, THE IDEA OF THE GAME IS THAT YOU HAVE TO COMBINE DIFERENT BLOCKS TO MAKE A BLOCK THAT IS OF 2 TIMES THE VALUE
# OF THE PREVIOUS BLOCK. AND THIS IS DONE BY PRESSING THE ARROW KEYS TO MOVE ALL THE MOVABLE BLOCKS IN THE DIRECTION OF
# THE ARROW KEY PRESSED. UPON MOVING, A RANDOM TILE OF VALUE 2 IS SPAWNED SOMEWHERE IN THE GRID, YOU LOSE WHEN YOUR GRID
# IS FULL

from Ky_Game import *
import pyautogui
import random
from random import choice
import time
from math import floor
import os

pygame.font.init()
pygame.mixer.init()

# INTITIALIZING THE WIDTH AND THE HEIGHT OF THE WINDOW.
# THIS GAME WILL BE MADE WITH RESPECT TO THE HEGHT AND THE WIDTH OF THE MONITOR, AND WILL BE HALF OF THAT./

WIDTH, HEIGHT = pyautogui.size()
WIDTH, HEIGHT = floor( WIDTH / 2 ), floor( HEIGHT / 2 )

# INITIALIZING THE DIMENSIONS OF THE BG_BOX OF THE 2048 THING, AND THE SIDE OF THE TILES

BG_BOX_SIZE = floor( HEIGHT / 1.35 )
BG_BOX_X = floor( WIDTH / 6.4 )
BG_BOX_Y = floor( HEIGHT / 7.7 )
BG_BOX_GAP_X = floor( BG_BOX_SIZE / 35 )
BG_BOX_GAP_Y = floor( BG_BOX_SIZE / 35 )
TILE_SIDE = floor( BG_BOX_SIZE / 4.6511 )

# INITIALIZING THE WINDOW.

WIN = pygame.display.set_mode( (WIDTH, HEIGHT), pygame.RESIZABLE )
pygame.display.set_caption( "2048" )

# INITIALIZING THE FONTS.

GAME_FONT = pygame.font.Font( os.path.join( "Assets", "kel.ttf" ), 70 )

# INITIALIZING THE BG MUSIC

pygame.mixer.music.load( os.path.join( "Assets", "BGM.ogg" ) )
pygame.mixer.music.play()
CLICK_SOUND = pygame.mixer.Sound( os.path.join( "Assets", "select1.ogg" ) )

# INTITIALIZING THE IMAGES.

BG_IMAGE = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "BG_IMAGE.png" ) ), (WIDTH, HEIGHT) )
LOST_IMAGE = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "LOST_IMAGE.png" ) ), (WIDTH, HEIGHT) )
PLAY_IMAGE = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "PLAY_IMAGE.png" ) ), (WIDTH, HEIGHT) )
BG_BOX_IMAGE = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "BG_BOX_IMAGE.png" ) ),
                                       (BG_BOX_SIZE, BG_BOX_SIZE) )

# INITIALIZING THE VALUED TILES.
IMAGE_2 = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "2.png" ) ),
                                  (TILE_SIDE, TILE_SIDE) )
IMAGE_4 = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "4.png" ) ),
                                  (TILE_SIDE, TILE_SIDE) )
IMAGE_8 = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "8.png" ) ),
                                  (TILE_SIDE, TILE_SIDE) )
IMAGE_16 = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "16.png" ) ),
                                   (TILE_SIDE, TILE_SIDE) )
IMAGE_32 = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "32.png" ) ),
                                   (TILE_SIDE, TILE_SIDE) )
IMAGE_64 = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "64.png" ) ),
                                   (TILE_SIDE, TILE_SIDE) )
IMAGE_128 = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "128.png" ) ),
                                    (TILE_SIDE, TILE_SIDE) )
IMAGE_256 = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "256.png" ) ),
                                    (TILE_SIDE, TILE_SIDE) )
IMAGE_512 = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "512.png" ) ),
                                    (TILE_SIDE, TILE_SIDE) )
IMAGE_1024 = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "1024.png" ) ),
                                     (TILE_SIDE, TILE_SIDE) )
IMAGE_2048 = pygame.transform.scale( pygame.image.load( os.path.join( "Assets", "2048.png" ) ),
                                     (TILE_SIDE, TILE_SIDE) )

# INITIALIZING THE POSITIONS OF THE BUTTONS.

START_BTN_LOWER = (floor( WIDTH / 3.67 ),
                   floor( HEIGHT / 1.75 ))
START_BTN_UPPER = (floor( WIDTH / 2.1 ),
                   floor( HEIGHT / 1.43 ))

EXIT_BTN_LOWER = (floor( WIDTH / 1.9 ),
                  floor( HEIGHT / 1.73 ))
EXIT_BTN_UPPER = (floor( WIDTH / 1.41 ),
                  floor( HEIGHT / 1.43 ))

# INITIALIZING THE GLOBAL LIST THAT CONTAINS ALL THE STUFF (BASED ON THE WIDTH AND THE HEIGHT)

Coordees = []
for i in range( 4 ):
    rows = []
    for j in range( 4 ):
        rows.append( [0, 0, 0] )
    Coordees.append( rows )

# DEFINING A DICTIONARY THAT SETS THE IMAGE BASED ON THE VALUE OF THE TILE.

ValueDict = {
    2: IMAGE_2,
    4: IMAGE_4,
    8: IMAGE_8,
    16: IMAGE_16,
    32: IMAGE_32,
    64: IMAGE_64,
    128: IMAGE_128,
    256: IMAGE_256,
    512: IMAGE_512,
    1024: IMAGE_1024,
    2048: IMAGE_2048
}

# INITIALIZING THE CLASS TILE
class Tile:
    
    def __init__( self, X, Y, Tile_Side, IndeX, IndeY, Value = 2 ):
        self.X = X
        self.Y = Y
        self.IndeX = IndeX
        self.IndeY = IndeY
        self.Tile_Side = Tile_Side
        self.Value = Value
        self.Image = IMAGE_2
        self.SetImage_()
        self.mask = pygame.mask.from_surface( self.Image )
    
    def SetImage_( self ):
        if self.Value == 2:
            self.Image = IMAGE_2
        elif self.Value == 4:
            self.Image = IMAGE_4
        elif self.Value == 8:
            self.Image = IMAGE_8
        elif self.Value == 16:
            self.Image = IMAGE_16
        elif self.Value == 32:
            self.Image = IMAGE_32
        elif self.Value == 64:
            self.Image = IMAGE_64
        elif self.Value == 128:
            self.Image = IMAGE_128
        elif self.Value == 256:
            self.Image = IMAGE_256
        elif self.Value == 512:
            self.Image = IMAGE_512
        elif self.Value == 1024:
            self.Image = IMAGE_1024
        elif self.Value == 2048:
            self.Image = IMAGE_2048
    
    def GetSide_( self ):
        return self.Tile_Side
    
    def GetValue_( self ):
        return self.Value
    
    def GetCoordees_( self ):
        return self.X, self.Y
    
    def Draw_( self ):
        WIN.blit( self.Image, (self.X, self.Y) )


# METHOD TO CHECK IF IT IS POSSIBLE TO PLAY THE GAME ANYMORE, RETURNS TRUE IF IT IS, ELSE FALSE.
def isMovable( ):
    is_Free = True
    for k in range( len( Coordees ) ):
        for l in range( len( Coordees[k] ) ):
            if Coordees[k][l][2] == 0:
                is_Free = True
                break
        if is_Free:
            break
    
    return is_Free

# METHOD TO ASSIGN CORDEES
def assignCordees( ):
    for k in range( len( Coordees ) ):
        y = floor( (BG_BOX_Y + BG_BOX_GAP_Y) + (k * (TILE_SIDE + BG_BOX_GAP_Y)) )
        for l in range( len( Coordees[k] ) ):
            x = floor( (BG_BOX_X + BG_BOX_GAP_X) + (l * (TILE_SIDE + BG_BOX_GAP_X)) )
            Coordees[k][l][0] = x
            Coordees[k][l][1] = y

# DRAWS THE BACKGROUND OF THE TILES.
def drawBG_BOX( ):
    WIN.blit( BG_BOX_IMAGE, (BG_BOX_X, BG_BOX_Y) )






shudBreak = False

is_movable_there = False



# RETURNS TRUE IF THERE IS A COLLISION BETWEEN 2 TILES IN THE Y AXIS, OF DIFFERENT VALUES, FALSE OTHERWISE
def checkCollisionY( firstObject, secondObject ):
    global shudBreak
    if firstObject.Y is not secondObject.Y:
        if firstObject.Y < secondObject.Y:
            if firstObject.Y + BG_BOX_GAP_Y + TILE_SIDE - 5>= secondObject.Y:
                if firstObject.Value != secondObject.Value:
                    return True
                else:
                    print(Tiles)
                    Tiles.remove( secondObject )
                    print(Tiles)
                    firstObject.Value *= 2
                    firstObject.SetImage_()
                    firstObject.Draw_()
                    shudBreak = True
                    return False
            else:
                return False
        else:
            return False
    else:
        return False



# RETURNS TRUE IF THERE IS A COLLISION BETWEEN 2 TILES IN THE X ASIS, OF DIFFERENT VALUES, FALSE OTHERWISE
def checkCollisionX( firstObject, secondObject ):
    global shudBreak
    if firstObject is not secondObject:
        if firstObject.X < secondObject.X:
            if firstObject.X + BG_BOX_GAP_X + TILE_SIDE - 5 >= secondObject.X:
                if firstObject.Value != secondObject.Value:
                    #print( 'value was not the same++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' )
                    return True
                else:
                    print(Tiles)
                    #print('value was same---------------------------------------------------------------------------------------')
                    Tiles.remove( secondObject )
                    print(Tiles)
                    firstObject.Value *= 2
                    firstObject.SetImage_()
                    firstObject.Draw_()
                    pygame.display.update()
                    shudBreak = True
                    return False
            else:
                return False
        else:
            return False
    else:
        return False






# FUNCTIONS TO MOVE ALL THE TILES.

def moveUp( ):
    global shudBreak, is_movable_there
    dont = [False for l in range( 16 )]
    for y in range( BG_BOX_SIZE ):
        drawBG_BOX()
        for tile in range( len( Tiles ) ):
            shudBreak = False
            Tiles[tile].Draw_()
            for t in Tiles:
                if Tiles[tile] is not t:
                    if isClostTo( Tiles[tile].X, t.X, 30 ):
                        dont[tile] = checkCollisionY( t, Tiles[tile] )
                        if shudBreak:
                            break
            if shudBreak:
                break
            if not dont[tile]:
                if (Tiles[tile].Y - 1) > Coordees[0][0][1]:
                    Tiles[tile].Y -= 1
                    is_movable_there = True
        pygame.display.update()

def moveDown( ):
    global shudBreak, is_movable_there
    dont = [False for l in range( 16 )]
    for y in range( BG_BOX_SIZE ):
        drawBG_BOX()
        for tile in range( len( Tiles ) ):
            shudBreak = False
            Tiles[tile].Draw_()
            for t in Tiles:
                if Tiles[tile] is not t:
                    if isClostTo( Tiles[tile].X, t.X, 30 ):
                        dont[tile] = checkCollisionY( Tiles[tile], t )
                        if shudBreak:
                            break
            if shudBreak:
                break
            if not dont[tile]:
                if (Tiles[tile].Y + 1) < Coordees[3][0][1]:
                    Tiles[tile].Y += 1
                    is_movable_there = True
        pygame.display.update()

def moveLeft( ):
    dont = [False for l in range( 16 )]
    global shudBreak, is_movable_there
    for x in range( BG_BOX_SIZE ):
        drawBG_BOX()
        for tile in range( len( Tiles ) ):
            shudBreak = False
            Tiles[tile].Draw_()
            for t in Tiles:
                if Tiles[tile] is not t:
                    if isClostTo( Tiles[tile].Y, t.Y, 30 ):
                        dont[tile] = checkCollisionX( t, Tiles[tile] )
                        if shudBreak:
                            break
            if shudBreak:
                break
            if not dont[tile]:
                if (Tiles[tile].X - 1) > Coordees[0][0][0]:
                    Tiles[tile].X -= 1
                    is_movable_there = True
        pygame.display.update()

def moveRight( ):
    dont = [False for l in range( 16 )]
    global shudBreak, is_movable_there
    
    for x in range( BG_BOX_SIZE ):
        
        drawBG_BOX()
        
        for I in range( len( Tiles ) ):
        
            shudBreak = False
            Tiles[I].Draw_()
        
            for t in Tiles:
                if Tiles[I] is not t:
                    if isClostTo( Tiles[I].Y, t.Y, 30 ):
                        dont[I] = checkCollisionX( Tiles[I], t )
                        if shudBreak:
                            break
        
            if shudBreak:
                break
            if not dont[I]:
                if (Tiles[I].X + 1) < Coordees[0][3][0]:
                    Tiles[I].X += 1
                    is_movable_there =  True
                    
        pygame.display.update()














# GLOBAL DECLARATION OF THE TILES LIST, CONTAINS EMPTY DUMMY TILE OBJECTS
# Tiles = [[Tile( 0, 0, TILE_SIDE, 2 ) for k in range( 4 )] for l in range( 4 )]
Tiles = []

# RETURNS TRUE IF A AND B ARE IN PROXIMITY OF S FROM EACH OTHER
def isClostTo( a, b, s ):
    rng = [b - s, b + s]
    if rng[0] <= a <= rng[1]:
        return True
    else:
        return False

# after every iteration of a move function, this will correct the coordinates of the tiles to the ones they are supposed to have
def CorrectTileCoordees():
    for k in range( 4 ):
        for l in range( 4 ):
            for m in range( len( Tiles ) ):
                if isClostTo( Tiles[m].X, Coordees[k][l][0], 30 ) and isClostTo( Tiles[m].Y, Coordees[k][l][1], 30 ):
                    Tiles[m].X = Coordees[k][l][0]
                    Tiles[m].Y = Coordees[k][l][1]
                    pygame.display.update()


# METHOD TO SEE SPAWN A RANDOM TILE
def refreshCoordees( ):
    for k in range( 4 ):
        for l in range( 4 ):
            itsThere = False
            for m in range( len( Tiles ) ):
                if isClostTo( Tiles[m].X, Coordees[k][l][0], 5 ) and isClostTo( Tiles[m].Y, Coordees[k][l][1], 5 ):
                    Coordees[k][l][2] = 1
                    itsThere = True
            if not itsThere:
                Coordees[k][l][2] = 0

# METHOD TO ASSIGN THE TILES USING THE CORDEES AND THEN DRAWING THEM, CALLED BY THE MOVETILES() METHODS
def assignRandom( ):
    exceptList = []
    for i in range(4):
        for j in range(4):
            exceptList.append([i, j])
    printList(exceptList)
    global Tiles
    exceptX, exceptY = [None], [None]
    for l in range( len( Coordees ) ):
        for k in range( len( Coordees ) ):
            if Coordees[l][k][2] == 1:
                for g in range(len(exceptList)):
                    if exceptList[g][0] == l and exceptList[g][1] == k:
                        print( 'just removed' )
                        print( exceptList[g] )
                        exceptList.remove( exceptList[g] )
                        break
    randomList = random.choice( exceptList )
    
    for k in range( 4 ):
        for l in range( 4 ):
            if k == randomList[0] and l == randomList[1]:
                TileObj = Tile( Coordees[randomList[0]][randomList[1]][0], Coordees[randomList[0]][randomList[1]][1],
                                TILE_SIDE, randomList[0], randomList[1], 2 )
                Coordees[randomList[0]][randomList[1]][2] = 1
                TileObj.Draw_()
                Tiles.append( TileObj )
                pygame.display.update()


def GiveCoordees(i, j):
    for t in Tiles:
        if isClostTo(t.X, Coordees[i][j][0], 10) and isClostTo(t.Y, Coordees[i][j][1], 10):
            return t
            



# METHOD TO MOVE THE TILES BASED ON USER IMPUT
def rightMovable( ):
    for i in range(4):
        for j in range(3):
            if Coordees[i][j][2] == 1:
                if Coordees[i][j + 1][2] == 0:
                    return True
                else:
                    if GiveCoordees(i, j).Value == GiveCoordees(i, j + 1).Value:
                        return True
    return False
    

def leftMovable( ):
    for i in range( 4 ):
        for j in range(1, 4 ):
            if Coordees[i][j][2] == 1:
                if Coordees[i][j - 1][2] == 0:
                    return True
                else:
                    if GiveCoordees(i, j).Value == GiveCoordees(i, j - 1).Value:
                        return True
    return False

def downMovable( ):
    for i in range( 3 ):
        for j in range( 4 ):
            if Coordees[i][j][2] == 1:
                if Coordees[i + 1][j][2] == 0:
                    return True
                else:
                    if GiveCoordees(i, j).Value == GiveCoordees(i + 1, j ).Value:
                        return True
    return False

def upMovable( ):
    for i in range( 1,4 ):
        for j in range( 4 ):
            if Coordees[i][j][2] == 1:
                if Coordees[i - 1][j][2] == 0:
                    return True
                else:
                    if GiveCoordees(i, j).Value == GiveCoordees(i - 1, j).Value:
                        return True
    return False

def moveTiles( ):
    global is_movable_there
    is_movable_there = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        refreshCoordees()
        CorrectTileCoordees()
        if upMovable():
            moveUp()
            CorrectTileCoordees()
            return True
        else: return False
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        refreshCoordees()
        CorrectTileCoordees()
        if downMovable():
            moveDown()
            CorrectTileCoordees()
            return True
        else: return False
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        refreshCoordees()
        CorrectTileCoordees()
        if leftMovable():
            moveLeft()
            CorrectTileCoordees()
            return True
        else: return False
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        refreshCoordees()
        CorrectTileCoordees()
        if rightMovable():
            moveRight()
            CorrectTileCoordees()
            return True
        else: return False
    else:
        return False

# ASSIGNS THE FIRST 2 RANDOM TILES, AND DRAWS THEM ON THE SCREEN
def AssignFirstTwo( ):
    global Tiles
    rand_Coordi_X = random.randrange( 4 )
    rand_Coordi_Y = random.randrange( 4 )
    rand_Coordi_X = 1
    rand_Coordi_Y = 2
    tiles_Obj = Tile( 0, 0, TILE_SIDE, rand_Coordi_X, rand_Coordi_Y, 2 )
    tiles_Obj.X = Coordees[rand_Coordi_X][rand_Coordi_Y][0]
    tiles_Obj.Y = Coordees[rand_Coordi_X][rand_Coordi_Y][1]
    Coordees[rand_Coordi_X][rand_Coordi_Y][2] = 1
    Tiles.append( tiles_Obj )
    rand_Coordi_X = choice( [e for e in range( 0, 4 ) if e not in [rand_Coordi_X]] )
    rand_Coordi_Y = choice( [r for r in range( 0, 4 ) if r not in [rand_Coordi_Y]] )
    rand_Coordi_X = 3
    rand_Coordi_Y = 0
    tiles_Obj2 = Tile( 0, 0, TILE_SIDE, rand_Coordi_X, rand_Coordi_Y, 2 )
    tiles_Obj2.X = Coordees[rand_Coordi_X][rand_Coordi_Y][0]
    tiles_Obj2.Y = Coordees[rand_Coordi_X][rand_Coordi_Y][1]
    Coordees[rand_Coordi_X][rand_Coordi_Y][2] = 1
    Tiles.append( tiles_Obj2 )
    print('just assigned the first 2')
    printList(Coordees)
    for tile in range( len( Tiles[:] ) ):
        Tiles[tile].Draw_()
    pygame.display.update()

# METHOD TO DO THE STUFF INSIDE THE PLAY GAME FUNCTION
def runPlay( ):
    WIN.blit( PLAY_IMAGE, ORIGIN )
    drawBG_BOX()
    pygame.display.update()
    assignCordees()
    AssignFirstTwo()
    pass
a = 2
# FUNCTION TO DO THE STUFF INSIDE THE LOOP OF THE PLAY GAME FUNCTION
def updatePlayInLoop( ):
    global Tiles, a

    if moveTiles():
        refreshCoordees()
        CorrectTileCoordees()
        print( "Just Before random assign *****************************************************************************************************" )
        printList(Coordees)
        assignRandom()
        print( "Just After Random assign *****************************************************************************************************" )
        printList(Coordees)
        for t in Tiles:
            t.SetImage_()
    pygame.display.update()

# DEFINING THE PLAY GAME FUNCTION
def playGame( ):
    play_Loop = True
    lost_Game = False
    clock = pygame.time.Clock()
    runPlay()
    while play_Loop:
        clock.tick( 60 )
        updatePlayInLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_Loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    lost_Game = True
        lost_Game = not (isMovable())
        
        if lost_Game:
            play_Loop = lostGame()
            lost_Game = False

# DEFINING THE LOST GAME FUNCTION, RETURNS FALSE IF YOU WANNA QUIT, TRUE IF YOU WANNA CONTINUE
def lostGame( ):
    lost_Loop = True
    result = False
    while lost_Loop:
        WIN.blit( LOST_IMAGE, ORIGIN )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lost_Loop = False
            if checkMouse( START_BTN_LOWER[0], START_BTN_LOWER[1], START_BTN_UPPER[0], START_BTN_UPPER[1], event ):
                print( "hi" )
                lost_Loop = False
                result = True
            if checkMouse( EXIT_BTN_LOWER[0], EXIT_BTN_LOWER[1], EXIT_BTN_UPPER[0], EXIT_BTN_UPPER[1], event ):
                lost_Loop = False
                result = False
        pygame.display.update()
    return result

# DEFINING THE START FUNCTION
def start( ):
    start_Loop = True
    while start_Loop:
        WIN.blit( BG_IMAGE, ORIGIN )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_Loop = False
            if checkMouse( START_BTN_LOWER[0], START_BTN_LOWER[1], START_BTN_UPPER[0], START_BTN_UPPER[1], event ):
                start_Loop = False
                playGame()
            if checkMouse( EXIT_BTN_LOWER[0], EXIT_BTN_LOWER[1], EXIT_BTN_UPPER[0], EXIT_BTN_UPPER[1], event ):
                start_Loop = False
        pygame.display.update()

start()
