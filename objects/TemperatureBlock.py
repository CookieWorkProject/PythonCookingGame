import pygame

from objects.BasicObject import BasicObject
class TemperatureBlock(BasicObject):
    def __init__(self,*args):
        super().__init__(*args)
        self.temp = 100
        
        
        
    