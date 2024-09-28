import pygame
import os
screen=pygame.display.set_mode((800,500))
playing=True
fp=60
VELOCITY=5
clock=pygame.time.Clock()
bgimage=pygame.image.load('background.png')
redimage=pygame.image.load('rocket1.png')
yellowimage=pygame.image.load('rocket2.png')
redimage1=pygame.transform.rotate(pygame.transform.scale(redimage,(50,50)),270)
yellowimage1=pygame.transform.rotate(pygame.transform.scale(yellowimage,(50,50)),90)

yellow=pygame.Rect(150,200,40,40)
red=pygame.Rect(600,200,40,40)

while playing:
    def redmove(keypressed,red):
        if keypressed[pygame.K_UP] and red.y>0 :
            red.y=red.y-5
        if keypressed[pygame.K_DOWN] and red.y<460:
            red.y=red.y+5
        if keypressed[pygame.K_LEFT]:
            red.x=red.x-5
        if keypressed[pygame.K_RIGHT]:
            red.x=red.x+5
    def yellowmove(keypressed,yellow):
        if keypressed[pygame.K_w]:
            yellow.y=yellow.y-5
        if keypressed[pygame.K_s]:
            yellow.y=yellow.y+5
        if keypressed[pygame.K_a]:
            yellow.x=yellow.x-5
        if keypressed[pygame.K_d]:
            yellow.x=yellow.x+5
    

    clock.tick(fp)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
    screen.fill('dark blue')
    screen.blit(yellowimage1,(yellow.x,yellow.y))
    screen.blit(redimage1,(red.x,red.y))
    keypressed=pygame.key.get_pressed()
    redmove(keypressed,red)
    yellowmove(keypressed,yellow)
    pygame.display.update()



