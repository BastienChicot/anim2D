# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:23:43 2022

@author: bchicot
"""

# import os

# os.getcwd()
# os.chdir("Documents/Perso")

import math
import pygame

fond = pygame.image.load('bank/image/fond.png')
pygame.init()

screen = pygame.display.set_mode((800, 800))

class Image():
    def __init__(self,image,pos,originPos, attached = False, down = True):
        self.image = image
        self.attached = attached
        self.down = down
        if not attached:
            self.pos = pos
        else:
            if down:
                self.pos = pos.rotated_image_rect.center[0]-pos.rotated_offset[0],pos.rotated_image_rect.center[1]-pos.rotated_offset[1]
            elif not down:
                self.pos = pos.rotated_image_rect.center[0]+pos.rotated_offset[0],pos.rotated_image_rect.center[1]+pos.rotated_offset[1]
                
        self.originPos = originPos
            
    def blitRotate(self,surf,angle):
        self.image_rect = self.image.get_rect(topleft = (self.pos[0] - self.originPos[0], self.pos[1]-self.originPos[1]))
        self.offset_center_to_pivot = pygame.math.Vector2(self.pos) - self.image_rect.center
        self.rotated_offset = self.offset_center_to_pivot.rotate(-angle)
        self.rotated_image_center = (self.pos[0] - self.rotated_offset.x, self.pos[1] - self.rotated_offset.y)
        self.rotated_image = pygame.transform.rotate(self.image, angle)
        self.rotated_image_rect = self.rotated_image.get_rect(center = self.rotated_image_center)
        surf.blit(self.rotated_image, self.rotated_image_rect)
        
    def update_pos(self,pos):
        if not self.attached:
            self.pos = pos
        else:
            if self.down:
                self.pos = pos.rotated_image_rect.center[0]-pos.rotated_offset[0],pos.rotated_image_rect.center[1]-pos.rotated_offset[1]
            elif not self.down:
                self.pos = pos.rotated_offset[0]-pos.rotated_image_rect.center[0],pos.rotated_offset[1]-pos.rotated_image_rect.center[1]
            
        return(self.pos)

    def anim_punch(self,frame, angle_max, angle_min):
        ##FONCTION PARABOLE MOUVEMENT
        # angle = (frame-(max_frame/2))² * ((angle_max-angle_min)/((frame-(max_frame/2))² -angle_min)+angle_min
        
        angle = (frame - 10)**2 * ((angle_max-angle_min)/((10)**2)) + angle_min
        
        return(angle)
        
def boucle():
    gameExit=False
    
    pygame.init()
    size = (800,800)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    
    torse_image = pygame.image.load('bank/image/torse.png')
    cuisse_img = pygame.image.load('bank/image/cuisse.png')
    mollet_img = pygame.image.load('bank/image/mollet.png')
    image = pygame.image.load('bank/image/bras.png')
    image2 = pygame.image.load("bank/image/avant-bras.png")
    
    pivot0 = (50,175)
    pivot = (25, 18)
    pivot2 = (10,18)
    pivot_nul = (40,18)
    pivot_mol = (0,18)

    base = 0
    angle_cuisse = 0
    angle_mollet = 0
    angle, frame = 60, 0
    angle2 = 160
    
    torse = Image(torse_image,(375,460),pivot0)
    torse.blitRotate(screen, base)

    cuisse = Image(cuisse_img,torse,pivot_nul, attached = True, down = False)
    cuisse.blitRotate(screen, angle_cuisse)

    mollet = Image(mollet_img,cuisse,pivot_mol,attached=True)
    mollet.blitRotate(screen,angle_mollet)
    
    img = Image(image,torse,pivot,attached=True)
    img.blitRotate(screen,angle)
        
    img2 = Image(image2,img,pivot2,attached=True)
    img2.blitRotate(screen,angle2)
    
    rot = 0
    rot2 = 0
    rot0 = 0

    clock = pygame.time.Clock()
    
    action = False
    punch = False
    
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    action = True
                
                if event.key == pygame.K_a:
                    frame = 0
                    punch = True
                        
                if event.key == pygame.K_UP and not action:
                    rot = 4
                    rot2 = 4
                if event.key == pygame.K_UP and action:
                    rot = 4
                    rot2 = 8
       
                if event.key == pygame.K_DOWN and angle == angle2:
                    rot = -4
                    rot2 = -4
                if event.key == pygame.K_DOWN and angle != angle2:
                    rot = -4
                    rot2 = -8

                if event.key == pygame.K_LEFT:
                    rot0 = -1
                if event.key == pygame.K_RIGHT:
                    rot0 = 1
                
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    rot0 = 0
                
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    rot = 0
                    rot2 = 0
                if event.key == pygame.K_RETURN:
                    action = False
                    
        screen.blit(fond,(0,0))

        pos0 = (375,460)
        torse.blitRotate(screen, base)
        
        pos = img.pos
        pos2 = img2.pos
        pos3 = cuisse.pos
        pos4 = mollet.pos
        
        cuisse = Image(cuisse_img,torse,pivot_nul, attached = True, down = False)
        cuisse.blitRotate(screen, angle_cuisse)
        torse.blitRotate(screen, base)

        mollet = Image(mollet_img,cuisse,pivot_mol,attached=True)
        mollet.blitRotate(screen,angle_mollet)
        
        img = Image(image,torse,pivot,attached=True)
        img.blitRotate(screen,angle)

        img2 = Image(image2,img,pivot2,attached=True)
        img2.blitRotate(screen,angle2)

        pygame.draw.line(screen, (0, 255, 0), (pos0[0]-20, pos0[1]), (pos0[0]+20, pos0[1]), 3)
        pygame.draw.line(screen, (0, 255, 0), (pos0[0], pos0[1]-20), (pos0[0], pos0[1]+20), 3)
        pygame.draw.circle(screen, (0, 255, 0), pos0, 7, 0)
        
        pygame.draw.line(screen, (0, 255, 0), (pos[0]-20, pos[1]), (pos[0]+20, pos[1]), 3)
        pygame.draw.line(screen, (0, 255, 0), (pos[0], pos[1]-20), (pos[0], pos[1]+20), 3)
        pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)

        pygame.draw.line(screen, (0, 255, 0), (pos2[0]-20, pos2[1]), (pos2[0]+20, pos2[1]), 3)
        pygame.draw.line(screen, (0, 255, 0), (pos2[0], pos2[1]-20), (pos2[0], pos2[1]+20), 3)
        pygame.draw.circle(screen, (0, 255, 0), pos2, 7, 0)
        
        pygame.draw.line(screen, (0, 255, 0), (pos3[0]-20, pos3[1]), (pos3[0]+20, pos3[1]), 3)
        pygame.draw.line(screen, (0, 255, 0), (pos3[0], pos3[1]-20), (pos3[0], pos3[1]+20), 3)
        pygame.draw.circle(screen, (0, 255, 0), pos3, 7, 0)

        pygame.draw.line(screen, (0, 255, 0), (pos4[0]-20, pos4[1]), (pos4[0]+20, pos4[1]), 3)
        pygame.draw.line(screen, (0, 255, 0), (pos4[0], pos4[1]-20), (pos4[0], pos4[1]+20), 3)
        pygame.draw.circle(screen, (0, 255, 0), pos4, 7, 0)


        frame += 1

        if punch and frame <= 20 :
            base = torse.anim_punch(frame, 0, -5)
            angle = img.anim_punch(frame, 60, 90)
            angle2 = img2.anim_punch(frame, 160, 100)
        else:
            frame = 0
            punch = False

        if angle > angle2:
            angle2 = angle
            
        if 152 >= angle > -72 :
            angle += rot
            angle2 += rot2
            
        elif angle <= -72:
            if rot < 0:
                rot = 0
                angle = angle
            else:
                angle += rot
        elif angle > 152:
            if rot > 0:
                rot = 0
                angle = angle
            else:
                angle += rot

        if angle2 >= 220 :
            if rot2 > 0:
                rot2 = 0
                angle2 = angle2                
            else:
                angle2 += rot2

        pygame.display.flip()
        pygame.display.update()

        clock.tick(100)        

boucle()
pygame.quit()

