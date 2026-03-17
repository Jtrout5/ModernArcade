import os
import sys
import subprocess
import zipfile
import shutil

file_path = os.path.abspath(__file__)
directory_path = os.path.dirname(file_path)
os.chdir(directory_path)
currentFile =  os.path.basename(__file__)
gameName = currentFile[:-3]
rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
lib_path = os.path.join(rootPath, "libraries")
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)

try:
    import pyautogui
    import requests
except ImportError as e:
    os.system("pip3 install -r ../../libraries/requirements.txt")
    import pyautogui
    import requests

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
app.shipSpeed = 5
app.ballSpeed = 8
app.launchSpeed = 10
app.play = True
app.spawn = 10


default = [0,0,0,0,0,0,0,0,0]
keys = ["HighScore", "GamesPlayed", "YellowSubAch", "MinesBlownUp", "TorpsFired", "TorpsHit" ,"PowerUpsCollected", "TimesLaunched", "HideStartScreen"] 
fullInfoList = [] 

app.autofs = 0

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

space = Rect(0,0,app.width, app.height)
bunkers = Group()
balls = Group()
enemyShots = Group()



def create_bunker(location_group):
    cx = location_group * app.width/8
    cy = 3*app.height/4
    for i in range(35):
        offsetX = (i%7)-3
        offsetY = (i//7)
        rad = 3
        bunkers.add(Circle(cx+offsetX*rad*1.5, cy+offsetY*rad*1.5, rad, fill="lime"))

for i in range(1,8,2):
    create_bunker(i)

app.line = Line(0,17*app.height/18, app.width, 17*app.height/18, fill='grey')
app.timeSince = 0
head = Circle(app.width/2, app.line.y2,7, fill = 'white')
ship = Group(head, Rect(head.centerX, head.centerY, 40, 15, align = 'top', fill='white'))
ship.bottom = app.line.y2

def spawn_balls(x,y,angle):
    '''
    Takes 3 args, 2 positional, and 1 directional
    Returns no values but does add a shape to a relevant group    
    '''
    new = Oval(x,y,2,8, fill='white')
    new.next = getPointInDir(x,y,angle,app.ballSpeed)
    balls.add(new)
    fullInfoList[0]+=1

def spawn_enemy_shots(x,y,angle):
    '''
    Takes 3 args, 2 positional, and 1 directional
    Returns no values but does add a shape to a relevant group    
    '''
    new = Oval(x,y,4,4, fill='white')
    new.next = getPointInDir(x,y,angle,app.ballSpeed)
    enemyShots.add(new)

def move_balls():
    '''
    no args, no returns
    moves shots fired by the player based on their aiming point.
    removes them if they leave the screen.
    '''
    for ball in balls:
        ball.centerX, ball.centerY = ball.next
        ball.next = getPointInDir(ball.centerX,ball.centerY, 0, app.ballSpeed)
        if(not(space.containsShape(ball))):
            balls.remove(ball)

def move_enemy_shots():
    '''
    no args, no returns
    moves shots fired by enemies based on their aiming point.
    removes them if they leave the screen.
    '''
    for ball in enemyShots:
        ball.centerX, ball.centerY = ball.next
        ball.next = getPointInDir(ball.centerX,ball.centerY, 180, app.ballSpeed)
        if(not(space.containsShape(ball))):
            enemyShots.remove(ball)

def bunker_vs_balls():
    for ball in balls:
        if(ball.top<bunkers.top or ball.bottom>bunkers.bottom):
            None
        else:
            for i in range(len(bunkers.children)-1, -1, -1):
                defense = bunkers.children[i]   
                if ball.hitsShape(defense):
                    balls.remove(ball)
                    bunkers.remove(defense)
                    return

def bunker_vs_enemy_shots():
    for ball in enemyShots:
        if(ball.top<bunkers.top or ball.bottom>bunkers.bottom):
            None
        else:
            for defense in bunkers:
                if ball.hitsShape(defense):
                    enemyShots.remove(ball)
                    bunkers.remove(defense)
                    return

def hit_detectiion():
    bunker_vs_balls()
    bunker_vs_enemy_shots()

def onKeyHold(keys):
    '''
    Built in CMU function which takes a list of currently held keys as an argument
    In this script, it is used to move the ship and fire shots
    '''
    if('left' in keys):
        ship.centerX-=app.shipSpeed
    if('right' in keys):
        ship.centerX+=app.shipSpeed
    if('space' in keys):
        if(app.timeSince == 0):
            spawn_balls(head.centerX, head.centerY, 0)
            app.timeSince = app.launchSpeed

def onStep():
    '''
    CMU Built-In Function
    Takes no arguments and returns no values
    Anything called in this function is called app.stepsPerSecond many times per second
    '''
    if(app.autofs<=1):
        app.autofs += 1
    if(app.autofs == 1):
        pyautogui.keyDown("command")
        pyautogui.keyDown('ctrl')
        pyautogui.press('f')
        pyautogui.keyUp("command")
        pyautogui.keyUp("ctrl")
    if(app.play==True):
        if(app.timeSince>0):
            app.timeSince-=1
        move_balls()
        move_enemy_shots()
        hit_detectiion()
        if(app.spawn == 0):
            spawn_enemy_shots(randrange(0,app.width), 20, 180)
            app.spawn = 10
        else:
            app.spawn-=1

app.run()