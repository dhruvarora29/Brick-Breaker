import pygame
import random

pygame.init()


width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

color_1 = 200, 120, 100
red = 255, 0, 0
white = 255, 255, 255
black = 0, 0, 0
blue = 0,0,255





def score(s):
    font = pygame.font.SysFont(None,25)
    text = font.render("Score : {}".format(s),True,red)
    screen.blit(text, (10,10))

def life(lifeRemaining):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Life Remaining : {}".format(lifeRemaining), True, red)
    screen.blit(text, (200, 10))

def gameOver():
    font_1 = pygame.font.SysFont(None,80)
    text_1 = font_1.render("Game Over!",True,black)
    font_2 = pygame.font.SysFont(None,60)
    text_2 = font_2.render("Press Any Key to Start Again",True,blue)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                main()

        screen.blit(text_1,(200,100))
        screen.blit(text_2,(100,250))

        pygame.display.update()


def main():
    barWidth = 70
    barHeight = 20
    img = pygame.Surface((barWidth,barHeight))
    #img_1=pygame.Surface((barWidth,barHeight))
    img.fill(red)
    #img_1.fill(red)
    barRect = img.get_rect()

    barRect_1=img.get_rect()
    barRect_2 = img.get_rect()
    barRect_3 = img.get_rect()
    barRect_4 = img.get_rect()
    barRect_5 = img.get_rect()
    barRect_6 = img.get_rect()

    barRect.center  = width/2, height/2
    barRect_1.center = width/2-70,height/2
    barRect_2.center = width / 2+70, height / 2
    barRect_3.center = width / 2+140, height / 2
    barRect_4.center = width / 2+210, height / 2
    barRect_5.center = width / 2-140, height / 2
    barRect_6.center = width / 2-210, height / 2

    barRect.y = height - 25
    barRect_1.y=height-25
    barRect_3.y = height - 25
    barRect_4.y = height - 25
    barRect_5.y = height - 25
    barRect_6.y = height - 25
    barRect_2.y = height - 25

    moveX = 0

    brickSurface = pygame.Surface((width-50,175))
    # brickSurface.fill(white)

    brickWidth = 100
    brickheight = 30

    brickList = []
    brickColors = []
    for row in range(1,6):
        for col in range(9):
            brickX = col * (brickWidth+5)
            brickY = row * (brickheight+5)
            color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            brickColors.append(color)
            brickList.append(pygame.Rect(brickX,brickY,brickWidth,brickheight))

    ballSurface = pygame.Surface((8,8))
    ballSurface.fill(blue)
    ballRect = ballSurface.get_rect()

    ballRadius = 8
    ballY = barRect.y - ballRadius
    moveBall = False
    ballOnBar = True
    moveBallY = 0
    moveBallX = 0

    FPS = 100
    clock = pygame.time.Clock()

    counter = 0
    lifeRemaining = 3

    while True:
        keypressed = pygame.key.get_pressed()
        if ballOnBar:
            ballX = barRect.x + barWidth // 2
            if keypressed[pygame.K_SPACE]:
                moveBall = True
                ballOnBar = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        if keypressed[pygame.K_RIGHT] and barRect.x<=870 and barRect_1.x<=800 and barRect_2.x<=930:
            moveX = 5
        elif keypressed[pygame.K_LEFT] and barRect.x>=70 and barRect_1.x>=0 and barRect_2.x>=140:
            moveX = -5

        else:
            moveX = 0

        screen.fill(white)
        brickSurface.fill(white)
        screen.blit(brickSurface, (30, 20))
        screen.blit(img,(barRect.x,barRect.y))
        screen.blit(img,(barRect_1.x,barRect_1.y))
        screen.blit(img, (barRect_2.x, barRect_2.y))
        for i in range(len(brickList)):
            pygame.draw.rect(screen,brickColors[i],brickList[i])

        pygame.draw.circle(screen,blue,(ballX,ballY),ballRadius)
        ballRect = pygame.Rect(ballX,ballY,ballRadius,ballRadius)

        if moveBall:
            moveBallY = -3
            moveBallX = 3
            moveBall = False

        ballX += moveBallX
        ballY += moveBallY
        barRect.x += moveX
        barRect_1.x += moveX
        barRect_2.x += moveX


        for i in range(len(brickList)):
            if brickList[i].colliderect(ballRect):
                del brickList[i]
                if moveBallY==3:
                    moveBallY=-3

                else:
                    moveBallY= 3

                FPS += 5
                counter += 1

                break

        if ballX > width - ballRadius:
            moveBallX = -3
        elif ballX < ballRadius:
            moveBallX = 3
        elif ballY < ballRadius:
            moveBallY = 3

        elif ballRect.colliderect(barRect):
            moveBallY = -3
        elif ballRect.colliderect(barRect_1):
            moveBallY = -3
            moveBallX = -3
        elif ballRect.colliderect(barRect_2):
            moveBallY = -3
            moveBallX = 3

        elif ballY > height * 2:
            ballOnBar = True
            moveBallX = 0
            moveBallY = 0
            ballY = barRect.y - ballRadius
            lifeRemaining -= 1

        if lifeRemaining == 0:
            gameOver()
        if counter==45:
            screen.fill(white)
            gameOver()

        score(counter)
        life(lifeRemaining)

        pygame.display.flip()
        clock.tick(FPS)

main()