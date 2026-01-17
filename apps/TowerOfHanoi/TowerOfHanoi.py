import os
import sys
import subprocess
import zipfile
import shutil

try:
    import pyautogui
    import requests
except ImportError as e:
    os.system("pip3 install -r requirements.txt")
    import pyautogui
    import requests

file_path = os.path.abspath(__file__)
directory_path = os.path.dirname(file_path)
os.chdir(directory_path)
currentFile =  os.path.basename(__file__)
gameName = currentFile[:-3]
rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
lib_path = os.path.join(rootPath, "libraries")
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)

def download_zip_file(url, destination_folder, filename):
    '''
    Takes 3 args, a url for the file, a destination folder, and a name to give the file
    Downloads the file found at url, gives it filename as a name and places it in the destination folder
    '''
    file_path = os.path.join(destination_folder, filename)
    response = requests.get(url, stream=True)
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            
def unzip_all(zip_file_path, destination_directory):
    """
    Takes 2 args, a path to a zip file and a path to the destination folder
    """
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_directory)

try:
    from cmu_graphics import *
except ImportError as e:
    zip_url = 'https://s3.amazonaws.com/cmu-cs-academy.lib.prod/desktop-cmu-graphics/cmu_graphics_installer.zip'  
    output_directory = "../../libraries"
    output_filename = "cmu_graphics_installer.zip"
    download_zip_file(zip_url, output_directory, output_filename)
    unzip_all(output_directory+'/cmu_graphics_installer.zip', output_directory)
    shutil.move(output_directory+"/cmu_graphics_installer/cmu_graphics", "../../libraries")
    os.remove("../../libraries/"+output_filename)
    shutil.rmtree("../../libraries/cmu_graphics_installer")
    from cmu_graphics import *


size = pyautogui.size()
width = size[0]
height = size[1]
app.width = width
app.height = height
app.moveCount = 0

app.setMaxShapeCount(100000000)
app.autofs = 0
app.maxSize = (0.3)*width
app.minSize = (1/40)*width

default = [0,0,0,0,0,3]
keys = ["HighestTowerCompleted", "TotalTowersCompleted", "TimesReset", "TimesPerfect", "TimesLaunched", "HighestLevel"] 
fullInfoList = []
allRods = Group()
allDiscs = Group()
postGame = Group()
leftDiscs = [None]
midDiscs = [None]
rightDiscs = [None]
colors = ['red', 'yellow', 'blue']


def file_checking(path, default):
    '''
    Takes 2 args, path for which file to look for, 
    default is the default info for the game, 
    returns no values but creates text files
    Looks for necessary game files. Creates and populates the files if they are not found in the expected directory
    Takes the values from the files, whether already existing or new and puts the values into a list for use later
    '''
    directory = "Files"
    properPath = os.path.join(directory, path)
    if(not os.path.exists(directory)):
        os.makedirs(directory, exist_ok=True)
    if (not os.path.exists(properPath)):
        with open(properPath, 'w') as f:
            f.seek(0)
            for i in range(len(default)):
                f.write((str)(default[i])+"\n")
    if("Stats" in properPath):
        with open(properPath, "r+") as gameInfo:
            for thing in gameInfo:
                thing = thing.strip()
                if thing != '':
                    fullInfoList.append((int)(thing))
            if(len(default)>len(fullInfoList)):
                keysFile = open("Files/"+gameName+"Keys.txt", "r+")
                start = len(fullInfoList)
                for i in range(start,len(default)):
                    fullInfoList.append(default[i])
                    gameInfo.seek(0,2)
                    gameInfo.write((str)(fullInfoList[i])+"\n")
                    keysFile.seek(0,2)
                    keysFile.write(keys[i] + "\n")

file_checking(gameName+"Stats.txt", default)
file_checking(gameName+"Keys.txt", keys)
gameInfo = open("Files/TowerOfHanoiStats.txt", "r+")
app.level = fullInfoList[5]
app.absX = 0
app.absY = 0
app.roundOver = False
reset = Rect(0,0,width/15, height/20, fill='white', border = 'black')
reset.name = Label("Reset Level", reset.centerX, reset.centerY)
newLevel = Rect(width, 0, width/15, height/20, fill = 'white', border = 'black', align = 'top-right', visible = False)
newLevel.name = Label("Next Level", newLevel.centerX, newLevel.centerY, visible = False)
closeGameButton = Rect(width/2, 0, width/15, height/20, fill='white', border = 'black')
closeGameButton.name = Label("Close Game", closeGameButton.centerX, closeGameButton.centerY)
backToLauncher = Rect(closeGameButton.left, closeGameButton.top, closeGameButton.width, closeGameButton.height, fill="white", border = 'black', align = 'top-right')
backToLauncher.name = Label("Return to Launcher", backToLauncher.centerX, backToLauncher.centerY)
backToLauncher.game = "PretendLauncher/PretendLauncher.py"


def onStep():
    '''
    CMU built in function
    All code in this body is executed app.stepsPerSecond many times every second
    Used to show motion in this project
    '''
    if(app.autofs<=5):
        app.autofs += 1
    if(app.autofs == 4):
        pyautogui.keyDown("command")
        pyautogui.keyDown('ctrl')
        pyautogui.press('f')
        pyautogui.keyUp("command")
        pyautogui.keyUp("ctrl")
    for ring in allDiscs:
        if(ring.canMove == True):
            ring.centerX, ring.centerY = (app.absX, app.absY)
            
        
def create_rod(x, discs):
    rod = Group()
    center = Rect(x,height,width//75, 4*(height//5), align = 'bottom')
    top = Circle(center.centerX, center.top, center.width/2)
    rod.add(center,top)
    rod.topDisc = discs[0]
    return rod

def create_ring(x, i, size):
    ring = Rect(x, height-(app.ringHeight*i), size, app.ringHeight, fill = colors[i%3], align = 'bottom', border = 'black')
    ring.id = app.level-i
    ring.topLeft = False
    ring.topMid = False
    ring.topRight = False
    ring.canMove = False
    ring.origin = 0
    leftDiscs.insert(0,ring)
    return ring

def start_level():
    app.perfectMoves = pow(2,app.level) - 1
    newLevel.visible = False
    newLevel.name.visible = False
    allRods.clear()
    allDiscs.clear()
    postGame.clear()
    app.moveCount = 0
    leftDiscs.clear()
    leftDiscs.append(None)
    midDiscs.clear()
    midDiscs.append(None)
    rightDiscs.clear()
    rightDiscs.append(None)
    starting = [None]
    app.allowableSizes = []
    app.ringHeight = (4*app.height//(5*app.level))
    variance = (app.maxSize - app.minSize)/(app.level-1)
    for i in range(app.level):
        starting.append(i+1)
        app.allowableSizes.append(app.maxSize-(variance*i))
    app.leftRod = create_rod(width/5, starting)
    app.centerRod = create_rod(width/2, [None])
    app.rightRod = create_rod(4*width/5, [None])
    allRods.add(app.leftRod, app.centerRod, app.rightRod)
    for i in range(app.level):
        allDiscs.add(create_ring(app.leftRod.centerX, i, app.allowableSizes[i]))
    for ring in allDiscs:
        if(ring.id == 1):
            ring.topLeft = True
    app.roundOver = False
    update_stats()
        
def select_disc(disc):
    disc.border = 'lime'
    disc.canMove = True
    if disc in leftDiscs:
        leftDiscs.remove(disc)
    if disc in midDiscs:
        midDiscs.remove(disc)
    if disc in rightDiscs:
        rightDiscs.remove(disc)

def win():
    app.roundOver = True
    newLevel.visible = True
    newLevel.name.visible = True
    postGame.add(Label("You solved the %d disc version of the Tower of Hanor puzzle in %d moves" %(app.level, app.moveCount), width/2, height/20))
    if(app.moveCount == app.perfectMoves):
        postGame.add(Label("That solution was perfect", width/2, height/10))
        fullInfoList[3]+=1
    else:
        postGame.add(Label("That solution was not the best, and could have been completed in %d fewer moves" %(app.moveCount - app.perfectMoves), width/2, height/10)) 
    if(app.level>fullInfoList[0]):
        fullInfoList[0]=app.level 
    fullInfoList[1]+=1
    update_stats()  

    
    
def check_win():
    countMid = 0
    countRight = 0
    if(len(midDiscs)==app.level+1):
        for i in range(app.level):
            if(midDiscs[i].id == i+1):
                countMid+=1
    elif(len(rightDiscs)==app.level+1):
        for i in range(app.level):
            if(rightDiscs[i].id ==i+1):
                countRight+=1
    if(countMid==app.level or countRight == app.level and app.roundOver == False):
        win()
            
            
         
def onMousePress(x,y):
    app.absX = x
    app.absY = y
    if(app.roundOver == False):
        for disc in allDiscs:
            if((disc == leftDiscs[0] or disc == midDiscs[0] or disc == rightDiscs[0]) and disc.contains(x,y)):
                select_disc(disc)
                app.moveCount+=1
    if(reset.contains(x,y)):
        if(app.roundOver == False):
            fullInfoList[2]+=1
        start_level()
    if(newLevel.visible == True and newLevel.contains(x,y)):
        app.level+=1
        if(app.level>fullInfoList[5]):
            fullInfoList[5] = app.level
        start_level()
    if(closeGameButton.contains(x,y)):
        update_stats()
        sys.exit(0)
    if(backToLauncher.contains(x,y)):
        update_stats()
        os.chdir("../")
        subprocess.Popen([sys.executable, backToLauncher.game])
        sys.exit(0)
        
            
def update_stats():
    '''
    Takes no arguments and returns no values
    Updates values relating to stored stats outside of the program
    '''
    gameInfo.seek(0)
    for i in range(len(fullInfoList)):
        gameInfo.write((str)(fullInfoList[i])+"\n")

def onMouseDrag(x,y):
    app.absX = x
    app.absY = y


def snap_disc(disc):
    distLeft = distance(disc.centerX, disc.centerY, app.leftRod.centerX, app.leftRod.top)
    distMid = distance(disc.centerX, disc.centerY, app.centerRod.centerX, app.centerRod.top)
    distRight = distance(disc.centerX, disc.centerY, app.rightRod.centerX, app.rightRod.top)
    correct = min(distLeft, distMid, distRight)
    if(correct == distLeft and (leftDiscs[0] == None or disc.id < leftDiscs[0].id)):
        locY = app.height - ((app.ringHeight)*(len(leftDiscs)-1))
        disc.centerX, disc.bottom = (app.leftRod.centerX, locY)
        leftDiscs.insert(0,disc)
        if(disc.origin==0):
            app.moveCount-=1
        disc.origin = 0
    elif(correct == distMid and (midDiscs[0] == None or disc.id < midDiscs[0].id)):
        locY = app.height - ((app.ringHeight)*(len(midDiscs)-1))
        disc.centerX, disc.bottom = (app.centerRod.centerX, locY)
        midDiscs.insert(0, disc)
        if(disc.origin==1):
            app.moveCount-=1
        disc.origin = 1
    elif(correct == distRight and (rightDiscs[0] == None or disc.id < rightDiscs[0].id)):
        locY = app.height - ((app.ringHeight)*(len(rightDiscs)-1))
        disc.centerX, disc.bottom = (app.rightRod.centerX, locY)
        rightDiscs.insert(0,disc)
        if(disc.origin==2):
            app.moveCount-=1
        disc.origin = 2
    elif(disc.origin == 0):
        locY = app.height - ((app.ringHeight)*(len(leftDiscs)-1))
        disc.centerX, disc.bottom = (app.leftRod.centerX, locY)
        leftDiscs.insert(0,disc)
        app.moveCount-=1
    elif(disc.origin == 1):
        locY = app.height - ((app.ringHeight)*(len(midDiscs)-1))
        disc.centerX, disc.bottom = (app.centerRod.centerX, locY)
        midDiscs.insert(0, disc)
        app.moveCount-=1
    else:
        locY = app.height - ((app.ringHeight)*(len(rightDiscs)-1))
        disc.centerX, disc.bottom = (app.rightRod.centerX, locY)
        rightDiscs.insert(0,disc)
        app.moveCount-=1

def onMouseRelease(x,y):
    app.absX = x
    app.absY = y
    for disc in allDiscs:
        if(disc.canMove == True):
            snap_disc(disc)
        disc.border = 'black'
        disc.canMove = False
        if(disc == leftDiscs[0]):
            disc.topLeft = True
        elif(disc == midDiscs[0]):
            disc.topMid = True
        elif(disc == rightDiscs[0]):
            disc.topRight = True
        else:
            disc.topLeft = False
            disc.topMid = False
            disc.topRight = False
    check_win()
    update_stats()

fullInfoList[4]+=1    
start_level()


app.run()