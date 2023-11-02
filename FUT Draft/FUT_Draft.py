
from sys import exit
import pygame

pygame.init()
pygame.display.set_caption("FUT Draft")
screen = pygame.display.set_mode((800, 600))
screen.fill('darkgreen')
running = True
#test = pygame.image.load('Grafiki/home.png')


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
  #  screen.blit(test,(0,0))
    pygame.display.update()
    