import pygam
import pygame.display

window=pygame.display.set_mode((500,500))

x=0
y=0
width=25
higth=25

flag=True

while flag:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            flag=False


    pygame.draw.rect(window,(255,0,0),(x,y,width,higth))
    pygame.display.update()