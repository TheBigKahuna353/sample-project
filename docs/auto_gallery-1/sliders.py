"""
Author: https://github.com/TheBigKahuna353
"""

from hooman import Hooman

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)

slider_options = {
    "background_color": hapi.color["grey"],
    "slider_color": (220, 220, 220),
}

real_slider = hapi.slider(50, 300, 400, 30, slider_options)

slider_2 = hapi.slider(50, 250, 100, 30, slider_options)


def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False


hapi.handle_events = handle_events


while hapi.is_running:
    hapi.background(bg_col)

    hapi.fill(int(real_slider.value() * 255))
    hapi.rect(10, 10, 100, 100)

    real_slider.update()
    slider_2.set_value(real_slider.value())
    slider_2.update()
    real_slider.set_value(slider_2.value())

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
