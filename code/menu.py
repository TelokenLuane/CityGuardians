#!/usr/bin/python
# -*- coding: utf-8 -*-
COLOR_WHITE = (255, 255, 255)

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_WELLOY, MENU_OPTION

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/City2.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, MENU_OPITION=None):
        pygame.mixer.music.load('./asset/music1.mp3')
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(
                text_size=60,
                text="City Guardians",
                text_color=COLOR_WELLOY,
                text_center_pos=(WIN_WIDTH / 2, 95)
            )

            for i, option in enumerate(MENU_OPTION):
                self.menu_text(
                    text_size=25,
                    text=option,
                    text_color=COLOR_WHITE,
                    text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i)
                )

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> object:
        font = pygame.font.SysFont("Arial", text_size)
        text_surf: Surface = font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)


