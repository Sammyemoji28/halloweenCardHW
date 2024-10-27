
import pygame
import time

pygame.init()
pygame.display.set_caption("Halloween Card!") 
screen = pygame.display.set_mode((600,600))

w = 600
h = 600

image1 = pygame.image.load("image1.png")
image2 = pygame.image.load("image2.png")
image3 = pygame.image.load("image3.png")
image4 = pygame.image.load("image4.png")

image1 = pygame.transform.scale(image1, (w,h))
image2 = pygame.transform.scale(image2, (w,h))
image3 = pygame.transform.scale(image3, (w,h))
image4 = pygame.transform.scale(image4, (w,h))

while True:
    font1 = pygame.font.SysFont("Calibri", 40)
    text1=font1.render("Happy Halloween!",True,(0,0,0))
    screen.fill("white")
    screen.blit(image1,(0,0))
    screen.blit(text1,(150,50))
    pygame.display.update()
    time.sleep(2)

    font2 = pygame.font.SysFont("Times New Roman", 30)
    text2 = font2.render("Spooky Scary Skeletons!",True,(0,0,0))
    screen.fill("white")
    screen.blit(image2,(0,0))
    screen.blit(text2,(150,100))
    pygame.display.update()
    time.sleep(2)

    font3 = pygame.font.SysFont("Arial", 50)
    text3 = font3.render("BOO!",True,(0,0,0))
    screen.fill("white")
    screen.blit(image3,(0,0))
    screen.blit(text3,(150,50))
    pygame.display.update()
    time.sleep(2)

    font4 = pygame.font.SysFont("Calibri", 30)
    text4 = font4.render("Trick Or Treat!!",True,(0,0,0))
    screen.fill("white")
    screen.blit(image4,(0,0))
    screen.blit(text4,(400,50))
    pygame.display.update()
    time.sleep(2)
