import pygame
import numpy
from objects.BasicObject import BasicObject
class CounterTop(BasicObject):
    def __init__(self,*args):
        super().__init__(*args)
        self.storedFood = None
    def takeFood(self):
        sendFood = self.storedFood
        self.storedFood = None
        return sendFood
    def draw(self,surface):
        pygame.draw.rect(surface, (255, 64, 64), self.rect)
        if self.storedFood != None:
            self.storedFood.draw(surface)