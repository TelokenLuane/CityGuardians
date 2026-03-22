#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, MENU_OPTION

COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/City2.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.selected_option = 0

    def run(self, menu_option=None):
        pygame.mixer.music.load('./asset/music1.mp3')
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(self.surf, self.rect)

            self.menu_text(
                text_size=60,
                text="City Guardians",
                text_color=COLOR_YELLOW,
                text_center_pos=(WIN_WIDTH / 2, 95)
            )

            for i, option in enumerate(MENU_OPTION):
                color = COLOR_YELLOW if i == self.selected_option else COLOR_WHITE

                self.menu_text(
                    text_size=25,
                    text=option,
                    text_color=color,
                    text_center_pos=(WIN_WIDTH / 2, 200 + 30 * i)
                )
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(MENU_OPTION)

                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(MENU_OPTION)

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[self.selected_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font = pygame.font.SysFont("Arcade Classic", text_size)
        text_surf: Surface = font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)