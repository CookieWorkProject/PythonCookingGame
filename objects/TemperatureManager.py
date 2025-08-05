import pygame
from objects.TemperatureBlock import TemperatureBlock
from objects.BasicObject import BasicObject
import numpy
class TemperatureManager(BasicObject):
    def __init__(self,*args):
        super().__init__(*args) 
        self.canvas = pygame.Surface((800,600),flags=pygame.SRCALPHA)
        self.predraw = pygame.Surface((200,200),flags=pygame.SRCALPHA)
        pygame.draw.rect(self.canvas,(0,0,0,0),pygame.Rect(0,0,800,600))
        
        
    
    
    def getPixels(self):
        arr = pygame.PixelArray(self.canvas)
        colors = {}
        for a in arr:
            for b in a:
                if b in colors:
                    colors[b] += 1
                    
                else:
                    colors[b] = 1
        
        return colors
    
    def draw(self,surface):
        surface.blit(self.canvas, (0,0))
    
    
                
    def updateHeatmap(self):
        pygame.draw.rect(self.canvas,(128,128,128,255),pygame.Rect(0,0,800,600))
        for a in self.gameObjects:
            print(str(type(a)))
            if type(a) == TemperatureBlock:
                self.preDraw(a.temp)
                self.canvas.blit(self.predraw, (a.rect.left-100,a.rect.top-100))
                #self.canvas.blit(self.predraw, (a.rect.left,a.rect.top),special_flags=pygame.BLEND_RGBA_MULT)
                #if a.temp>0:
                #    self.canvas.blit(self.predraw, (a.rect.left,a.rect.top),special_flags=pygame.BLEND_RGBA_ADD)
                #else:
                #    self.canvas.blit(self.predraw, (a.rect.left,a.rect.top),special_flags=pygame.BLEND_RGBA_SUB)


    def preDraw(self,temp):
        
        circles = self.getCircleCount(temp)
        self.predraw.fill((0,0,0,0))
        while circles >0:
            if temp>0:
                pygame.draw.circle(self.predraw,(128+temp/circles,0,0,64),(100,100),100*(circles)/6)
            else:
                pygame.draw.circle(self.predraw,(0,0,128+abs(temp)/circles,64),(100,100),100*(circles)/6)
            circles -=1
        
    def getCircleCount(self,val):
        num = abs(val)
        circles = 0
        while num >1.1:
            num = numpy.sqrt(num)
            circles+=1
        return circles
        
        
    def getTempAt(self,x,y):
        
        
        return self.canvas.get_at((x, y)).r-self.canvas.get_at((x, y)).b
        