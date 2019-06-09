import pygame

from pygame.locals import *

pygame.init()

size = [400, 400]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bat and Ball")

pygame.mouse.set_visible(0)

bat_surf = pygame.Surface((64,12))
bat_surf.fill(( 0, 255, 0 )




