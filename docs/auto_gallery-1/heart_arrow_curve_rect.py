"""
Author: https://github.com/TheBigKahuna353
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

    hapi.rotate(hapi.mouseX())

    hapi.fill(hapi.color["red"])
    hapi.heart(10, 200, hapi.mouseX() // 4, hapi.mouseY() // 4)

    hapi.arrow(300, 200, hapi.mouseX(), hapi.mouseY() // 2)

    hapi.curve_rect(10, 10, 200, 100, hapi.mouseY() // 5)

    hapi.event_loop()

    hapi.flip_display()

    clock.tick(60)

pygame.quit()
