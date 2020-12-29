
___________.__               _________.__                      
\__    ___/|  |__   ____    /   _____/|__| ____   ____   ____  
  |    |   |  |  \_/ __ \   \_____  \ |  |/ __ \ / ___\_/ __ \ 
  |    |   |   Y  \  ___/   /        \|  \  ___// /_/  >  ___/ 
  |____|   |___|  /\___  > /_______  /|__|\___  >___  / \___  >
                \/     \/          \/         \/_____/      \/ 
#Before you play:
this game requires python 3.5 and PyGame v1.9.2
please read below for controls

#files
This game has 3 folders that contain images:
- icon
- player1
- player2

... and program file with musics in general folder:
- MG-shoot.ogg(music - sound effect for machinegun))
- shieldblocked.ogg(music - sound effect for shield blocking)
- shieldcharge.ogg(music - sound effect for shield dashing)
- shotgun-shoot.ogg(music - sound effect for shotgun)
- won.ogg(music - opened after winner is determined)
- menu.ogg(music - opened in the menu of the program)
- gameFile.py(python file - starts the game and loops until the user decides to quit)

any of the missing file will cause the error so make sure all files are there

#HOW TO LAUNCH THE GAME:
simply open gameFile.py and you are good to go!

#CONTROLS:
for player1:
    1, 2, 3, 4, 5, - switch units
    W - Up
    A - Left
    S - Down
    D - Right
    G - shoot/use ability

for player2:
    j, k, l, ;(semicolon), '(QUOTE)  - switch units  <- place your pinkie on j for maximum controls
    UPARROW - Up
    LEFTARROW - Left
    DOWNARROW - Down
    RIGHTARROW - Right
    SLASH - shoot/use ability

CLASSES:
shotgun
    shoots spreading pallets
machinegun
    shoots bullets in a high fire rate
shield
    blocks the bullet with the shield,
    dashes instead of shooting
