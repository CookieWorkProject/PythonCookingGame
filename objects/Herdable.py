import pygame
from objects.Solid import Solid
from objects.BlockLeft import BlockLeft
from objects.BlockRight import BlockRight
from objects.BlockUp import BlockUp
from objects.BlockDown import BlockDown
from objects.BasicObject import BasicObject
from objects.Enemy import Enemy
from objects.Player import Player
from objects.HerdRepeller import HerdRepeller
import numpy
import copy
class Herdable(BasicObject):
    def __init__(self,*args):
        super().__init__(*args) 
        
    








    def collision(self):
        for a in self.gameObjects:
            if a.active == False or self.rect.colliderect(a) == False :
                continue
            if type(a) == Enemy:
                
                self.active = False


    def draw(self,surface):
        pygame.draw.ellipse(surface, (196, 64, 64), self.rect)


    def step(self):
        xMove = 0
        yMove = 0
        for a in self.gameObjects:
            dist = self.distToObj(a)
            
            if dist >100:
                continue
            if type(a) == Player:
                
                
                vector = (a.getAxisDistToObjectX(self),a.getAxisDistToObjectY(self))
                normalVector = self.normalizeVector(vector)
                xMove += normalVector[0]*numpy.sqrt(dist)*.25
                yMove += normalVector[1]*numpy.sqrt(dist)*.25
            elif type(a) == HerdRepeller:
                
                
                vector = (a.getAxisDistToObjectX(self),a.getAxisDistToObjectY(self))
                normalVector = self.normalizeVector(vector)
                xMove += normalVector[0]*numpy.sqrt(dist)*a.repelPower
                yMove += normalVector[1]*numpy.sqrt(dist)*a.repelPower
            
        
        
        self.moveSelf(xMove,yMove)
    def getAllValidSolids(self,xMove=0,yMove=0):
        
        objects = list()
        for a in self.gameObjects:
            if type(a) == Solid:
                objects.append(a)
            if type(a) == BlockLeft and xMove>=0 and self.getRightX()<a.rect.left+1:
                objects.append(a)
            if type(a) == BlockRight and xMove<=0 and self.rect.left>a.getRightX()-1:
                
                objects.append(a)
            if type(a) == BlockUp and yMove<=0 and self.rect.top>a.getBottomY()-1:
                objects.append(a)
            if type(a) == BlockDown and yMove>=0 and self.getBottomY()<a.rect.top+1:
                objects.append(a)    
        #print("getAllValidSolids: "+str(len(objects)))
        #print("xpos: "+str(self.rect.left))
        return objects
    def moveSelf(self,xMove,yMove):
        solidList = self.getAllValidSolids(xMove,yMove)
        
        #push in X
        rect = self.getRectOffset(xMove,0)
        if self.meetingList(rect,solidList):
            #collision occured push in self
            while not self.meetingList(self.getRectOffset(numpy.sign(xMove),0),solidList):
                self.rect.left+=numpy.sign(xMove)
            xMove = 0
        #push in X
        rect = self.getRectOffset(0,yMove)
        if self.meetingList(rect,solidList):
            #collision occured push in self
            while not self.meetingList(self.getRectOffset(0,numpy.sign(yMove)),solidList):
                self.rect.top+=numpy.sign(yMove)
            yMove = 0
        #push in both
        rect = self.getRectOffset(xMove,yMove)
        if self.meetingList(rect,solidList):
            #collision occured push in self
            while not self.meetingList(self.getRectOffset(numpy.sign(xMove),numpy.sign(yMove)),solidList):
                self.rect.left+=numpy.sign(xMove)
                self.rect.top+=numpy.sign(yMove)
            xMove = 0
            yMove = 0
        self.rect.left+= xMove
        self.rect.top+= yMove