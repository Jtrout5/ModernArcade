# Modern Arcade

Project Author: Jeramiah Trout
<details>
<summary>Quick Information</summary>
This repository hosts content which began as a group project for COMP 333, Software Engineering, at Wesleyan University. I have spun this repository off as a new personal project containing only the parts of the project I personally wrote, and will expand from that starting point. All content in this repository, except that which I specifically note as being sourced elsewhere, was created solely by me during the semester long group project.

 <br>
In this readme, you will find info on installing python, as well as getting this project to run on your system. There are also detailed descriptions for each of the games included, and the video guide shows some of these games being played. As new games are added, there will be updates to the readme providing details on the new releases. Please enjoy.

<br>

I have personally tested each game on Windows and Mac devices and believe everything to be fully functional and bug free. However, if you find crashes, launch failures, or bugs in your play time, please submit a bug report on the github page for this repository. Thank you for taking the time to read this document and for showing your interest in my project.

________
</details>
<details>
<summary> Getting Started </summary>
<details>
<summary>Python Installation</summary>

# Python 3.14 is now supported!!!

You may download the most recent release of Python 3.14 (3.14.2) at https://www.python.org/downloads/release/python-3142/ and then navigate to your specific platform and download the installer from there. I personally recommend scrolling all the way down to the files portion of the site and downloading the recommended installer directly instead of the using the install manager as the manager introduced some annoyance. After the download is complete, open the installer, and click "Install Now" or "Upgrade" (Upgrade is only available if you have an older release of the same version). Once installation is complete, you can use the rest of this guide to get started.
</details>

<details>
<summary>Graphics Installtion</summary>

## Graphics Package (Now Installed Automatically on First Launch)

This project is built using the CMU graphics library which can be found at https://academy.cs.cmu.edu/desktop. The December 8th update to this project now installs the most updated version of the graphics package for you on your 1st running of the pretend launcher or any game. If this process fails (which should not happen), then you should follow the above link, download the package as a zip, extract/expand, and then copy the cmu_graphics folder from the cmu_graphics_installer folder, and place it into the libraries folder of the project directory. It is important to only copy and move the cmu_graphics folder, not the entire cmu_graphics_installer folder. If future versions of this package release, you can delete the cmu_graphics folder from the libraries directory in this repository and then run any game or the launcher itself and the newest version will automatically be installed.
</details>

<details>
<summary>Launching the Project</summary>

# How to play

You can find a short video demo on YouTube at https://youtu.be/CQykV8IK4Tk. Note that it does not cover all of the games but shows a decent subset of the games and mechanics as well as a general guide for starting from the download to running the launcher. However, if you would prefer written step by step instructions from download to running, read below. 
<br >

Regardless of platform, please download or clone this entire project repository from the "main" branch. This can be accomplished by navigating to the main branch, and then clicking the green "code" button and either downloading as zip or copying the shown link and cloning via your favorite IDE with git cloning functionality, such as VS Code. Running any of the games or the Pretend Launcher will install all dependencies, though you may need to allow certain bits of access and control, but these popups should come up automatically if applicable.
<br>

You will find platform specific information below

<details>
<summary>MacOs</summary>

## MacOS Instructions for PretendLauncher.py
If you are on MacOS, you have 3 options for running the launcher:

1. Open PretendLauncher.py with VS code, and run through the play button at the top right  
or  
2. Open in Python Launcher (NOT IDLE) and run the script  
or  
3. Open a terminal window, navigate to the directory the launcher is in and run the launcher. Note that the launcher is in ModernArcade/apps/PretendLauncher, so you will have to navigate to the location you placed this repository first*


```bash
cd path/to/this/repository
cd apps/PretendLauncher
python3 PretendLauncher.py
```
Note that if you have multiple versions of python3 installed, (such as 3.6.4, 3.9.3, 3.13.7, 3.14.2), you may need to specify version in your command as shown below:

To check installed versions, simply run 

```bash
which -a python3
```
or 

```bash
python3 --vesion
```
____
For example, if you have vesion 3.13.7 and 3.14.1 and 3.12.9, you would run:

```bash
cd path/to/this/repository
cd apps/PretendLauncher
python3.13 PretendLauncher.py
```
____
</details>
<details>
<summary> Windows </summary>

## Windows Instructions for PretendLauncher.py

If you are on Windows you have 2 simple options to run the launcher:

1. Double click the PretendLauncher.py file as if it were an executable  
or  
2. Open the repository folder through VS code and click the play button at the top right while having the launcher file selected <br>
or
3. Open command prompt and navigate to the directory PretendLauncher.py is stored in, type "python3 PretendLauncher.py" and press Enter
____

</details>
</details>
</details>

<details>
<summary> Extra Information</summary>

## Launcher
<details>
<summary>PretendLauncher.py</summary>
This file acts as the launcher file for all of the games released with this project. It will make and maintain stats and key files for all of the included games. If you wish to know what stats are kept, you may check the keys files which should make it clear what game events are being tracked. 

<br>

If you delete the files or the entire Files folder, then the launcher will remake the files the next time it is run. The files are necessary for the games to work, and the games will crash on launch if the files are missing. This is solved by running the launcher again. If you delete the stats file for a specific game, your progress is erased for that game (or all games if you delete the Files folder)
</details>

## Games

<details>
<summary>Asteroids.py</summary>
This is a remake of the classic arcade game, Asteroids. In this version of the game, you have 3 HP instead of 1 so you will not die immediately to one hit. Additionally, you can move in 4 directions, relative to ship rotation instead of only forward in the direction you face, like in the original. Please note that "W" will accelerate the ship forward from the ship's perspective, not up or down according to your perspective, though those perspectives may occasionally overlap. Use WASD to accelerate in the following directions (Forward, Left, Back, Right) in relation to the ship. Use Left and Right arrow keys to accelerate your ship's rotation in those direcitons, and use spacebar to fire projectiles from the front of your ship in the direction you face. The asteroids have HP relating to their size, with the smallest asteroids exploding after one hit and the largest taking 4 shots to destroy, but point values are scaled with this in mind. All sizes of asteroids except the smallest will spawn 2 asteroids of the next size down at its location upon destruction. You will also encounter enemy saucers which will fire at you and call allies in to assist if you don't destroy them fast enough. Enemy saucer health scales with time played and destroying all enemy saucers on screen will result in an increased score multiplier. Enemy saucers can destroy asteroids but you will not receive score credit for asteroids destroyed by enemy saucers. You may pause and unpause with 'p', and restart the game after a game over by pressing enter.
</details>

<details>
<summary>ColorGame.py</summary>
This is an attention test described in a few psychology courses. Words will pop up at the top of the screen, and those words will be written in a certain color. To score, you must select and click the color of the word from your options. Those options are the 15 colored buttons at the bottom of the screen. The color buttons are placed in a frustrating order, on purpose, and some of the words are themselves colors. Example: You may receive the word "orange", written in the color cyan, and you will be correct if you click the cyan button, not the orange button. You will receive a time bonus of 1 second added to your countdown clock for every correct guess. You are granted 2 seconds per guess. This means that you can gain time if you answer correctly in under 1 second but you will lose time overall if you average longer time between guesses. Additionally, an incorrect guess will subtract time from your overall time, and no guess is treated as an incorrect guess, so you'll lose the 2 seconds it took to not guess and be penalized on top of that. You lose when you run out of time overall. 
</details>

<details>
<summary>Fireworks.py</summary>
This is a mindless stress relief style of "game", where you click on the screen and watch fireworks shoot up from the ground and explode where you clicked. This project has several features, such as screensaver mode, which handles clicking for you so you can put it up as a screensaver if you wish. You can still make manual clicks in screensaver mode and you can also control the rate of firework launches in screensaver mode from the main menu. Additional features include Starry Night mode which leaves small circles at the point of explosion which, overtime lead to a night sky-like background populated with colorful "stars". This mode is compatibale with manual clicks and with screensaver mode. Finally, there is also twinkle mode which will select "stars" at random to twinkle. This mode can only be activated if Starry Night mode is also active, and is compatible with manual clicks and screensaver mode. The available colors are the 9 on the main menu. Select colors by clicking on them, or alternatively using the select all or deselect all buttons. The game will prevent you from continuing if you fail to select a color on the main screen. 
</details>

<details>
<summary>FlappyBat.py</summary>
This is a knockoff of flappy bird, a popular phone app from the early 2010s. There are aspects of the game that set it apart, however. The creator of this game was bitten by a bat at Wesleyan and so chose to model a bat at the player character for this game. The game also takes place at night with a starry background, and the cities in the distance are generated from the same model that generates the cities in MissileCommand.py which is mentioned later in this document. You will select your difficulty from the main menu. Difficulty is relating to the speed at which the pipes move in the beginning. In all difficulty modes, speed will increase over time. Your bat is affected by gravity and you flap by pressing spacebar which will send you upwarards. Be careful to avoid the green pipes, the ground, and flying too high into the sky, as your bat will crash and your round will end. You may pause and unpause at any point with 'p' and you may reselect difficulty upon failure by pressing escape, or simply replay at the same difficulty upon failure with enter.
</details>

<details>
<summary>Hangman.py</summary>
To guess a letter, you can either type the letter using your keyboard or click the box surrounding the letter on the screen. This game is similar to the standard Hangman experience, but with a few key differnces. Internal development reffered to this game as Hangman Hard Mode becase it is significantly harder than standard hangman. To provide balance, you only fail after 9 incorrect letter guesses. The difficulty is a result of the following design choices. 

<br>

1. The word list is 365k words long and contains words from past and present english dictionaries. This means that there are hundreds of old english words with weird spellings.  

2. The game will operate as normal hangman until you have selected a correct letter, which it will show and reveal as correct. Subsequent guesses after choosing your first correct letter will function in a different manner, as the program attempts to find a word matching all previous characteristics, (length, what letters are not present, what letters are present and in what specific locations) but without your most recent guess. It collects all words meeting those criteria and picks one randomly to be the new word. If it cannot find a word with those characteristics, you are granted that letter as a correct guess. This continues in a cycle until you figure out the word or guess incorrectly 9 times. You may try to guess a new word by clicking the try again button opon winning or losing the round
</details>

<details>
<summary>Minesweeper.py</summary>
This game is the standard minesweeper experience. You select a difficulty and click on the board. The numbers in each square represent how many its adjacent 8 squares are bombs. You can place flags with right click on physical mice, or the two-finger click on trackpads. Flags should be used to help you remember places that you think are bombs. Rates of bomb placement scale up with difficulty, as does the size of the board. There is also a system in place which will automatically clear all squares adjacent to a square containing a 0 once it is discovered, since it is the case that a 0 means that all adjacent squares are safe. This is a quality of life feature which speeds up each game since you do not have to manually clear all squares adjacent to a 0. You may pause and see help info with either 'p' or 'h'. Upon winning the game or failing, you may return to the main menu with escape and select difficulty to play another round. Your first click will reveal information about the square you click and all adjacent squares, at minimum, and will automatically flag bombs in that subset of squares. More information will be revelaed if a zero happens to fall in the subset cleared by your first click.
</details>

<details>
<summary>MissileCommand.py</summary>
Basic Information: This is a modern remake of an arcade game, Missile Command. In this game, you control 3 missile batteries tasked with protecting 6 cities during an overnight attack. If you wish to manually switch which missile battery you are controlling at any time, you may do so by using the left and right arrow keys. Additionally, upon firing, the game will automatically select the next missile battery in rotation. You shoot by clicking your mouse on the screen at the place you want to fire a missile towards. The missile will fire from whichever missile battery you have selected, which will be outlined in white. Once reaching its target destination, your missile will explode and the explosion will remain for a few seconds as a fireball, able to destroy incoming enemies, allowing you to score. If you hit an enemy with a missile directly, instead of via the explosion, you will earn a 5x score bonus. 

<br>

More Gameplay: Each missile battery must reload after firing, and it has its own ammo which cannot be moved to other missile batteries. If an enemy hits any missile battery, it is damaged for a set amount of time and cannot fire or be selected during that time. This damaged state will result in a red highlight around the missile battery. This damage time is determined based on the type of enemy which caused the damage. Repair time after a large enemy hit is 25 seconds, and repair time after a small enemy hit is 10 seconds. This time is cumulative, meaning that subsequent hits extend repair time. This a a change from the original aracde game, where a single hit to a missile battery resulted in total destruction of the missile battery for the level, with repair immediate upon survival of the level. In order to balance this feature of repair time instead of destruction, repair time will carry over between levels. If a large enemy hits a city, it is immediately destroyed in its entirety. If a small enemy hits a city, the building(s) hit by the small enemy will be destroyed and the city overall will take damage. If the city takes damage in this way 3 times, it will be wholly destroyed. You will receive extra ammo each level, on top of the ammo you retained, but the number of enemies scales faster than the ammount of new ammo granted at later levels, so pick your targets carefully, and keep as much ammo as possible. All enemies can be destroyed in 1 shot.
<br >

Enemies: You will face tougher enemies as you advance in the game. You begin by defending against basic missiles will travel directly down and with a constant speed. The next enemy type is a bomber plane which will drop bombs across the map, but can be destroyed before dropping all bombs. The next enemy type are missiles with horizontal velocity which are affected by gravity, so they will move faster as they travel. The next enemy is a "multi-bomb" which will explode well above the ground and launch multiple smaller bombs, but it can be destroyed before reaching that unknown height. The next enemy is a smart missile which will manuever to avoid fireballs. It is affected by gravity and will speed up as it falls, and has limited angles to avoid fireballs, but it is best to try and hit this enemy directly or nearly directly. The final enemy type is the UFO. You absolutely can not afford to let this enemy reach the space above your middle missile battery, because it will launch devestating strikes of smaller bombs towards your cities and missile batteries. This is the most dangerous enemy and should be your primary target if you spot one. 
<br >

There are certain score milestones which enable you to unlock bonus cities, which will replace a destroyed city at the start of the next level in the event that you were unable to protect it. Bonus cities will only spawn if you survived the level, by keeping at least one city alive. Since you gain points for destruction, including a 5x muliplier on direct hit, and bonus points for unspent ammo, and cities kept alive, you will earn bonus cities faster the better you are at the game. Cities will spawn at the start of a new level if you ahve space for a new city. If ypu do not have space, you will retain your bonus city until you reach the start of a level and have space for the city. Bonus cities stack, so it is possible to have several bonus cities, and therfore multiple cities created at the start of a level. There is no win condition for this game, as eventually, you will be unable to protect all of your cities, despite your best efforts.
<br >

Allied flak gunners have arrived to support the play in the Nov 24 2025 update, each city building has an operational flak gun which will automatically take aim and target incoming enemies. They have an incredible rate of fire, tempered by a lack of accuracy, but they can deal serious damgage. It would be unwise to rely soley on the flak gunners, but they are valuable teammates capable of destroying each type of enemy projectile if they are lucky enough to make contact. They can even provide cover for player missile batteries and save the player from an exposion causing damage and increasing the delay for repairs. Projectiles destroyed my the flak gunners also count towards player score.
</details>

<details>
<summary>Simon.py</summary>
This is the standard Simon experience, as the computer makes a sequence using the available 4 colored buttons and you must click the same pattern to succeed. The pattern grows longer as time progresses, always building on the existing pattern until you lose. Gameplay is simple, just watch the computer play the pattern, and repeat it. 
</details>

<details>
<summary>SubGame.py</summary>
This game places you as the commander of a submarine in an underwater minefield, targeted by mines, depth charges, and (in an upcoming update in december, other submarines.) It is your job to survive as long as possible. You have torpedoes to preotect yourself against mines fired with left arrow key (front of sub) and right arrow key (back of sub). Torpedoes can cause a chain reaction of mine explosions You may also angle your submarine counterclockwise with Q or clockwise with E. Finally, actually moving your submarine is accomplished with WASD keys, where W and S move the submarine upwards and downwards with respect to the screen and general notions of up and down while A and D move the ship forward or backwards relative to its rotation. Periodically, you willbe targeted with depth charges which will target your general location within the ocean and explode near your last known coordinates. Depth charges can also start a chain reaction, blowing up nearby mines. You will earn score for all depth charges avoided and mines destroyed by your torpedoes, depth charges or chain reactions. There is no win condition in this game, your goal is to survive as long as possible. 
</details>

<details>
<summary>TowerOfHanoi.py</summary>
This is a digital recreation of the Tower Of Hanoi Puzzle, where you must move rings from one rod to another under the following rules. All rings are stacked smallest to largest (when viewed top to bottom) on the leftmost rod to start. You may only move one ring at any time, and a move includes taking it from one rod and placing it on another. This means you cant move the entire tower at once or take a ring from a rod, set it on the table and then start moving another before placing the orginal ring on a rod. No ring can be under a ring larger than itself at any time. The final position of the game must contain all rings stacked exactly as they were in the beginning, but on either the middle or rightmost rod. 

<br>
To play the game, click and drag a ring from its current position and move it to another rod. Assuming you have brought the rod somewhere that is allowed, simply release the mouse and the ring will snap onto the rod. If the move were to be invalid for any reason, the ring will automatically be returned to where it was at the beginning of your move, and you will not be penalized by the move counter. The game keeps track of your move count so it can reveal whether or not your solution was perfect upon completion. The rings are sized automatically based on the number of rings, so as you progress to higher numbers of rings, the rings themselves get shorter. You will be unable to move any rings that are not already at the top of their rod. 

<br>
Additionally, you can save your progress at any point by pressing the save game button. This will save the exact current positioning of the board such that you can load this state at any point in the future, including future launches of the game. There can only be one active save at a time, so saving a second time will overwrite the previous save automatically. Upon completion of the current level, you will automatically unlock access to the next level, but you will not progress to it unless you choose to do so. Upon launching the game, it will automatically create the puzzle based on the highest level you have unlocked. At any point, you may reset your current level, or start a new puzzle at any level you have unlocked by using the selection button. If you wish to save your current progress before selecting a new level, you may do so with the save button, but this will overwrite past saves. If you elect to not save your progress, starting a new level irreversibly deletes the progress you have made on your current level. 
</details>

<details>
<summary>Typespeed.py</summary>
This game is a simple typing exercise in typing ability, as words move from left to right across the screen and it is the players job to type the words correctly. As you go on a streak, your score multiplier will increase which also leads to a higher frequency of word spawns. It is impossible to get every word, and that's why you are not severely penalized for words getting passed you. Depending on your multiplier, after a certain number of words pass by without you typing a correct word, your multiplier will decrease. Be careful, because typing an incorrect word will drop the muliplier by a lot more and reset your streak. The game is played using the keyboard to type the words. Your current typed word appears at the top of the screen, and you press enter to submit. Backspace works as expected, where 1 press deletes the most recent letter only.
</details>

## Extra Files

<details>
<summary>libraries</summary>
This is the folder that will be accessed by all of the games and the launcher for purposes of audio, text, and images, as well as to obtain the list of required packages to be installed, found in a txt file called requirements.txt. These packages will be installed upon running the Pretend Launcher or one of the games. More explicit definitions of included items are listed below
<details>
<summary>words_alpha.txt</summary>
This folder will come populated with a slightly altered version of the words_alpha.txt file available at https://github.com/dwyl/english-words/blob/master/words_alpha.txt. The alterations are just the removal of words that are 4 letters or fewer, but you can feel free to look at the source or replace the file attached in this repository with that file instead. 
</details>
<details>
<summary>Graphics</summary>
Upon running the launcher or any game, the libraries folder will become populated with the cmu_graphics package via an automatic download if it was not already added manually by the user. This will take some time, depending on the speed of your internet, but it is a one time install. All subsequent launches will be instant. This graphics package was developed and is currently maintained by students at Carnegie Mellon University.
</details>

<details>
<summary>Audio</summary>
This folder comes populated with mp3 files used in some of the games. Deleting this folder or files within the folder may cause game crashes as audio files are attempted to be played. These files were made by using free audio available online through open license and through garage band built in sounds. Each game containing audio can have that audio muted by pressing the m key while in game.
</details>

<details>
<summary>Thumbnails</summary>
 Additionally, there is a Thumbnails folder containing images used to represent games via the Pretend Launcher. These are images captures as screenshots from in game, with only minimal editing to remove menus and UI elements like score counters and settings buttons. The screenshots were then sized down from 8k to 400x400 pixels such that they could be used on the game buttons in the launcher without causing lag on lower end hardware.
</details>
</details>
</details>