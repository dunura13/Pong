import pygame
import math
import random




pygame.init()



# WINDOW

DIMENSIONS = (1000,700)
window = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption("Pong")


# COLOURS

WHITE = (255,255,255)




# PLAYER 1 (LEFT SIDE)


player1X = 100
player1Y = 350

player1Y_change = 0


def drawPlayer1(x,y):
    player1 = pygame.Rect(x,y, 10,50)
    pygame.draw.rect(window,WHITE,player1)




# PLAYER 2 (RIGHT SIDE)

player2X = 900
player2Y = 350

player2Y_change = 0

def drawPlayer2(x,y):
    player2 = pygame.Rect(x,y, 10,50)
    pygame.draw.rect(window,WHITE,player2)



# BORDER

def drawBorder():
    border = pygame.Rect(500,0,5,700)
    pygame.draw.rect(window,WHITE,border)



# DRAW BALL
ballX = 500
ballY = 350

ballX_change = 4
ballY_change = 4

flag = 0

def drawBall(x,y):
    pygame.draw.circle(window,WHITE,(x,y),5)


# COLLISION BETWEEN BALL AND PLAYER

def isCollision(x1,y1,x2,y2):
    distance = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))

    return distance




#PLAYER SCORES

player1_score = 0
player2_score = 0

def drawScore1():
    font = pygame.font.Font('freesansbold.ttf',24)
    scoreText = font.render(str(player1_score),True,WHITE)

    scoreText_rect = scoreText.get_rect()
    scoreText_rect.center = (75,20)
    
    window.blit(scoreText, scoreText_rect)

def drawScore2():
    font = pygame.font.Font('freesansbold.ttf',24)
    scoreText = font.render(str(player2_score),True,WHITE)

    scoreText_rect = scoreText.get_rect()
    scoreText_rect.center = (925,20)
    
    window.blit(scoreText, scoreText_rect)

# GAME LOOP

running = True

while running:

    window.fill((0,0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        
        if event.type == pygame.KEYDOWN:

            # PLAYER 1 KEYS
            if event.key == pygame.K_w:
                player1Y_change = -8
            
            elif event.key == pygame.K_s:
                player1Y_change = 8
            
            # PLAYER 2 KEYS

            if event.key == pygame.K_UP:
                player2Y_change = -8
            
            elif event.key == pygame.K_DOWN:
                player2Y_change = 8
        
        

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1Y_change = 0
            
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2Y_change = 0
        





    # PLAYER 1 MOVEMENT
    
    drawPlayer1(player1X,player1Y)
    player1Y+=player1Y_change


    #PLAYER 2 MOVEMENT
    drawPlayer2(player2X,player2Y)
    player2Y+=player2Y_change


    # DRAW BORDER
    drawBorder()

    #PLAYER BORDERS

    if player1Y <= 0:
        player1Y = 0
    
    if player1Y >= 650:
        player1Y = 650
    
    if player2Y <= 0:
        player2Y = 0
    
    if player2Y >=650:
        player2Y = 650

    

    # BALL MECHANICS
    drawBall(ballX,ballY)
    


    ballX+=ballX_change
    ballY+=ballY_change

    collision1 = isCollision(ballX,ballY,player1X,player1Y)
    collision2 = isCollision(player2X,player2Y,ballX,ballY)



    if ballY>= 700:
        ballY_change*=-1

    if ballX >=1000:
        ballX_change*=-1

    if ballY<=0:
        ballY_change*=-1
    
    if ballX <=0:
        ballX_change*=-1
    
    
    
    if collision1 <= 50:
        ballX_change = 4


    if collision2 <= 50:
        ballX_change = -4
        



    if ballX < player1X-50:
        player2_score+=1
        ballX = 500
        ballY= 350


    if ballX > player2X+50:
        player1_score+=1
        ballX = 500
        ballY= 350


    
  
    

        
    



    

    drawScore1()
    drawScore2()




    pygame.display.update()