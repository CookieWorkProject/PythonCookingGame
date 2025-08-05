import pygame
import numpy
from objects.BasicObject import BasicObject
from objects.CounterTop import CounterTop
from objects.Food import Food
class FoodDispenser(CounterTop):
    def __init__(self,*args):
        super().__init__(*args)
        self.stockFood = Food
        self.storedFood = self.stockFood(self.gameObjects, pygame.Rect(0,0,5,5))
    def takeFood(self):
        sendFood = self.storedFood
        self.storedFood = self.stockFood(self.gameObjects, pygame.Rect(0,0,5,5))
        return sendFood
    def draw(self,surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        