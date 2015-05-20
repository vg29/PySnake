import pygame
import random
import shelve

pygame.init()
#global gameExit
display_height = 360
display_width = 640
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Alpha v1')

icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)
#snaketail = pygame.image.load('tail.png')
appleimg = pygame.image.load('apple.png')
#scores = []


#pygame.display.update()

fps = 15
clock = pygame.time.Clock()

font = pygame.font.SysFont(None,25)
lfont = pygame.font.SysFont(None,50)

def checkscore(score):

    scorefile = open('score.txt','r+')
    scorefile.seek(0)
    high_score = int(scorefile.read())

    if score > high_score:
        scorefile.seek(0)
        hi_score = str(score)
        scorefile.write(hi_score)

    scorefile.close()
        
        

def showscore():
    try:
        readfile = open('score.txt','r')
        readfile.seek(0)
        high_score = int(readfile.read())
        readfile.close()
    except:
        high_score = 0
        
    text = font.render(" High Score: "+str(high_score), True, (0,0,0))
    gameDisplay.blit(text,[0,0])

    
def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_s:
                    paused = False
        
                    
        #gameDisplay.fill((255,255,255))
        message_screen("Paused!!",(255,0,0),-50,"med")
        message_screen("press 's' to play again 'q' to quit",(0,0,0),50)
        pygame.display.update()
        clock.tick(5)      
        
def score(score):
    text = font.render("Score: "+str(score), True, (0,0,0))
    gameDisplay.blit(text,[550,0])



def snake(snakelist,block_size):
    #gameDisplay.blit(snakehead, (snakelist[-1][0],snakelist[-1][1]))
    #gameDisplay.blit(snaketail, (snakelist[0][0],snakelist[0][1]))
    for XnY in snakelist:
        gameDisplay.fill((0,0,160), rect=[XnY[0],XnY[1],block_size,block_size])

def ltext_objects(text,color):
    textSurface = lfont.render(text, True, color)
    return textSurface,textSurface.get_rect()


def text_objects(text,color):
    textSurface = font.render(text, True, color)
    return textSurface,textSurface.get_rect()
    


def message_screen(msg,colour,y_displace=0,size="small"):
    if size == "small":
        textSurf,textRect = text_objects(msg,colour)
    elif size == "med":
        textSurf,textRect = ltext_objects(msg,colour)
    textRect.center = (display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)
##    screen_text=font.render(msg,True,colour)
##    gameDisplay.blit(screen_text,[display_width/2,display_height/2])




def gameloop():
    #global gameExit
    gameMenu = True
    gameExit = False
    gameOver = False
    block_size=10
    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_change = 0
    lead_y_change = -block_size
    appleSize = 30
    randomAppleX = random.randrange(0,(display_width-appleSize))
    randomAppleX = round(randomAppleX/10.0)*10.0
    randomAppleY = random.randrange(0,(display_height-appleSize))
    randomAppleY = round(randomAppleY/10.0)*10.0
    snakelist = []
    snakelength = 3
    


    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill((255,255,255))
            message_screen("Game Over!!",(255,0,0),-50,"med")
            message_screen("press 's' to play again 'q' to quit",(0,0,0),50)
            pygame.display.update()
            block_size=10
            lead_x=display_width/2
            lead_y=display_height/2
            lead_x_change = 0
            lead_y_change = -block_size
            appleSize = 30
            randomAppleX = random.randrange(0,(display_width-appleSize))
            randomAppleX = round(randomAppleX/10.0)*10.0
            randomAppleY = random.randrange(0,(display_height-appleSize))
            randomAppleY = round(randomAppleY/10.0)*10.0
            snakelist = []
            snakelength = 3
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
##                        gameExit = True
##                        gameOver = False
                    if event.key == pygame.K_s:
                        gameExit = False
                        gameOver = False

            

        while gameMenu == True:
            gameDisplay.fill((255,255,255))
            message_screen("Snake!!",(0,0,0),-50,"med")
            message_screen("Welcome, press 's' to play 'q' to quit",(255,0,0),50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameMenu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameMenu = False
                    if event.key == pygame.K_s:
                        gameExit = False
                        gameMenu = False
            


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change =  block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change =  block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        lead_x = (lead_x + lead_x_change) % display_width
        lead_y = (lead_y + lead_y_change) % display_height

        gameDisplay.fill((255,255,255))
        message_screen("Press 'p' to Pause",(0,0,0),-170)
        #pygame.draw.rect(gameDisplay,(0,255,0),[randomAppleX,randomAppleY,appleSize,appleSize])
        gameDisplay.blit(appleimg,(randomAppleX,randomAppleY))
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        if len(snakelist) > snakelength:
            del snakelist[0]

        for eachSegment in snakelist[:-1]:
            if eachSegment == snakehead:
                gameOver = True

        snake(snakelist,block_size)
        score(snakelength-3)
        checkscore(snakelength-3)
        showscore()
        pygame.display.update()

        if(lead_x > randomAppleX and lead_x < randomAppleX + appleSize) or ((lead_x+block_size) > randomAppleX and (lead_x + block_size) < randomAppleX + appleSize):
            if(lead_y > randomAppleY and lead_y < randomAppleY + appleSize) or (lead_y+block_size > randomAppleY and lead_y+block_size < randomAppleY + appleSize):
                snakelength +=1
                randomAppleX = random.randrange(0,(display_width-appleSize))
                randomAppleX = round(randomAppleX/10.0)*10.0
                randomAppleY = random.randrange(0,(display_height-appleSize))
                randomAppleY = round(randomAppleY/10.0)*10.0
                

##        if lead_x == randomAppleX and lead_y == randomAppleY:
##            snakelength +=1
##            randomAppleX = random.randrange(0,(display_width-block_size))
##            randomAppleX = round(randomAppleX/10.0)*10.0
##            randomAppleY = random.randrange(0,(display_height-block_size))
##            randomAppleY = round(randomAppleY/10.0)*10.0


        clock.tick(fps)

                
            #print event


            
    pygame.quit()
    quit()



gameloop()    
