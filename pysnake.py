import pygame
import random

pygame.init()
#global gameExit
display_height = 360
display_width = 640
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Alpha v1')

#pygame.display.update()

fps = 15
clock = pygame.time.Clock()

font = pygame.font.SysFont(None,25)


def snake(snakelist,block_size):
    for XnY in snakelist:
        gameDisplay.fill((155,155,155), rect=[XnY[0],XnY[1],block_size,block_size])


def text_objects(text,color):
    textSurface = font.render(text, True, color)
    return textSurface,textSurface.get_rect()
    


def message_screen(msg,colour):
    textSurf,textRect = text_objects(msg,colour)
    textRect.center = (display_width/2),(display_height/2)
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
    randomAppleX = random.randrange(0,(display_width-block_size))
    randomAppleX = round(randomAppleX/10.0)*10.0
    randomAppleY = random.randrange(0,(display_height-block_size))
    randomAppleY = round(randomAppleY/10.0)*10.0
    snakelist = []
    snakelength = 3
    appleSize = 30



    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill((255,255,255))
            message_screen("GameOver, press 's' to play 'q' to quit",(255,0,0))
            pygame.display.update()
            block_size=10
            lead_x=display_width/2
            lead_y=display_height/2
            lead_x_change = 0
            lead_y_change = -block_size
            randomAppleX = random.randrange(0,(display_width-block_size))
            randomAppleX = round(randomAppleX/10.0)*10.0
            randomAppleY = random.randrange(0,(display_height-block_size))
            randomAppleY = round(randomAppleY/10.0)*10.0
            snakelist = []
            snakelength = 3
            appleSize = 30

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
            message_screen("Welcome, press 's' to play 'q' to quit",(255,0,0))
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

        lead_x = (lead_x + lead_x_change) % display_width
        lead_y = (lead_y + lead_y_change) % display_height

        gameDisplay.fill((155,0,0))
        pygame.draw.rect(gameDisplay,(0,255,0),[randomAppleX,randomAppleY,appleSize,appleSize])
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
        
        pygame.display.update()

        if(lead_x >= randomAppleX and lead_x <= randomAppleX + appleSize):
            if(lead_y >= randomAppleY and lead_y <= randomAppleY + appleSize):
                snakelength +=1
                randomAppleX = random.randrange(0,(display_width-block_size))
                randomAppleX = round(randomAppleX/10.0)*10.0
                randomAppleY = random.randrange(0,(display_height-block_size))
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
