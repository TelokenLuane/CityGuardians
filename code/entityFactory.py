#!/usr/bin/python
# -*- coding: utf-8 -*-

from .background import Background
from .const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg