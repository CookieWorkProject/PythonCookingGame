import pygame
import numpy
from objects.BasicObject import BasicObject

class Food(BasicObject):
    def __init__(self,*args):
        super().__init__(*args)
        self.cookLevel = 0
        
    def draw(self,surface):
        pygame.draw.rect(surface, (128, 128, 255), self.rect)
        