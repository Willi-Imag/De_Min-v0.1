""" Python3 docu-docu """
"""
"""
import pygame, sys
import psutil, GPUtil
"""
"""
pygame.init()

_clock = pygame.time.Clock()
_display = pygame.display
_screen = _display.set_mode((264, 264), pygame.NOFRAME)

images = [pygame.image.load('images/de_min-0.png'),
         pygame.image.load('images/de_min-1.png'),
         pygame.image.load('images/de_min-2.png')]

running = True

while running:

    _screen.fill((149, 99, 149))

    cpu_temp = psutil.sensors_temperatures()['k10temp'][0].current

    if cpu_temp < 50:
        _screen.blit(images[0], (4, 4))
    elif cpu_temp < 60:
        _screen.blit(images[1], (4, 4))
    elif cpu_temp > 60:
        _screen.blit(images[2], (4, 4))
    else: _screen.fill((244, 129, 129))
    
    _display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.time.wait(250)
    #_clock.tick(1)

pygame.quit()
sys.exit()
"""QwQ"""
