import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 710))
background = pygame.image.load('images/bts_main.jpg').convert()
playerImg = pygame.image.load('images/char1.png')
fire = pygame.image.load('images/f2.png')

pygame.display.set_caption("BTSWorld")
icon = pygame.image.load('images/interface.png')
pygame.display.set_icon(icon)


def player(x, y):
    screen.blit(playerImg, (x, y))

def fire(x, y, val):
    f1 = pygame.image.load('images/f1.png')
    f2 = pygame.image.load('images/f2.png')
    f3 = pygame.image.load('images/f3.png')
    f = [f1, f2, f3]
    screen.blit(f[val], (x+5, y+5))


running = True

x=100
y=100
val=0
temp=0
while running:
    temp+=1

    screen.fill((0,0,0))
    screen.blit(background, (0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        if event.type == pygame.KEYDOWN:
            # x += 10
            c=0
            if event.key == pygame.K_DOWN:
                while c<25:
                    y += 1
                    c+=1
            if event.key == pygame.K_UP:
                while c<25:
                    y -= 1
                    c+=1
            if event.key == pygame.K_LEFT:
                while c<25:
                    x -= 1
                    c+=1
            if event.key == pygame.K_RIGHT:
                while c<25:
                    x += 1
                    c+=1
    if temp%5 == 0:
        temp = 0
        val += 1
    if val == 3:
        val = 0
    fire(x, y, val)
    player(x,y)
    pygame.display.update()
    
    # scree.fill(())