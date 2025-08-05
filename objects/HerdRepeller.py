import pygame
from objects.Solid import Solid
from objects.BlockLeft import BlockLeft
from objects.BlockRight import BlockRight
from objects.BlockUp import BlockUp
from objects.BlockDown import BlockDown
from objects.BasicObject import BasicObject
import numpy
import copy
class HerdRepeller(BasicObject):
    def __init__(self,*args):
        super().__init__(*args) 
        self.repelPower = .5
        
        
    def draw(self,surface):
        pygame.draw.ellipse(surface, (64, 128, 196), self.rect)