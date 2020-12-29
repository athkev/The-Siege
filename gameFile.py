#Program Modules
import pygame
import os

#Initialize PyGame
pygame.init()

###getting images from folder (numbers after direction are for sprite animations)
#player1's class: machinegun and shotgun (same image)
Player1MGDownRest = "player1/shotgun&mg/Player1MGDownRest.jpg"
Player1MGDown1 = "player1/shotgun&mg/Player1MGDown1.jpg"
Player1MGDown2 = "player1/shotgun&mg/Player1MGDown2.jpg"
Player1MGLeftRest = "player1/shotgun&mg/Player1MGLeftRest.jpg"
Player1MGLeft1 = "player1/shotgun&mg/Player1MGLeft1.jpg"
Player1MGLeft2 = "player1/shotgun&mg/Player1MGLeft2.jpg"
Player1MGRightRest = "player1/shotgun&mg/Player1MGRightRest.jpg"
Player1MGRight1 = "player1/shotgun&mg/Player1MGRight1.jpg"
Player1MGRight2 = "player1/shotgun&mg/Player1MGRight2.jpg"
Player1MGUpRest = "player1/shotgun&mg/Player1MGUpRest.jpg"
Player1MGUp1 = "player1/shotgun&mg/Player1MGUp1.jpg"
Player1MGUp2 = "player1/shotgun&mg/Player1MGUp2.jpg"

#player1's class: shield
Player1ShieldDownRest = "player1/shield/Player1ShieldDownRest.jpg"
Player1ShieldDown1 = "player1/shield/Player1ShieldDown1.jpg"
Player1ShieldDown2 = "player1/shield/Player1ShieldDown2.jpg"
Player1ShieldLeftRest = "player1/shield/Player1ShieldLeftRest.jpg"
Player1ShieldLeft1 = "player1/shield/Player1ShieldLeft1.jpg"
Player1ShieldLeft2 = "player1/shield/Player1ShieldLeft2.jpg"
Player1ShieldRightRest = "player1/shield/Player1ShieldRightRest.jpg"
Player1ShieldRight1 = "player1/shield/Player1ShieldRight1.jpg"
Player1ShieldRight2 = "player1/shield/Player1ShieldRight2.jpg"
Player1ShieldUpRest = "player1/shield/Player1ShieldUpRest.jpg"
Player1ShieldUp1 = "player1/shield/Player1ShieldUp1.jpg"
Player1ShieldUp2 = "player1/shield/Player1ShieldUp2.jpg"

#player2's class: machinegun and shotgun
Player2MGDownRest = "player2/shotgun&mg/Player2MGDownRest.jpg"
Player2MGDown1 = "player2/shotgun&mg/Player2MGDown1.jpg"
Player2MGDown2 = "player2/shotgun&mg/Player2MGDown2.jpg"
Player2MGLeftRest = "player2/shotgun&mg/Player2MGLeftRest.jpg"
Player2MGLeft1 = "player2/shotgun&mg/Player2MGLeft1.jpg"
Player2MGLeft2 = "player2/shotgun&mg/Player2MGLeft2.jpg"
Player2MGRightRest = "player2/shotgun&mg/Player2MGRightRest.jpg"
Player2MGRight1 = "player2/shotgun&mg/Player2MGRight1.jpg"
Player2MGRight2 = "player2/shotgun&mg/Player2MGRight2.jpg"
Player2MGUpRest = "player2/shotgun&mg/Player2MGUpRest.jpg"
Player2MGUp1 = "player2/shotgun&mg/Player2MGUp1.jpg"
Player2MGUp2 = "player2/shotgun&mg/Player2MGUp2.jpg"

#player2's class: shield
Player2ShieldDownRest = "player2/shield/Player2ShieldDownRest.jpg"
Player2ShieldDown1 = "player2/shield/Player2ShieldDown1.jpg"
Player2ShieldDown2 = "player2/shield/Player2ShieldDown2.jpg"
Player2ShieldLeftRest = "player2/shield/Player2ShieldLeftRest.jpg"
Player2ShieldLeft1 = "player2/shield/Player2ShieldLeft1.jpg"
Player2ShieldLeft2 = "player2/shield/Player2ShieldLeft2.jpg"
Player2ShieldRightRest = "player2/shield/Player2ShieldRightRest.jpg"
Player2ShieldRight1 = "player2/shield/Player2ShieldRight1.jpg"
Player2ShieldRight2 = "player2/shield/Player2ShieldRight2.jpg"
Player2ShieldUpRest = "player2/shield/Player2ShieldUpRest.jpg"
Player2ShieldUp1 = "player2/shield/Player2ShieldUp1.jpg"
Player2ShieldUp2 = "player2/shield/Player2ShieldUp2.jpg"

###sound effects
#shotgun shooting sound
shotgun_shoot = pygame.mixer.Sound("shotgun-shoot.ogg")

#machinegun shooting sound
MG_shoot = pygame.mixer.Sound("MG-shoot.ogg")

#shield blocking sound
shieldblocked = pygame.mixer.Sound("shieldblocked.ogg")

#unit dashing sound (only for shield classes)
shieldcharge = pygame.mixer.Sound("shieldcharge.ogg")

#short music for winner's ending (TA DAAA~)
won = pygame.mixer.Sound("won.ogg")

#resolution of the window
fullscreen = (800,600)
width = 800
height = 600

#program name display
window = pygame.display.set_mode(fullscreen)
pygame.display.set_caption("Window")

#measure time
clock = pygame.time.Clock()

#colours in RGB
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
light_black = (100,100,100)
light_white = (200,200,200)

#frames per second
fps = 60

###damage
#shotgun damage
shotgundmg = 20
#machinegun damage
mgdmg = 10

#function for creating text surface using font.render
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

###button functions
#msg - displaying text, inactiveColor - colour when cursor is not on the button
#activeColor - colour when cursor is on the button, action - action that will proceed by pressing
def button(msg, x, y, w, h, inactiveColor, activeColor, action=None):
    #gets mouse position
    mouse = pygame.mouse.get_pos()
    #checks if the mouse is pressed/clicked
    click = pygame.mouse.get_pressed()
    #button within the loop is True
    loop = True

    #if the mouse is on the button
    if x+100> mouse[0] > x and y + h > mouse[1]> y:
        #change the button's colour to activeColor
        pygame.draw.rect(window, activeColor, (x,y, w, h))
        #if button is clicked
        if click[0] == 1 and action != None:
            #if the button's functionality is "play"
            if action == "play":
                #break the loop and proceed
                loop = False
            #if the button's functionality is "quit"
            elif action == "quit":
                #exit game and close the program
                pygame.quit()
                quit()
    #if the mouse is not on the button
    else:
        #display button with inactiveColor
        pygame.draw.rect(window, inactiveColor, (x,y, w,h))

    #create text with a size of 20
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    #position of the text
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    #display
    window.blit(TextSurf, TextRect)

    #return True or False to stay or escape from loop
    return loop

#start of the game, function beginning() will be called to comeback here
def beginning():
    #reset
    menuloop = True
    #load music "menu.ogg"
    pygame.mixer.music.load("menu.ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    ########TITLE LOOP########
    while menuloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.fill(white)

        #create title with a size of 115
        largetext = pygame.font.Font('freesansbold.ttf',115)
        #use function to create surface and rect
        TextSurf, TextRect = text_objects("The Siege", largetext)
        #position of the title
        TextRect.center = ((width/2),(height/2))
        #display the title
        window.blit(TextSurf, TextRect)

        #create buttons
        menuloop = button("Play!", 150, 450, 100, 50, light_black, green, "play")
        button("Quit", 550, 450, 100, 50, light_black, green, "quit")

        #update displays
        pygame.display.update()

    #out of menu loop

    #resolution
    fullscreen = (800,600)
    winner = 'not determined yet'
    gameEnd = False

    #display texts ingame (number of hp, cooldown, etc)
    smallText = pygame.font.Font("freesansbold.ttf", 15)
    even_smallerText = pygame.font.Font("freesansbold.ttf", 10)

    #function for different icon display when changing the class
    def icon(players, x, y):
        #if player class is shotgun
        if players.intro_class == "class_shotgun":
            #load up shotgun icon
            shotgunicon = pygame.image.load("icon/shotgunicon.jpg")
            shotgunicon = pygame.transform.scale(shotgunicon, (60,60))
            window.blit(shotgunicon, (x, y))
        #if player class is machinegun
        if players.intro_class == "class_mg":
            #load up machinegun icon
            machinegunicon = pygame.image.load("icon/machinegunicon.jpg")
            machinegunicon = pygame.transform.scale(machinegunicon, (60,60))
            window.blit(machinegunicon, (x, y))
        #if player class is shield
        if players.intro_class == "class_shield":
            #load up shield icon
            shieldicon = pygame.image.load("icon/shieldicon.jpg")
            shieldicon = pygame.transform.scale(shieldicon, (60,60))
            window.blit(shieldicon, (x, y))
    #button function but purely for switching players (requires sprite)
    def selection(msg, x, y, w, h, ic, ac, players, action=None):
        #same stuff with button function but has player sprites
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        switching = players.intro_class
        if players.intro_delay > 0:
            players.intro_delay += 1
        if players.intro_delay >= 40:
            players.intro_delay = 0
        if x+100> mouse[0] > x and y + h > mouse[1]> y:
            pygame.draw.rect(window, ac, (x,y, w, h))
            if players.intro_delay == 0:
                #if button is clicked
                if click[0] == 1 and action != None:
                    if action == "switch":
                        #if players' class was previously shotgun,
                        if players.intro_class == "class_shotgun":
                            #switch to next class which is shield
                            switching = "class_shield"
                        #if players' class was previously shield,
                        if players.intro_class == "class_shield":
                            #switch to next class which is machinegun
                            switching = "class_mg"
                        #if players' class was previously machinegun,
                        if players.intro_class == "class_mg":
                            #switch BACK to shotgun, this will loop around for an option
                            switching = "class_shotgun"
                        players.intro_class = switching
                    #delay is only for preventing mouse hold changing the option rapidly
                    players.intro_delay += 1
        #if mouse is not on the button
        else:
            #create a normal button
            pygame.draw.rect(window, ic, (x,y, w,h))

        #message display on the button
        smallText = pygame.font.Font("freesansbold.ttf", 10)
        TextSurf, TextRect = text_objects(msg, smallText)
        TextRect.center = ((x+(w/2)), (y+(h/2)))
        window.blit(TextSurf, TextRect)
    #another button function for normal use, works the same as previous one
    def button_secondary(msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        loop = True
        if x+100> mouse[0] > x and y + h > mouse[1]> y:
            pygame.draw.rect(window, ac, (x,y, w, h))
            if click[0] == 1 and action != None:
                if action == "play":
                    loop = False

                elif action == "quit":
                    #goes back to beginning (menu)
                    beginning()
        else:
            pygame.draw.rect(window, ic, (x,y, w,h))

        smallText = pygame.font.Font("freesansbold.ttf", 10)
        TextSurf, TextRect = text_objects(msg, smallText)
        TextRect.center = ((x+(w/2)), (y+(h/2)))
        window.blit(TextSurf, TextRect)
        return loop

    #create 5 player1 unit
    player1 = pygame.sprite.Sprite()
    player1.p = 1
    player1a = pygame.sprite.Sprite()
    player1a.p = 1
    player1b = pygame.sprite.Sprite()
    player1b.p = 1
    player1c = pygame.sprite.Sprite()
    player1c.p = 1
    player1d = pygame.sprite.Sprite()
    player1d.p = 1
    #create 5 player2 unit
    player2 = pygame.sprite.Sprite()
    player2.p = 2
    player2a = pygame.sprite.Sprite()
    player2a.p = 2
    player2b = pygame.sprite.Sprite()
    player2b.p = 2
    player2c = pygame.sprite.Sprite()
    player2c.p = 2
    player2d = pygame.sprite.Sprite()
    player2d.p = 2

    #add all player sprites into group to update them at once
    allplayerlist = pygame.sprite.Group()
    allplayerlist.add(player1)
    allplayerlist.add(player1a)
    allplayerlist.add(player1b)
    allplayerlist.add(player1c)
    allplayerlist.add(player1d)
    allplayerlist.add(player2)
    allplayerlist.add(player2a)
    allplayerlist.add(player2b)
    allplayerlist.add(player2c)
    allplayerlist.add(player2d)

    #give all sprites .intro_delay and .intro_class value for switching/button function
    for players in allplayerlist:
        players.intro_delay = 0
        players.intro_class = "class_shotgun"

    #########CLASS SELECTION LOOP########
    gameIntro = True
    while gameIntro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #set icons all the unit in each individual position
        window.fill(white)
        icon(player1, 150, 100)
        icon(player1a, 150, 200)
        icon(player1b, 150, 300)
        icon(player1c, 150, 400)
        icon(player1d, 150, 500)
        icon(player2, 650, 100)
        icon(player2a, 650, 200)
        icon(player2b, 650, 300)
        icon(player2c, 650, 400)
        icon(player2d, 650, 500)
        #create buttons that allows players to switch
        selection("switch", 250, 130, 50, 25, light_black, green,player1, "switch")
        selection("switch", 250, 230, 50, 25, light_black, green,player1a, "switch")
        selection("switch", 250, 330, 50, 25, light_black, green,player1b, "switch")
        selection("switch", 250, 430, 50, 25, light_black, green,player1c, "switch")
        selection("switch", 250, 530, 50, 25, light_black, green,player1d, "switch")
        selection ("switch", 550, 130, 50, 25, light_black, green,player2, "switch")
        selection("switch", 550, 230, 50, 25, light_black, green,player2a, "switch")
        selection("switch", 550, 330, 50, 25, light_black, green,player2b, "switch")
        selection("switch", 550, 430, 50, 25, light_black, green,player2c, "switch")
        selection("switch", 550, 530, 50, 25, light_black, green,player2d, "switch")

        #create title text using text function
        largetext = pygame.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects("Choose your class", largetext)
        TextRect.center = ((400,30))
        window.blit(TextSurf, TextRect)

        #create normal buttons that will allow players to proceed
        #button to start the game
        gameIntro = button_secondary("Play!", 400,300, 30,30, light_white, green, "play")
        #button to go back to the menu
        button_secondary("Back to Menu", 375,350, 80,30, light_white, green, "quit")
        pygame.display.update()

    #cooldown/reloadspeed (change for balanced gaming)
    shotgundelay = 50
    machinegundelay = 8
    shielddelay = 100

    #damage
    shotgundmg = 10
    mgdmg = 5

    #shield dashspeed
    shield_dashspeed = 50

    ###sprites
    #machinegun
    classMachinegun = pygame.sprite.Sprite
    def classMachinegun_initial(classMachinegun, x, y, number):
        pygame.sprite.Sprite.__init__(classMachinegun)
        classMachinegun.classname = "classMachinegun"  #class identification for updates
        classMachinegun.x = x
        classMachinegun.y = y
        classMachinegun.w = 25
        classMachinegun.h = 25
        classMachinegun.hp = 50
        classMachinegun.alive = True
        classMachinegun.number = number
        classMachinegun.rect = pygame.Rect(classMachinegun.x, classMachinegun.y, classMachinegun.w, classMachinegun.h )

        classMachinegun.delay = 0

        #vertical images
        if classMachinegun.p == 1:
            classMachinegun.Player1MGDownRest = pygame.image.load(Player1MGDownRest)
            classMachinegun.Player1MGDownRest = pygame.transform.scale(classMachinegun.Player1MGDownRest, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGDown1 = pygame.image.load(Player1MGDown1)
            classMachinegun.Player1MGDown1 = pygame.transform.scale(classMachinegun.Player1MGDown1, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGDown2 = pygame.image.load(Player1MGDown2)
            classMachinegun.Player1MGDown2 = pygame.transform.scale(classMachinegun.Player1MGDown2, (classMachinegun.w,classMachinegun.h))

            classMachinegun.Player1MGLeftRest = pygame.image.load(Player1MGLeftRest)
            classMachinegun.Player1MGLeftRest = pygame.transform.scale(classMachinegun.Player1MGLeftRest, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGLeft1 = pygame.image.load(Player1MGLeft1)
            classMachinegun.Player1MGLeft1 = pygame.transform.scale(classMachinegun.Player1MGLeft1, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGLeft2 = pygame.image.load(Player1MGLeft2)
            classMachinegun.Player1MGLeft2 = pygame.transform.scale(classMachinegun.Player1MGLeft2, (classMachinegun.w,classMachinegun.h))

            classMachinegun.Player1MGRightRest = pygame.image.load(Player1MGRightRest)
            classMachinegun.Player1MGRightRest = pygame.transform.scale(classMachinegun.Player1MGRightRest, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGRight1 = pygame.image.load(Player1MGRight1)
            classMachinegun.Player1MGRight1 = pygame.transform.scale(classMachinegun.Player1MGRight1, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGRight2 = pygame.image.load(Player1MGRight2)
            classMachinegun.Player1MGRight2 = pygame.transform.scale(classMachinegun.Player1MGRight2, (classMachinegun.w,classMachinegun.h))

            classMachinegun.Player1MGUpRest = pygame.image.load(Player1MGUpRest)
            classMachinegun.Player1MGUpRest = pygame.transform.scale(classMachinegun.Player1MGUpRest, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGUp1 = pygame.image.load(Player1MGUp1)
            classMachinegun.Player1MGUp1 = pygame.transform.scale(classMachinegun.Player1MGUp1, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGUp2 = pygame.image.load(Player1MGUp2)
            classMachinegun.Player1MGUp2 = pygame.transform.scale(classMachinegun.Player1MGUp2, (classMachinegun.w,classMachinegun.h))

        elif classMachinegun.p == 2:
            classMachinegun.Player1MGDownRest = pygame.image.load(Player2MGDownRest)
            classMachinegun.Player1MGDownRest = pygame.transform.scale(classMachinegun.Player1MGDownRest, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGDown1 = pygame.image.load(Player2MGDown1)
            classMachinegun.Player1MGDown1 = pygame.transform.scale(classMachinegun.Player1MGDown1, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGDown2 = pygame.image.load(Player2MGDown2)
            classMachinegun.Player1MGDown2 = pygame.transform.scale(classMachinegun.Player1MGDown2, (classMachinegun.w,classMachinegun.h))

            classMachinegun.Player1MGLeftRest = pygame.image.load(Player2MGLeftRest)
            classMachinegun.Player1MGLeftRest = pygame.transform.scale(classMachinegun.Player1MGLeftRest, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGLeft1 = pygame.image.load(Player2MGLeft1)
            classMachinegun.Player1MGLeft1 = pygame.transform.scale(classMachinegun.Player1MGLeft1, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGLeft2 = pygame.image.load(Player2MGLeft2)
            classMachinegun.Player1MGLeft2 = pygame.transform.scale(classMachinegun.Player1MGLeft2, (classMachinegun.w,classMachinegun.h))

            classMachinegun.Player1MGRightRest = pygame.image.load(Player2MGRightRest)
            classMachinegun.Player1MGRightRest = pygame.transform.scale(classMachinegun.Player1MGRightRest, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGRight1 = pygame.image.load(Player2MGRight1)
            classMachinegun.Player1MGRight1 = pygame.transform.scale(classMachinegun.Player1MGRight1, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGRight2 = pygame.image.load(Player2MGRight2)
            classMachinegun.Player1MGRight2 = pygame.transform.scale(classMachinegun.Player1MGRight2, (classMachinegun.w,classMachinegun.h))

            classMachinegun.Player1MGUpRest = pygame.image.load(Player2MGUpRest)
            classMachinegun.Player1MGUpRest = pygame.transform.scale(classMachinegun.Player1MGUpRest, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGUp1 = pygame.image.load(Player2MGUp1)
            classMachinegun.Player1MGUp1 = pygame.transform.scale(classMachinegun.Player1MGUp1, (classMachinegun.w,classMachinegun.h))
            classMachinegun.Player1MGUp2 = pygame.image.load(Player2MGUp2)
            classMachinegun.Player1MGUp2 = pygame.transform.scale(classMachinegun.Player1MGUp2, (classMachinegun.w,classMachinegun.h))

        #the speed of the animation
        classMachinegun.timeTarget = 10
        classMachinegun.timeNum = 0
        classMachinegun.currentImage = 0

        classMachinegun.direction = "Down"
        classMachinegun.stats = "Idle"
    def classMachinegun_update(classMachinegun):
        if classMachinegun.delay > 0:
            classMachinegun.delay += 1
            #delay timing for bullet
            if classMachinegun.delay >= 8:
                classMachinegun.delay = 0
        classMachinegun.timeNum += 1
        if classMachinegun.timeNum == classMachinegun.timeTarget:
            if classMachinegun.currentImage ==  0:
                classMachinegun.currentImage += 1
            if classMachinegun.currentImage == 1:
                classMachinegun.currentImage += 1
            else:
                classMachinegun.currentImage = 0

            classMachinegun.timeNum = 0

        classMachinegun.rect = pygame.Rect(classMachinegun.x, classMachinegun.y, classMachinegun.w, classMachinegun.h)
        classMachinegun_imageupdate(classMachinegun)
    def classMachinegun_imageupdate(classMachinegun):
            if classMachinegun.direction == "Down":
                if classMachinegun.stats == "Idle":
                    #change the 'green' into color variable for different colors in hp ratio
                    window.blit(classMachinegun.Player1MGDownRest, (classMachinegun.x, classMachinegun.y))
                else:
                    if classMachinegun.currentImage == 0:
                        window.blit(classMachinegun.Player1MGDown1, (classMachinegun.x, classMachinegun.y))
                    if classMachinegun.currentImage == 1:
                        window.blit(classMachinegun.Player1MGDownRest, (classMachinegun.x, classMachinegun.y))
                    if classMachinegun.currentImage == 2:
                        window.blit(classMachinegun.Player1MGDown2, (classMachinegun.x, classMachinegun.y))

            if classMachinegun.direction == "Up":
                if classMachinegun.stats == "Idle":
                    window.blit(classMachinegun.Player1MGUpRest, (classMachinegun.x, classMachinegun.y))
                else:
                    if classMachinegun.currentImage == 0:
                        window.blit(classMachinegun.Player1MGUp1, (classMachinegun.x, classMachinegun.y))
                    if classMachinegun.currentImage == 1:
                        window.blit(classMachinegun.Player1MGUpRest, (classMachinegun.x, classMachinegun.y))
                    if classMachinegun.currentImage == 2:
                        window.blit(classMachinegun.Player1MGUp2, (classMachinegun.x, classMachinegun.y))

            if classMachinegun.direction == "Right":
                if classMachinegun.stats == "Idle":
                    window.blit(classMachinegun.Player1MGRightRest, (classMachinegun.x, classMachinegun.y))
                else:
                    if classMachinegun.currentImage == 0:
                        window.blit(classMachinegun.Player1MGRight1, (classMachinegun.x, classMachinegun.y))
                    if classMachinegun.currentImage == 1:
                        window.blit(classMachinegun.Player1MGRightRest, (classMachinegun.x, classMachinegun.y))
                    if classMachinegun.currentImage == 2:
                        window.blit(classMachinegun.Player1MGRight2, (classMachinegun.x, classMachinegun.y))

            if classMachinegun.direction == "Left":
                if classMachinegun.stats == "Idle":
                    window.blit(classMachinegun.Player1MGLeftRest, (classMachinegun.x, classMachinegun.y))
                else:
                    if classMachinegun.currentImage == 0:
                        window.blit(classMachinegun.Player1MGLeft1, (classMachinegun.x, classMachinegun.y))
                    if classMachinegun.currentImage == 1:
                        window.blit(classMachinegun.Player1MGLeftRest, (classMachinegun.x, classMachinegun.y))
                    if classMachinegun.currentImage == 2:
                        window.blit(classMachinegun.Player1MGLeft2, (classMachinegun.x, classMachinegun.y))

            pygame.draw.rect(window, green, (classMachinegun.x-10, classMachinegun.y-20, classMachinegun.hp,10))
            TextSurf, TextRect = text_objects(classMachinegun.number, smallText)
            TextRect.center = (classMachinegun.x-20, classMachinegun.y-15)
            window.blit(TextSurf, TextRect)
            hpSurf, hpRect = text_objects(str(classMachinegun.hp), even_smallerText)
            hpRect.center = (classMachinegun.x+15, classMachinegun.y-15)
            window.blit(hpSurf, hpRect)

    #shotgun
    classShotgun = pygame.sprite.Sprite
    def classShotgun_initial(classShotgun, x, y, number):
        pygame.sprite.Sprite.__init__(classShotgun)
        classShotgun.classname = "classShotgun"
        classShotgun.x = x
        classShotgun.y = y
        classShotgun.w = 25
        classShotgun.h = 25
        classShotgun.hp = 50
        classShotgun.alive = True
        classShotgun.number = number
        classShotgun.rect = pygame.Rect(classShotgun.x, classShotgun.y, classShotgun.w, classShotgun.h )

        classShotgun.delay = 0

        if classShotgun.p == 1:
            classShotgun.Player1MGDownRest = pygame.image.load(Player1MGDownRest)
            classShotgun.Player1MGDownRest = pygame.transform.scale(classShotgun.Player1MGDownRest, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGDown1 = pygame.image.load(Player1MGDown1)
            classShotgun.Player1MGDown1 = pygame.transform.scale(classShotgun.Player1MGDown1, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGDown2 = pygame.image.load(Player1MGDown2)
            classShotgun.Player1MGDown2 = pygame.transform.scale(classShotgun.Player1MGDown2, (classShotgun.w,classShotgun.h))

            classShotgun.Player1MGLeftRest = pygame.image.load(Player1MGLeftRest)
            classShotgun.Player1MGLeftRest = pygame.transform.scale(classShotgun.Player1MGLeftRest, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGLeft1 = pygame.image.load(Player1MGLeft1)
            classShotgun.Player1MGLeft1 = pygame.transform.scale(classShotgun.Player1MGLeft1, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGLeft2 = pygame.image.load(Player1MGLeft2)
            classShotgun.Player1MGLeft2 = pygame.transform.scale(classShotgun.Player1MGLeft2, (classShotgun.w,classShotgun.h))

            classShotgun.Player1MGRightRest = pygame.image.load(Player1MGRightRest)
            classShotgun.Player1MGRightRest = pygame.transform.scale(classShotgun.Player1MGRightRest, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGRight1 = pygame.image.load(Player1MGRight1)
            classShotgun.Player1MGRight1 = pygame.transform.scale(classShotgun.Player1MGRight1, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGRight2 = pygame.image.load(Player1MGRight2)
            classShotgun.Player1MGRight2 = pygame.transform.scale(classShotgun.Player1MGRight2, (classShotgun.w,classShotgun.h))

            classShotgun.Player1MGUpRest = pygame.image.load(Player1MGUpRest)
            classShotgun.Player1MGUpRest = pygame.transform.scale(classShotgun.Player1MGUpRest, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGUp1 = pygame.image.load(Player1MGUp1)
            classShotgun.Player1MGUp1 = pygame.transform.scale(classShotgun.Player1MGUp1, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGUp2 = pygame.image.load(Player1MGUp2)
            classShotgun.Player1MGUp2 = pygame.transform.scale(classShotgun.Player1MGUp2, (classShotgun.w,classShotgun.h))

        elif classShotgun.p == 2:
            classShotgun.Player1MGDownRest = pygame.image.load(Player2MGDownRest)
            classShotgun.Player1MGDownRest = pygame.transform.scale(classShotgun.Player1MGDownRest, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGDown1 = pygame.image.load(Player2MGDown1)
            classShotgun.Player1MGDown1 = pygame.transform.scale(classShotgun.Player1MGDown1, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGDown2 = pygame.image.load(Player2MGDown2)
            classShotgun.Player1MGDown2 = pygame.transform.scale(classShotgun.Player1MGDown2, (classShotgun.w,classShotgun.h))

            classShotgun.Player1MGLeftRest = pygame.image.load(Player2MGLeftRest)
            classShotgun.Player1MGLeftRest = pygame.transform.scale(classShotgun.Player1MGLeftRest, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGLeft1 = pygame.image.load(Player2MGLeft1)
            classShotgun.Player1MGLeft1 = pygame.transform.scale(classShotgun.Player1MGLeft1, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGLeft2 = pygame.image.load(Player2MGLeft2)
            classShotgun.Player1MGLeft2 = pygame.transform.scale(classShotgun.Player1MGLeft2, (classShotgun.w,classShotgun.h))

            classShotgun.Player1MGRightRest = pygame.image.load(Player2MGRightRest)
            classShotgun.Player1MGRightRest = pygame.transform.scale(classShotgun.Player1MGRightRest, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGRight1 = pygame.image.load(Player2MGRight1)
            classShotgun.Player1MGRight1 = pygame.transform.scale(classShotgun.Player1MGRight1, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGRight2 = pygame.image.load(Player2MGRight2)
            classShotgun.Player1MGRight2 = pygame.transform.scale(classShotgun.Player1MGRight2, (classShotgun.w,classShotgun.h))

            classShotgun.Player1MGUpRest = pygame.image.load(Player2MGUpRest)
            classShotgun.Player1MGUpRest = pygame.transform.scale(classShotgun.Player1MGUpRest, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGUp1 = pygame.image.load(Player2MGUp1)
            classShotgun.Player1MGUp1 = pygame.transform.scale(classShotgun.Player1MGUp1, (classShotgun.w,classShotgun.h))
            classShotgun.Player1MGUp2 = pygame.image.load(Player2MGUp2)
            classShotgun.Player1MGUp2 = pygame.transform.scale(classShotgun.Player1MGUp2, (classShotgun.w,classShotgun.h))

        #the speed of the animation
        classShotgun.timeTarget = 10
        classShotgun.timeNum = 0
        classShotgun.currentImage = 0

        classShotgun.direction = "Down"
        classShotgun.stats = "Idle"
    def classShotgun_update(classShotgun):
        if classShotgun.delay > 0:
            classShotgun.delay += 1
            if classShotgun.delay >= shotgundelay:
                classShotgun.delay = 0

        classShotgun.timeNum += 1
        if classShotgun.timeNum == classShotgun.timeTarget:

            if classShotgun.currentImage ==  0:
                classShotgun.currentImage += 1
            if classShotgun.currentImage == 1:
                classShotgun.currentImage += 1
            else:
                classShotgun.currentImage = 0

            classShotgun.timeNum = 0

        classShotgun.rect = pygame.Rect(classShotgun.x, classShotgun.y, classShotgun.w, classShotgun.h)
        classShotgun_imageupdate(classShotgun)
    def classShotgun_imageupdate(classShotgun):
        if classShotgun.direction == "Down":
            if classShotgun.stats == "Idle":
                #change the 'green' into color variable for different colors in hp ratio
                window.blit(classShotgun.Player1MGDownRest, (classShotgun.x, classShotgun.y))
            else:
                if classShotgun.currentImage == 0:
                    window.blit(classShotgun.Player1MGDown1, (classShotgun.x, classShotgun.y))
                if classShotgun.currentImage == 1:
                    window.blit(classShotgun.Player1MGDownRest, (classShotgun.x, classShotgun.y))
                if classShotgun.currentImage == 2:
                    window.blit(classShotgun.Player1MGDown2, (classShotgun.x, classShotgun.y))

        if classShotgun.direction == "Up":
            if classShotgun.stats == "Idle":
                window.blit(classShotgun.Player1MGUpRest, (classShotgun.x, classShotgun.y))
            else:
                if classShotgun.currentImage == 0:
                    window.blit(classShotgun.Player1MGUp1, (classShotgun.x, classShotgun.y))
                if classShotgun.currentImage == 1:
                    window.blit(classShotgun.Player1MGUpRest, (classShotgun.x, classShotgun.y))
                if classShotgun.currentImage == 2:
                    window.blit(classShotgun.Player1MGUp2, (classShotgun.x, classShotgun.y))

        if classShotgun.direction == "Right":
            if classShotgun.stats == "Idle":
                window.blit(classShotgun.Player1MGRightRest, (classShotgun.x, classShotgun.y))
            else:
                if classShotgun.currentImage == 0:
                    window.blit(classShotgun.Player1MGRight1, (classShotgun.x, classShotgun.y))
                if classShotgun.currentImage == 1:
                    window.blit(classShotgun.Player1MGRightRest, (classShotgun.x, classShotgun.y))
                if classShotgun.currentImage == 2:
                    window.blit(classShotgun.Player1MGRight2, (classShotgun.x, classShotgun.y))

        if classShotgun.direction == "Left":
            if classShotgun.stats == "Idle":
                window.blit(classShotgun.Player1MGLeftRest, (classShotgun.x, classShotgun.y))
            else:
                if classShotgun.currentImage == 0:
                    window.blit(classShotgun.Player1MGLeft1, (classShotgun.x, classShotgun.y))
                if classShotgun.currentImage == 1:
                    window.blit(classShotgun.Player1MGLeftRest, (classShotgun.x, classShotgun.y))
                if classShotgun.currentImage == 2:
                    window.blit(classShotgun.Player1MGLeft2, (classShotgun.x, classShotgun.y))

        #hp bar
        pygame.draw.rect(window, green, (classShotgun.x-10, classShotgun.y-20, classShotgun.hp,10))

        #player's number/letter which will be pressed to switch
        TextSurf, TextRect = text_objects(classShotgun.number, smallText)
        TextRect.center = (classShotgun.x-20, classShotgun.y-15)
        window.blit(TextSurf, TextRect)

        #number of hp
        hpSurf, hpRect = text_objects(str(classShotgun.hp), even_smallerText)
        hpRect.center = (classShotgun.x+15, classShotgun.y-15)
        window.blit(hpSurf, hpRect)

        #reload delay
        delaySurf, delayRect = text_objects(str(classShotgun.delay), even_smallerText)
        delayRect.center = (classShotgun.x+45, classShotgun.y-15)
        window.blit(delaySurf, delayRect)

    #shield
    classShield = pygame.sprite.Sprite
    def classShield_initial(classShield, x, y, number):
        pygame.sprite.Sprite.__init__(classShield)
        classShield.classname = "classShield"
        classShield.x = x
        classShield.y = y
        classShield.w = 25
        classShield.h = 25
        classShield.hp = 50
        classShield.alive = True
        classShield.number = number
        classShield.rect = pygame.Rect(classShield.x, classShield.y, classShield.w, classShield.h )

        classShield.delay = 0

        if classShield.p == 1:
        #vertical images
            classShield.Player1ShieldDownRest = pygame.image.load(Player1ShieldDownRest)
            classShield.Player1ShieldDownRest = pygame.transform.scale(classShield.Player1ShieldDownRest, (classShield.w,classShield.h))
            classShield.Player1ShieldDown1 = pygame.image.load(Player1ShieldDown1)
            classShield.Player1ShieldDown1 = pygame.transform.scale(classShield.Player1ShieldDown1, (classShield.w,classShield.h))
            classShield.Player1ShieldDown2 = pygame.image.load(Player1ShieldDown2)
            classShield.Player1ShieldDown2 = pygame.transform.scale(classShield.Player1ShieldDown2, (classShield.w,classShield.h))

            classShield.Player1ShieldLeftRest = pygame.image.load(Player1ShieldLeftRest)
            classShield.Player1ShieldLeftRest = pygame.transform.scale(classShield.Player1ShieldLeftRest, (classShield.w,classShield.h))
            classShield.Player1ShieldLeft1 = pygame.image.load(Player1ShieldLeft1)
            classShield.Player1ShieldLeft1 = pygame.transform.scale(classShield.Player1ShieldLeft1, (classShield.w,classShield.h))
            classShield.Player1ShieldLeft2 = pygame.image.load(Player1ShieldLeft2)
            classShield.Player1ShieldLeft2 = pygame.transform.scale(classShield.Player1ShieldLeft2, (classShield.w,classShield.h))

            classShield.Player1ShieldRightRest = pygame.image.load(Player1ShieldRightRest)
            classShield.Player1ShieldRightRest = pygame.transform.scale(classShield.Player1ShieldRightRest, (classShield.w,classShield.h))
            classShield.Player1ShieldRight1 = pygame.image.load(Player1ShieldRight1)
            classShield.Player1ShieldRight1 = pygame.transform.scale(classShield.Player1ShieldRight1, (classShield.w,classShield.h))
            classShield.Player1ShieldRight2 = pygame.image.load(Player1ShieldRight2)
            classShield.Player1ShieldRight2 = pygame.transform.scale(classShield.Player1ShieldRight2, (classShield.w,classShield.h))

            classShield.Player1ShieldUpRest = pygame.image.load(Player1ShieldUpRest)
            classShield.Player1ShieldUpRest = pygame.transform.scale(classShield.Player1ShieldUpRest, (classShield.w,classShield.h))
            classShield.Player1ShieldUp1 = pygame.image.load(Player1ShieldUp1)
            classShield.Player1ShieldUp1 = pygame.transform.scale(classShield.Player1ShieldUp1, (classShield.w,classShield.h))
            classShield.Player1ShieldUp2 = pygame.image.load(Player1ShieldUp2)
            classShield.Player1ShieldUp2 = pygame.transform.scale(classShield.Player1ShieldUp2, (classShield.w,classShield.h))

        elif classShield.p == 2:
            classShield.Player1ShieldDownRest = pygame.image.load(Player2ShieldDownRest)
            classShield.Player1ShieldDownRest = pygame.transform.scale(classShield.Player1ShieldDownRest, (classShield.w,classShield.h))
            classShield.Player1ShieldDown1 = pygame.image.load(Player2ShieldDown1)
            classShield.Player1ShieldDown1 = pygame.transform.scale(classShield.Player1ShieldDown1, (classShield.w,classShield.h))
            classShield.Player1ShieldDown2 = pygame.image.load(Player2ShieldDown2)
            classShield.Player1ShieldDown2 = pygame.transform.scale(classShield.Player1ShieldDown2, (classShield.w,classShield.h))

            classShield.Player1ShieldLeftRest = pygame.image.load(Player2ShieldLeftRest)
            classShield.Player1ShieldLeftRest = pygame.transform.scale(classShield.Player1ShieldLeftRest, (classShield.w,classShield.h))
            classShield.Player1ShieldLeft1 = pygame.image.load(Player2ShieldLeft1)
            classShield.Player1ShieldLeft1 = pygame.transform.scale(classShield.Player1ShieldLeft1, (classShield.w,classShield.h))
            classShield.Player1ShieldLeft2 = pygame.image.load(Player2ShieldLeft2)
            classShield.Player1ShieldLeft2 = pygame.transform.scale(classShield.Player1ShieldLeft2, (classShield.w,classShield.h))

            classShield.Player1ShieldRightRest = pygame.image.load(Player2ShieldRightRest)
            classShield.Player1ShieldRightRest = pygame.transform.scale(classShield.Player1ShieldRightRest, (classShield.w,classShield.h))
            classShield.Player1ShieldRight1 = pygame.image.load(Player2ShieldRight1)
            classShield.Player1ShieldRight1 = pygame.transform.scale(classShield.Player1ShieldRight1, (classShield.w,classShield.h))
            classShield.Player1ShieldRight2 = pygame.image.load(Player2ShieldRight2)
            classShield.Player1ShieldRight2 = pygame.transform.scale(classShield.Player1ShieldRight2, (classShield.w,classShield.h))

            classShield.Player1ShieldUpRest = pygame.image.load(Player2ShieldUpRest)
            classShield.Player1ShieldUpRest = pygame.transform.scale(classShield.Player1ShieldUpRest, (classShield.w,classShield.h))
            classShield.Player1ShieldUp1 = pygame.image.load(Player2ShieldUp1)
            classShield.Player1ShieldUp1 = pygame.transform.scale(classShield.Player1ShieldUp1, (classShield.w,classShield.h))
            classShield.Player1ShieldUp2 = pygame.image.load(Player2ShieldUp2)
            classShield.Player1ShieldUp2 = pygame.transform.scale(classShield.Player1ShieldUp2, (classShield.w,classShield.h))

        #the speed of the animation
        classShield.timeTarget = 10
        classShield.timeNum = 0
        classShield.currentImage = 0

        classShield.direction = "Down"
        classShield.stats = "Idle"
    def classShield_update(classShield):
        #delete if not used
        if classShield.delay > 0:
            classShield.delay += 1
            if classShield.delay >= shielddelay:
                classShield.delay = 0

        classShield.timeNum += 1
        if classShield.timeNum == classShield.timeTarget:

            if classShield.currentImage ==  0:
                classShield.currentImage += 1
            if classShield.currentImage == 1:
                classShield.currentImage += 1
            else:
                classShield.currentImage = 0

            classShield.timeNum = 0

        classShield.rect = pygame.Rect(classShield.x, classShield.y, classShield.w, classShield.h)
        classShield_imageupdate(classShield)
    def classShield_imageupdate(classShield):
        if classShield.direction == "Down":
            if classShield.stats == "Idle":
                #change the 'green' into color variable for different colors in hp ratio
                window.blit(classShield.Player1ShieldDownRest, (classShield.x, classShield.y))
            else:
                if classShield.currentImage == 0:
                    window.blit(classShield.Player1ShieldDown1, (classShield.x, classShield.y))
                if classShield.currentImage == 1:
                    window.blit(classShield.Player1ShieldDownRest, (classShield.x, classShield.y))
                if classShield.currentImage == 2:
                    window.blit(classShield.Player1ShieldDown2, (classShield.x, classShield.y))

        if classShield.direction == "Up":
            if classShield.stats == "Idle":
                window.blit(classShield.Player1ShieldUpRest, (classShield.x, classShield.y))
            else:
                if classShield.currentImage == 0:
                    window.blit(classShield.Player1ShieldUp1, (classShield.x, classShield.y))
                if classShield.currentImage == 1:
                    window.blit(classShield.Player1ShieldUpRest, (classShield.x, classShield.y))
                if classShield.currentImage == 2:
                    window.blit(classShield.Player1ShieldUp2, (classShield.x, classShield.y))

        if classShield.direction == "Right":
            if classShield.stats == "Idle":
                window.blit(classShield.Player1ShieldRightRest, (classShield.x, classShield.y))
            else:
                if classShield.currentImage == 0:
                    window.blit(classShield.Player1ShieldRight1, (classShield.x, classShield.y))
                if classShield.currentImage == 1:
                    window.blit(classShield.Player1ShieldRightRest, (classShield.x, classShield.y))
                if classShield.currentImage == 2:
                    window.blit(classShield.Player1ShieldRight2, (classShield.x, classShield.y))

        if classShield.direction == "Left":
            if classShield.stats == "Idle":
                window.blit(classShield.Player1ShieldLeftRest, (classShield.x, classShield.y))
            else:
                if classShield.currentImage == 0:
                    window.blit(classShield.Player1ShieldLeft1, (classShield.x, classShield.y))
                if classShield.currentImage == 1:
                    window.blit(classShield.Player1ShieldLeftRest, (classShield.x, classShield.y))
                if classShield.currentImage == 2:
                    window.blit(classShield.Player1ShieldLeft2, (classShield.x, classShield.y))

        #displays
        #hp bar
        pygame.draw.rect(window, green, (classShield.x-10, classShield.y-20, classShield.hp,10))

        #player's control(letter/number) to switch
        TextSurf, TextRect = text_objects(classShield.number, smallText)
        TextRect.center = (classShield.x-20, classShield.y-15)
        window.blit(TextSurf, TextRect)

        # number of hp
        hpSurf, hpRect = text_objects(str(classShield.hp), even_smallerText)
        hpRect.center = (classShield.x+15, classShield.y-15)
        window.blit(hpSurf, hpRect)

        # number of delay
        delaySurf, delayRect = text_objects(str(classShield.delay), even_smallerText)
        delayRect.center = (classShield.x+45, classShield.y-15)
        window.blit(delaySurf, delayRect)

    #bullets
    DefaultBullet = pygame.sprite.Sprite
    def DefaultBullet_initial(DefaultBullet, classes):
        DefaultBullet.type = "default"
        DefaultBullet.direction = classes.direction

        DefaultBullet.x = classes.x
        DefaultBullet.y = classes.y
        DefaultBullet.w = 5
        DefaultBullet.h = 5

        #barrel position
        if DefaultBullet.direction == "Down":
            DefaultBullet.x += 9
            DefaultBullet.y += 32
            DefaultBullet.opp_direction = "Up"
        if DefaultBullet.direction == "Up":
            DefaultBullet.x += 23
            DefaultBullet.opp_direction = "Down"
        if DefaultBullet.direction == "Right":
            DefaultBullet.x += 32
            DefaultBullet.y += 23
            DefaultBullet.opp_direction = "Left"
        if DefaultBullet.direction == "Left":
            DefaultBullet.y += 9
            DefaultBullet.opp_direction = "Right"
        DefaultBullet.image = pygame.Surface((5,5))

        DefaultBullet.rect = pygame.Rect(DefaultBullet.x, DefaultBullet.y, DefaultBullet.w, DefaultBullet.h)
    def DefaultBullet_update(DefaultBullet):
        if DefaultBullet.direction == "Down":
            DefaultBullet.y += 15
        if DefaultBullet.direction == "Up":
            DefaultBullet.y -= 15
        if DefaultBullet.direction == "Right":
            DefaultBullet.x += 15
        if DefaultBullet.direction == "Left":
            DefaultBullet.x -= 15


        DefaultBullet.rect = pygame.Rect(DefaultBullet.x, DefaultBullet.y, DefaultBullet.w, DefaultBullet.h)
        window.blit(DefaultBullet.image, (DefaultBullet.x, DefaultBullet.y))

    #shotgunbullets
    ShotgunBullet = pygame.sprite.Sprite
    def ShotgunBullet_initial(ShotgunBullet, classes, forward, spread):
        ShotgunBullet.type = "shotgun"
        ShotgunBullet.direction = classes.direction

        ShotgunBullet.forward = forward
        ShotgunBullet.spread = spread
        ShotgunBullet.x = classes.x
        ShotgunBullet.y = classes.y
        ShotgunBullet.w = 3
        ShotgunBullet.h = 3

        if ShotgunBullet.direction == "Down":
            ShotgunBullet.x += 9
            ShotgunBullet.y += 32
            ShotgunBullet.opp_direction = "Up"
        if ShotgunBullet.direction == "Up":
            ShotgunBullet.x += 23
            ShotgunBullet.opp_direction = "Down"
        if ShotgunBullet.direction == "Right":
            ShotgunBullet.x += 32
            ShotgunBullet.y += 23
            ShotgunBullet.opp_direction = "Left"
        if ShotgunBullet.direction == "Left":
            ShotgunBullet.y += 9
            ShotgunBullet.opp_direction = "Right"
        ShotgunBullet.image = pygame.Surface((3,3))

        ShotgunBullet.rect = pygame.Rect(ShotgunBullet.x, ShotgunBullet.y, ShotgunBullet.w, ShotgunBullet.h)
    def ShotgunBullet_update(ShotgunBullet):
        if ShotgunBullet.direction == "Down":
            ShotgunBullet.y += ShotgunBullet.forward
            ShotgunBullet.x += ShotgunBullet.spread
        if ShotgunBullet.direction == "Up":
            ShotgunBullet.y -= ShotgunBullet.forward
            ShotgunBullet.x += ShotgunBullet.spread
        if ShotgunBullet.direction == "Right":
            ShotgunBullet.x += ShotgunBullet.forward
            ShotgunBullet.y += ShotgunBullet.spread
        if ShotgunBullet.direction == "Left":
            ShotgunBullet.x -= ShotgunBullet.forward
            ShotgunBullet.y += ShotgunBullet.spread

        ShotgunBullet.rect = pygame.Rect(ShotgunBullet.x, ShotgunBullet.y, ShotgunBullet.w, ShotgunBullet.h)
        window.blit(ShotgunBullet.image, (ShotgunBullet.x, ShotgunBullet.y))

    #walls
    wall = pygame.sprite.Sprite
    def wall_initial(wall, x, y, width, height):
        wall.x = x
        wall.y = y
        wall.width = width
        wall.height = height
        wall.rect = pygame.Rect(wall.x, wall.y, wall.width, wall.height)
    def wall_update(wall):
        pygame.draw.rect(window,  black, (wall.x, wall.y, wall.width, wall.height))

    #data inside dictionary, can be used to change 'em
    #list in side the dictionary, thats two lol
    # Control&Position -> {player : [control, x, y]}
    ControlNPos = {player1:[1,150,100],
                   player1a:[2,150,200],
                   player1b:[3,150,300],
                   player1c:[4,150,400],
                   player1d:[5,150,500],
                   player2:['j',650,100],
                   player2a:['k',650,200],
                   player2b:['l',650,300],
                   player2c:[';',650,400],
                   player2d:["'",650,500]}

    for players in allplayerlist:
        x = int(ControlNPos[players][1])
        y = int(ControlNPos[players][2])
        control = str(ControlNPos[players][0])
        if players.intro_class == "class_shotgun":
            classShotgun_initial(players, x, y, control)
        if players.intro_class == "class_mg":
            classMachinegun_initial(players, x, y, control)
        if players.intro_class == "class_shield":
            classShield_initial(players, x, y, control)

    activeUnit1 = player1
    activeUnit2 = player2


    screenwidth = 800
    screenheight = 600
    line_width = 10

    #create wall
    topwall = pygame.sprite.Sprite()
    wall_initial(topwall, 0,0,screenwidth, line_width)
    bottomwall = pygame.sprite.Sprite()
    wall_initial(bottomwall, 0,screenheight-line_width, screenwidth, line_width)
    leftwall = pygame.sprite.Sprite()
    wall_initial(leftwall, 0,0,line_width, screenheight)
    rightwall = pygame.sprite.Sprite()
    wall_initial(rightwall, screenwidth-line_width, 0, line_width, screenheight)

    walllists = pygame.sprite.Group()
    player1bulletlists = pygame.sprite.Group()
    player2bulletlists = pygame.sprite.Group()
    allbulletlists = pygame.sprite.Group()
    player1lists = pygame.sprite.Group()
    player2lists = pygame.sprite.Group()


    player1lists.add(player1)
    player1lists.add(player1a)
    player1lists.add(player1b)
    player1lists.add(player1c)
    player1lists.add(player1d)

    player2lists.add(player2)
    player2lists.add(player2a)
    player2lists.add(player2b)
    player2lists.add(player2c)
    player2lists.add(player2d)

    walllists.add(topwall)
    walllists.add(bottomwall)
    walllists.add(leftwall)
    walllists.add(rightwall)

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                pygame.quit()
                quit()

        #exit gameloop when all player1 or 2s unit is dead
        #if all player1s are dead
        if player1.alive == False and player1a.alive == False and player1b.alive == False and player1c.alive == False\
                and player1d.alive == False:
            gameExit = True
            #winner is player2
            winner = 'Player2'
            gameEnd = True
        #if all player2s are dead
        if player2.alive == False and player2a.alive == False and player2b.alive == False and player2c.alive == False\
                and player2d.alive == False:
            gameExit = True
            #winner is player1
            winner = 'Player1'
            gameEnd = True


        for player1s in player1lists:
            #collision
            #if player1 hits on the wall
            hits_wall_1 = pygame.sprite.spritecollide(player1s, walllists, False)
            if hits_wall_1:
                #resist by moving opposite direction in equal speed
                if player1s.direction == "Left":
                    player1s.x += 3
                if player1s.direction == "Right":
                    player1s.x -= 3
                if player1s.direction == "Up":
                    player1s.y += 3
                if player1s.direction == "Down":
                    player1s.y -= 3
            #if player1s hp is 0 and lower
            if player1s.hp <= 0:
                #remove player1s from the display
                player1s.alive = False
                player1lists.remove(player1s)
        for player2s in player2lists:
            #collision
            #if player2 hits on the wall
            hits_wall_2 = pygame.sprite.spritecollide(player2s, walllists, False)
            if hits_wall_2:
                #resist by moving opposite direction in equal speed
                if player2s.direction == "Left":
                    player2s.x += 3
                if player2s.direction == "Right":
                    player2s.x -= 3
                if player2s.direction == "Up":
                    player2s.y += 3
                if player2s.direction == "Down":
                    player2s.y -= 3
            #if player2s hp is 0 and lower
            if player2s.hp <= 0:
                #remove player2s from the display
                player2s.alive = False
                player2lists.remove(player2s)

        #ALL BULLET COLLISION HERE
        for bullets in allbulletlists:
            #if the bullet hits the wall
            hits_wall_bullet = pygame.sprite.spritecollide(bullets, walllists, False)
            #remove the bullet from lists
            if hits_wall_bullet:
                if bullets.origin == "player1":
                    player1bulletlists.remove(bullets)
                    allbulletlists.remove(bullets)
                if bullets.origin == "player2":
                    player2bulletlists.remove(bullets)
                    allbulletlists.remove(bullets)

            #bullets from player1
            if bullets.origin == "player1":
                #go through all player2 units with for loop
                for player2s in player2lists:
                    if bullets.type == "default":
                        hits_player2_by_default = pygame.sprite.collide_rect(bullets, player2s)
                        if hits_player2_by_default:
                            if player2s.classname == "classShield" and player2s.direction == bullets.opp_direction:
                                pygame.mixer.Sound.play(shieldblocked)
                                player1bulletlists.remove(bullets)
                                allbulletlists.remove(bullets)
                            else:
                                player2s.hp -= mgdmg
                                player1bulletlists.remove(bullets)
                                allbulletlists.remove(bullets)
                    if bullets.type == "shotgun":
                        hits_player2_by_shotgun = pygame.sprite.collide_rect(bullets, player2s)
                        if hits_player2_by_shotgun:
                            if player2s.classname == "classShield" and player2s.direction == bullets.opp_direction:
                                pygame.mixer.Sound.play(shieldblocked)
                                player1bulletlists.remove(bullets)
                                allbulletlists.remove(bullets)
                            else:
                                player2s.hp -= shotgundmg
                                player1bulletlists.remove(bullets)
                                allbulletlists.remove(bullets)
            if bullets.origin == "player2":
                for player1s in player1lists:
                    if bullets.type == "default":
                        hits_player1_by_default = pygame.sprite.collide_rect(bullets, player1s)
                        if hits_player1_by_default:
                            if player1s.classname == "classShield" and player1s.direction == bullets.opp_direction:
                                pygame.mixer.Sound.play(shieldblocked)
                                player2bulletlists.remove(bullets)
                                allbulletlists.remove(bullets)
                            else:
                                player1s.hp -= mgdmg
                                player2bulletlists.remove(bullets)
                                allbulletlists.remove(bullets)
                    if bullets.type == "shotgun":
                        hits_player1_by_shotgun = pygame.sprite.collide_rect(bullets, player1s)
                        if hits_player1_by_shotgun:
                            if player1s.classname == "classShield" and player1s.direction == bullets.opp_direction:
                                pygame.mixer.Sound.play(shieldblocked)
                                player2bulletlists.remove(bullets)
                                allbulletlists.remove(bullets)
                            else:
                                player1s.hp -= shotgundmg
                                player2bulletlists.remove(bullets)
                                allbulletlists.remove(bullets)

        #move (player2)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            activeUnit2.x -= 3
            activeUnit2.stats = "Active"
            activeUnit2.direction = "Left"
        if key[pygame.K_RIGHT]:
            activeUnit2.x += 3
            activeUnit2.stats = "Active"
            activeUnit2.direction = "Right"
        if key[pygame.K_UP]:
            activeUnit2.y -= 3
            activeUnit2.stats = "Active"
            activeUnit2.direction = "Up"
        if key[pygame.K_DOWN]:
            activeUnit2.y += 3
            activeUnit2.stats = "Active"
            activeUnit2.direction = "Down"

        if key[pygame.K_SLASH]:
            if activeUnit2.classname == "classShield":
                if activeUnit2.delay == 0 and activeUnit2.alive == True:
                    pygame.mixer.Sound.play(shieldcharge)
                    if activeUnit2.direction == "Left":
                        activeUnit2.x -= shield_dashspeed
                    if activeUnit2.direction == "Right":
                        activeUnit2.x += shield_dashspeed
                    if activeUnit2.direction == "Up":
                        activeUnit2.y -= shield_dashspeed
                    if activeUnit2.direction == "Down":
                        activeUnit2.y += shield_dashspeed
                activeUnit2.delay += 1
            if activeUnit2.classname == "classMachinegun":
                if activeUnit2.delay == 0 and activeUnit2.alive == True:
                    pygame.mixer.Sound.play(MG_shoot)
                    bullet = pygame.sprite.Sprite()
                    bullet.origin = "player2"
                    DefaultBullet_initial(bullet, activeUnit2)
                    player2bulletlists.add(bullet)
                    allbulletlists.add(bullet)
                    activeUnit2.delay += 1
            if activeUnit2.classname == "classShotgun":
                if activeUnit2.delay == 0 and activeUnit2.alive == True:
                    pygame.mixer.Sound.play(shotgun_shoot)
                    bullet1 = pygame.sprite.Sprite()
                    bullet2 = pygame.sprite.Sprite()
                    bullet3 = pygame.sprite.Sprite()
                    bullet4 = pygame.sprite.Sprite()
                    bullet5 = pygame.sprite.Sprite()
                    bullet1.origin = "player2"
                    bullet2.origin = "player2"
                    bullet3.origin = "player2"
                    bullet4.origin = "player2"
                    bullet5.origin = "player2"
                    ShotgunBullet_initial(bullet1, activeUnit2, 9, 3)
                    ShotgunBullet_initial(bullet2, activeUnit2, 9, 1)
                    ShotgunBullet_initial(bullet3, activeUnit2, 9, 0)
                    ShotgunBullet_initial(bullet4, activeUnit2, 9, -1)
                    ShotgunBullet_initial(bullet5, activeUnit2, 9, -3)

                    player2bulletlists.add(bullet1,bullet2, bullet3, bullet4, bullet5)
                    allbulletlists.add(bullet1, bullet2, bullet3, bullet4, bullet5)

                    activeUnit2.delay += 1

        #switch units
        if key[pygame.K_j]:
            activeUnit2 = player2
        if key[pygame.K_k]:
            activeUnit2 = player2a
        if key[pygame.K_l]:
            activeUnit2 = player2b
        if key[pygame.K_SEMICOLON]:
            activeUnit2 = player2c
        if key[pygame.K_QUOTE]:
            activeUnit2 = player2d

        #move (player1)
        if key[pygame.K_a]:
            activeUnit1.x -= 3
            activeUnit1.stats = "Active"
            activeUnit1.direction = "Left"
        if key[pygame.K_d]:
            activeUnit1.x += 3
            activeUnit1.stats = "Active"
            activeUnit1.direction = "Right"
        if key[pygame.K_w]:
            activeUnit1.y -= 3
            activeUnit1.stats = "Active"
            activeUnit1.direction = "Up"
        if key[pygame.K_s]:
            activeUnit1.y += 3
            activeUnit1.stats = "Active"
            activeUnit1.direction = "Down"

        #shoot bullets(player1)
        if key[pygame.K_g]:
            if activeUnit1.classname == "classShield":
                if activeUnit1.delay == 0 and activeUnit1.alive == True:
                    pygame.mixer.Sound.play(shieldcharge)
                    if activeUnit1.direction == "Left":
                        activeUnit1.x -= shield_dashspeed
                    if activeUnit1.direction == "Right":
                        activeUnit1.x += shield_dashspeed
                    if activeUnit1.direction == "Up":
                        activeUnit1.y -= shield_dashspeed
                    if activeUnit1.direction == "Down":
                        activeUnit1.y += shield_dashspeed
                activeUnit1.delay += 1
            if activeUnit1.classname == "classMachinegun":
                if activeUnit1.delay == 0 and activeUnit1.alive == True:
                    pygame.mixer.Sound.play(MG_shoot)
                    bullet = pygame.sprite.Sprite()
                    bullet.origin = "player1"
                    DefaultBullet_initial(bullet, activeUnit1)
                    player1bulletlists.add(bullet)
                    allbulletlists.add(bullet)
                    activeUnit1.delay += 1
            if activeUnit1.classname == "classShotgun":
                if activeUnit1.delay == 0 and activeUnit1.alive == True:
                    pygame.mixer.Sound.play(shotgun_shoot)
                    bullet1 = pygame.sprite.Sprite()
                    bullet2 = pygame.sprite.Sprite()
                    bullet3 = pygame.sprite.Sprite()
                    bullet4 = pygame.sprite.Sprite()
                    bullet5 = pygame.sprite.Sprite()
                    bullet1.origin = "player1"
                    bullet2.origin = "player1"
                    bullet3.origin = "player1"
                    bullet4.origin = "player1"
                    bullet5.origin = "player1"
                    ShotgunBullet_initial(bullet1, activeUnit1, 9, 3)
                    ShotgunBullet_initial(bullet2, activeUnit1, 9, 1)
                    ShotgunBullet_initial(bullet3, activeUnit1, 9, 0)
                    ShotgunBullet_initial(bullet4, activeUnit1, 9, -1)
                    ShotgunBullet_initial(bullet5, activeUnit1, 9, -3)

                    player1bulletlists.add(bullet1,bullet2, bullet3, bullet4, bullet5)
                    allbulletlists.add(bullet1, bullet2, bullet3, bullet4, bullet5)

                    activeUnit1.delay += 1

        #switch units
        if key[pygame.K_1]:
            activeUnit1 = player1
        if key[pygame.K_2]:
            activeUnit1 = player1a
        if key[pygame.K_3]:
            activeUnit1 = player1b
        if key[pygame.K_4]:
            activeUnit1 = player1c
        if key[pygame.K_5]:
            activeUnit1 = player1d


        window.fill(white)

        for walls in walllists:
            wall_update(walls)

        for player1s in player1lists:
            if player1s.classname == "classMachinegun":
                classMachinegun_update(player1s)
            if player1s.classname == "classShotgun":
                classShotgun_update(player1s)
            if player1s.classname == "classShield":
                classShield_update(player1s)
        for player2s in player2lists:
            if player2s.classname == "classMachinegun":
                classMachinegun_update(player2s)
            if player2s.classname == "classShotgun":
                classShotgun_update(player2s)
            if player2s.classname == "classShield":
                classShield_update(player2s)

        #player1lists.update()
        #player2lists.update()
        for bullets in player1bulletlists:
            if bullets.type == "default":
                DefaultBullet_update(bullets)
            if bullets.type == "shotgun":
                ShotgunBullet_update(bullets)
        for bullets in player2bulletlists:
            if bullets.type == "default":
                DefaultBullet_update(bullets)
            if bullets.type == "shotgun":
                ShotgunBullet_update(bullets)

        pygame.display.update()
        clock.tick(fps)

        #reset
        activeUnit1.stats = "Idle"
        activeUnit2.stats = "Idle"

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(won)

    while gameEnd:
        window.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largetext = pygame.font.Font('freesansbold.ttf',30)
        mediumtext = pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect = text_objects("Congratulation", largetext)
        TextRect.center = ((400,30))
        window.blit(TextSurf, TextRect)
        winner_output = winner+" won!"
        TextSurf, TextRect = text_objects(winner_output, mediumtext)
        TextRect.center = ((400, 60))
        window.blit(TextSurf, TextRect)

        button_secondary("Back To Menu", 400-40,350-40, 80,80, light_white, green, "quit")
        pygame.display.update()

#loop infinitely unless pygame.quit() is used within the function beginning()
while True:
    beginning()
