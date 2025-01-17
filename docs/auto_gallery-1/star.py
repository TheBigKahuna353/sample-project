"""
Author: Abdur-Rahmaan Janhangeer
Github: https://github.com/Abdur-rahmaanJ
"""

from hooman import Hooman

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)


def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False


hapi.handle_events = handle_events

clock = pygame.time.Clock()

while hapi.is_running:
    hapi.background(bg_col)

    hapi.fill(hapi.color["red"])
    hapi.star(100, 100, 30, 70, hapi.mouseX() // 10)

    hapi.event_loop()

    hapi.flip_display()

    clock.tick(60)

pygame.quit()
