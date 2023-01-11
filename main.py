#Imports-------------------------------------------------+
import pygame
import sys
from pygame import mixer

#Setup Window--------------------------------------------+

#Clock
mainClock = pygame.time.Clock()

#Init
pygame.init()

#Caption
pygame.display.set_caption("Idle Folktales")

#Icon
icon = pygame.image.load("helmet.png")
pygame.display.set_icon(icon)

#Screen
screen = pygame.display.set_mode((800,600),0,32)

#font
smallfont = pygame.font.SysFont(None,20)
smallishfont = pygame.font.SysFont("freesansbold.ttf", 30)
bigfont = pygame.font.SysFont("freesansbold.ttf", 100)
mediumfont = pygame.font.SysFont("freesansbold.ttf",50)



#Draw Text-----------------------------------------------+
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

mixer.music.load("Kingdom Hearts 2 - Dearly Beloved II (128 kbps).mp3")
mixer.music.play(-1)

#Main Menu------------------------------------------------+
def main_menu():
    running = True
    while running:

        screen.fill((0,0,0))

        mx, my = pygame.mouse.get_pos()

        menuArt_image = pygame.image.load("menu art.png")
        startButton_image = pygame.image.load("StartButton.png")
        controlButton_image = pygame.image.load("controlsButton.png")
        #title_image = pygame.image.load("sign.png")
        background = pygame.image.load("background.png")


        play_button = pygame.Rect((screen.get_width()/2)-200,335,400,100)
        controls_button = pygame.Rect((screen.get_width()/2)-112.5,450,225,50)

        screen.blit(background, (0,0))
        screen.blit(menuArt_image, (150,35))
        screen.blit(startButton_image, ((screen.get_width()/2)-200,335))
        screen.blit(controlButton_image, ((screen.get_width()/2)-112.5,450))

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if play_button.collidepoint((mx,my)):
            if click:
                idle_menu()
                running = False
                mixer.music.stop()

        if controls_button.collidepoint((mx,my)):
            if click:
                controls_menu()

        pygame.display.update()
        mainClock.tick(100)

#Idle Menu--------------------------------------------+
def idle_menu():
    mixer.music.load("Lazy Afternoons -Remaster _ Kingdom Hearts 358_2 Days- (128 kbps).mp3")
    kaching = mixer.Sound("Cash Register (Kaching) - Sound Effect (HD) (128 kbps).mp3")
    mixer.music.play(-1)

    running = True
    clockStart = 1000
    milliseconds = 0
    seconds = 0
    minutes = 0
    hours = 0
    hours2 = 0

    score = 0
    upgrade1 = 0
    upgrade2 = 0
    upgrade3 = 0
    upgrade4 = 0
    upgrade5 = 0
    upgrade6 = 0
    upgrade7 = 0
    upgrade8 = 0
    upgrade9 = 0
    upgrade10 = 0

    cost_upgrade1 = 10
    cost_upgrade2 = 50
    cost_upgrade3 = 525
    cost_upgrade4 = 2125
    cost_upgrade5 = 11600
    cost_upgrade6 = 53750
    cost_upgrade7 = 250000
    cost_upgrade8 = 1250000
    cost_upgrade9 = 5350000
    cost_upgrade10 = 11250000

    multiplier = 1
    cost_presitge = 30000000

    while running:
        screen.fill((0,0,0))

        mx, my = pygame.mouse.get_pos()

        background = pygame.image.load("background.png")
        gems_image = pygame.image.load("gemIcon.png")
        #gems_imageFlipped = pygame.image.load("gemFlipped.png")
        getGems_button = pygame.image.load("getGems.png")
        backdrop = pygame.image.load("backdrop.png")
        tool_button = pygame.image.load("tool button.png")

        upgrade1_image = pygame.image.load("jacks beans.png")
        upgrade2_image = pygame.image.load("red hens.png")
        upgrade3_image = pygame.image.load("goldilocks bears.png")
        upgrade4_image = pygame.image.load("frog kings.png")
        upgrade5_image = pygame.image.load("mother geese.png")
        upgrade6_image = pygame.image.load("blue oxen.png")
        upgrade7_image = pygame.image.load("cave dragons.png")
        upgrade8_image = pygame.image.load("serpent kings.png")
        upgrade9_image =  pygame.image.load("rumples golden thread.png")
        upgrade10_image = pygame.image.load("midas golden touch.png")

        gems_button = pygame.Rect((screen.get_width()/2)-200,50,400,50)
        upgrade1_button = pygame.Rect(47.5,150,125,50)
        upgrade2_button = pygame.Rect(47.5,225,125,50)
        upgrade3_button = pygame.Rect(47.5,300,125,50)
        upgrade4_button = pygame.Rect(47.5,375,125,50)
        upgrade5_button = pygame.Rect(47.5,450,125,50)
        upgrade6_button = pygame.Rect(255,150,125,50)
        upgrade7_button = pygame.Rect(255,225,125,50)
        upgrade8_button = pygame.Rect(255,300,125,50)
        upgrade9_button = pygame.Rect(255,375,125,50)
        upgrade10_button = pygame.Rect(255,450,125,50)
        #battle_button = pygame.Rect((screen.get_width()/2)-100,525,200,25)
        prestige_button = pygame.Rect(500,197.5,200,25)
        win_button = pygame.Rect(500,422.5,200,25)

        screen.blit(background,(0,0))
        screen.blit(gems_image, (200,105))
        screen.blit(backdrop, (487.5,184))
        screen.blit(backdrop, (487.5,296.5))
        screen.blit(backdrop, (487.5,409))
        screen.blit(tool_button, (500,197.5))
        screen.blit(tool_button, (500,422.5))

        #screen.blit(gems_imageFlipped, (562,105))
        screen.blit(getGems_button, (200,50))
        screen.blit(upgrade1_image,(47.5,150))
        screen.blit(upgrade2_image,(47.5,225))
        screen.blit(upgrade3_image,(47.5,300))
        screen.blit(upgrade4_image,(47.5,375))
        screen.blit(upgrade5_image,(47.5,450))
        screen.blit(upgrade6_image,(255,150))
        screen.blit(upgrade7_image,(255,225))
        screen.blit(upgrade8_image,(255,300))
        screen.blit(upgrade9_image,(255,375))
        screen.blit(upgrade10_image,(255,450))
        #screen.blit(optionsButton_image, (645,50))

        #pygame.draw.rect(screen, (255,255,255), battle_button)

        draw_text(str(score), smallishfont, (255,255,255), screen, 235,112.5)
        draw_text(str(hours2).zfill(2) + ":" + str(hours).zfill(2) + ":" + str(minutes).zfill(2) , smallishfont, (255,255,255), screen, 558,312.5)

        draw_text(str(upgrade1), mediumfont, (255,255,255), screen, 177.5,157.5)
        draw_text(str(upgrade2), mediumfont, (255,255,255), screen, 177.5,232.5)
        draw_text(str(upgrade3), mediumfont, (255,255,255), screen, 177.5,307.5)
        draw_text(str(upgrade4), mediumfont, (255,255,255), screen, 177.5,382.5)
        draw_text(str(upgrade5), mediumfont, (255,255,255), screen, 177.5,457.5)
        draw_text(str(upgrade6), mediumfont, (255,255,255), screen, 385,157.5)
        draw_text(str(upgrade7), mediumfont, (255,255,255), screen, 385,232.5)
        draw_text(str(upgrade8), mediumfont, (255,255,255), screen, 385,307.5)
        draw_text(str(upgrade9), mediumfont, (255,255,255), screen, 385,382.5)
        draw_text(str(upgrade10), mediumfont, (255,255,255), screen, 385,457.5)

        draw_text("Cost:"+ str(cost_upgrade1), smallfont , (255,255,255), screen, (screen.get_width()/2)-344.5,202.5)
        draw_text("Cost:"+ str(cost_upgrade2), smallfont , (255,255,255), screen, (screen.get_width()/2)-344.5,277.5)
        draw_text("Cost:"+ str(cost_upgrade3), smallfont , (255,255,255), screen, (screen.get_width()/2)-344.5,352.5)
        draw_text("Cost:"+ str(cost_upgrade4), smallfont , (255,255,255), screen, (screen.get_width()/2)-344.5,427.5)
        draw_text("Cost:"+ str(cost_upgrade5), smallfont , (255,255,255), screen, (screen.get_width()/2)-344.5,502.5)
        draw_text("Cost:"+ str(cost_upgrade6), smallfont , (255,255,255), screen, (screen.get_width()/2)-137,202.5)
        draw_text("Cost:"+ str(cost_upgrade7), smallfont , (255,255,255), screen, (screen.get_width()/2)-137,277.5)
        draw_text("Cost:"+ str(cost_upgrade8), smallfont , (255,255,255), screen, (screen.get_width()/2)-137,352.5)
        draw_text("Cost:"+ str(cost_upgrade9), smallfont , (255,255,255), screen, (screen.get_width()/2)-137,427.5)
        draw_text("Cost:"+ str(cost_upgrade10), smallfont , (255,255,255), screen, (screen.get_width()/2)-137,502.5)
        draw_text("Prestige", smallfont , (255,255,255), screen, 570,170)
        draw_text("Cost:"+ str(cost_presitge), smallfont , (255,255,255), screen, 487.5,237.5)
        draw_text("End Game", smallfont , (255,255,255), screen, 565,395)
        draw_text("Cost: 100000000", smallfont , (255,255,255), screen, 487.5,462.5)

        click = False
        press = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    press = True

        if gems_button.collidepoint((mx,my)):
            if click:
                score += multiplier

        if press:
            score += multiplier

        if upgrade1_button.collidepoint((mx,my)):
            if click and score >= cost_upgrade1:
                upgrade1 += 1
                score -= cost_upgrade1
                cost_upgrade1 = (cost_upgrade1*2)
                kaching.play()

        if upgrade2_button.collidepoint((mx,my)):
            if click and score >= cost_upgrade2:
                upgrade2 += 1
                score -= cost_upgrade2
                cost_upgrade2 = (cost_upgrade2*2)
                kaching.play()

        if upgrade3_button.collidepoint((mx,my)):
            if click and score >= cost_upgrade3:
                upgrade3 += 1
                score -= cost_upgrade3
                cost_upgrade3 = (cost_upgrade3*2)
                kaching.play()

        if upgrade4_button.collidepoint((mx,my)):
            if click and score >= cost_upgrade4:
                upgrade4 += 1
                score -= cost_upgrade4
                cost_upgrade4 = (cost_upgrade4*2)
                kaching.play()

        if upgrade5_button.collidepoint((mx,my)):
            if click and score >= cost_upgrade5:
                upgrade5 += 1
                score -= cost_upgrade5
                cost_upgrade5 = (cost_upgrade5*2)
                kaching.play()

        if upgrade6_button.collidepoint((mx,my)):
            if click and score >= cost_upgrade6:
                upgrade6 += 1
                score -= cost_upgrade6
                cost_upgrade6 = (cost_upgrade6*2)
                kaching.play()

        if upgrade7_button.collidepoint((mx,my)):
            if click and score >= cost_upgrade7:
                upgrade7 += 1
                score -= cost_upgrade7
                cost_upgrade7 = (cost_upgrade7*2)
                kaching.play()

        if upgrade8_button.collidepoint((mx,my)):
            if click and score >= cost_upgrade8:
                upgrade8 += 1
                score -= cost_upgrade8
                cost_upgrade8 = (cost_upgrade8*2)
                kaching.play()

        if upgrade9_button.collidepoint((mx,my)):
            if click and score >= cost_upgrade9:
                upgrade9 += 1
                score -= cost_upgrade9
                cost_upgrade9 = (cost_upgrade9*2)
                kaching.play()

        if upgrade10_button.collidepoint((mx,my)):
            if click and score >= cost_upgrade10:
                upgrade10 += 1
                score -= cost_upgrade10
                cost_upgrade10 = (cost_upgrade10*2)
                kaching.play()

        if prestige_button.collidepoint((mx,my)):
            if click and score >= cost_presitge:
                multiplier += 1
                cost_presitge = cost_presitge*2

                score = 0
                upgrade1 = 0
                upgrade2 = 0
                upgrade3 = 0
                upgrade4 = 0
                upgrade5 = 0
                upgrade6 = 0
                upgrade7 = 0
                upgrade8 = 0
                upgrade9 = 0
                upgrade10 = 0

                cost_upgrade1 = 10
                cost_upgrade2 = 50
                cost_upgrade3 = 525
                cost_upgrade4 = 2125
                cost_upgrade5 = 11600
                cost_upgrade6 = 53750
                cost_upgrade7 = 250000
                cost_upgrade8 = 125000
                cost_upgrade9 = 5350000
                cost_upgrade10 = 11250000

                kaching.play()

        if win_button.collidepoint((mx,my)):
            if click and score >= 100000000:
                running = False
                game_over()
                mixer.music.stop()


        #if battle_button.collidepoint((mx,my)):
            #if click:
               #battle_menu()
                
        clockStart -= 1

        if(clockStart == 1000 or clockStart == 900 or clockStart == 800 or clockStart == 700 or clockStart == 600 or clockStart == 500 or  clockStart == 400 or clockStart == 300 or clockStart == 200 or clockStart == 100):
            score = score + (1 * upgrade1 * multiplier)

        if(clockStart == 1000 or clockStart == 890 or clockStart == 780 or clockStart == 670 or clockStart == 560 or clockStart == 450 or clockStart == 340 or clockStart == 230 or clockStart == 120):
                score = score + (5 * upgrade2 * multiplier)

        if(clockStart == 1000 or clockStart == 875 or clockStart == 750 or clockStart == 625 or clockStart == 500 or clockStart == 375 or clockStart == 250 or clockStart == 125):
                score = score + (25 * upgrade3 * multiplier)

        if(clockStart == 1000 or clockStart == 860 or clockStart == 720 or clockStart == 580 or clockStart == 440 or clockStart == 300 or clockStart == 160 ):
                score = score + (125 * upgrade4 * multiplier)

        if(clockStart == 1000 or clockStart == 830 or clockStart == 660 or clockStart == 490 or clockStart == 320 or clockStart == 150):
            score = score + (625 * upgrade5 * multiplier)

        if(clockStart == 1000 or clockStart == 800 or clockStart == 600 or clockStart == 400 or clockStart == 200):
            score = score + (3125 * upgrade6 * multiplier)

        if(clockStart == 1000 or clockStart == 750 or clockStart == 500 or clockStart == 250):
            score = score + (15625 * upgrade7 * multiplier)

        if(clockStart == 1000 or clockStart == 666 or clockStart == 333):
            score = score + (78125 * upgrade8 * multiplier)

        if(clockStart == 1000 or clockStart == 500):
            score = score + (390625 * upgrade9 * multiplier)

        if(clockStart == 1000):
            score = score + (1953125 * upgrade9 * multiplier)

        if(clockStart == 0):

            clockStart = 1000

        pygame.display.update()
        mainClock.tick(100)
        seconds += 1

        if(milliseconds / 100 == 1):
            milliseconds = 0
            seconds += 1

        if(seconds / 60 == 1):
            seconds = 0
            minutes += 1

        if(minutes / 60 == 1):
            minutes = 0
            hours += 1

        if(hours / 60 == 1):
            hours = 0
            hours2 += 1


#Options Menu-------------------------------------------+
def controls_menu():
    running = True

    while running:

        screen.fill((0,0,0))

        mx, my = pygame.mouse.get_pos()

        background = pygame.image.load("background.png")
        backButton_image = pygame.image.load("back button.png")

        back_button = pygame.Rect((screen.get_width()/2)-112.5,500,225,50)

        screen.blit(background,(0,0))
        screen.blit(backButton_image, ((screen.get_width()/2)-112.5,500))

        draw_text("Controls and Instructions", mediumfont , (255,255,255), screen, 180,75)
        draw_text("Controls:" , smallishfont , (255,255,255), screen, 50,125)
        draw_text("To collect gems, click on the -Get Gems- Button, or hit the space bar." , smallfont , (255,255,255), screen, 51,150)
        draw_text("Either way, you will collect gems." , smallfont , (255,255,255), screen, 51,175)
        draw_text("Purchasing Farms:" , smallishfont , (255,255,255), screen, 50,200)
        draw_text("To purchase a farm, simply click on the farm button." , smallfont , (255,255,255), screen, 51,225)
        draw_text("Before buying a farm though, make sure you have enough gems to make the purchase!" , smallfont , (255,255,255), screen, 51,250)
        draw_text("Farms will help you speed up gem production, and get you closer to prestige and end game.", smallfont , (255,255,255), screen, 51,275)
        draw_text("Prestige:" , smallishfont , (255,255,255), screen, 50,300)
        draw_text("Prestiges allow you to earn extra gems buy clicking and with farms, but at a cost;", smallfont , (255,255,255), screen, 51,325)
        draw_text("Each prestige will reset your stats, erasing all the ems you've collected and restarting the game." , smallfont , (255,255,255), screen, 51,350)
        draw_text("With a prestige, you get a boost in gem production, making the game progress much faster.", smallfont , (255,255,255), screen, 51,375)
        draw_text("End Game:" , smallishfont , (255,255,255), screen, 50,400)
        draw_text("End Game, or game over is achievable with enough gems at your disposal;", smallfont , (255,255,255), screen, 51,425)
        draw_text("After you purchase - End Game - the game will be over." , smallfont , (255,255,255), screen, 51,450)
        draw_text("Compete with friends, and see who can beat the game in the least amount of time!!", smallfont , (255,255,255), screen, 51,475)

        click = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if back_button.collidepoint((mx,my)):
            if click == True:
                running = False

        pygame.display.update()
        mainClock.tick(100)

#Battle Menu--------------------------------------------------------------+
def battle_menu():
    running = True

    while running:

        screen.fill((0,0,0))

        return_button = pygame.Rect((screen.get_width()/2)-200,50,400,100)

        draw_text("Battle menu", smallfont , (255,255,255), screen, 20,20)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(100)

#Game Over-----------------------------------------------------------------+
def game_over():
    mixer.music.load("lovbug - Love w_ 4am.mp3")
    mixer.music.play((-1))

    running = True
    while running:

        background = pygame.image.load("background.png")
        menuArt_image = pygame.image.load("menu art.png")

        screen.fill((0,0,0))
        screen.blit(background, (0,0))
        screen.blit(menuArt_image, (150,225))
        draw_text("Game Over!", bigfont, (255,255,255), screen, 200,100)
        draw_text("Art, Game Design and Code by Ian Kwiatkowski", smallishfont, (255,255,255), screen, 170,200)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(100)

main_menu()