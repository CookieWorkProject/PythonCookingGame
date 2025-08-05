import pygame
import numpy
from objects.BasicObject import BasicObject
from objects.Food import Food
from objects.CounterTop import CounterTop
class Stove(CounterTop):
    def __init__(self,*args):
        super().__init__(*args)
        self.storedFood = None
        
        
    def step(self):
        if self.storedFood!=None and  isinstance(self.storedFood,Food):
            self.storedFood.cookLevel+=1
    def draw(self,surface):
        pygame.draw.rect(surface, (32, 32, 32), self.rect)
        if self.storedFood != None:
            self.storedFood.draw(surface)