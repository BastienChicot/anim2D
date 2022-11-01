# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:23:43 2022

@author: bchicot
"""

import math
import pygame

fond = pygame.image.load('bank/image/fond.png')
pygame.init()

screen = pygame.display.set_mode((800, 800))

class Human():
    def __init__(self,liste_image):
        self.buste = liste_image[0]
        self.cuisse = liste_image[1]
        self.mollet = liste_image[2]
        self.bras = liste_image[3]
        self.avant_bras = liste_image[4]

class Image():
    def __init__(self,image,pos,originPos, attached = False, down = True , angle = 0):
        self.angle = angle
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
        
    def update(self,surf):
        self.__init__(self.image, self.pos, self.originPos, self.attached, self.down, self.angle)
        self.blitRotate(surf, self.angle)
        
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
        
        self.angle = (frame - 10)**2 * ((angle_max-angle_min)/((10)**2)) + angle_min
        
        return(self.angle)
    
    def anim_sin(self,frame,angle_cote,per,h=0):
        
        angle = angle_cote*(math.sin((1/per)*(frame+h)))
        
        return(angle)
    
        
def boucle():
    gameExit=False
    
    frame = 0
    
    pygame.init()
    size = (800,800)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    tete_img = pygame.image.load('bank/image/tete.png')    
    torse_image = pygame.image.load('bank/image/torse.png')
    cuisse_img = pygame.image.load('bank/image/cuisse.png')
    mollet_img = pygame.image.load('bank/image/mollet.png')
    image = pygame.image.load('bank/image/bras.png')
    image2 = pygame.image.load("bank/image/avant-bras.png")
    main = pygame.image.load('bank/image/main.png')
    pied = pygame.image.load('bank/image/shoe.png')
    
    pivot0 = (50,175)
    pivot = (25, 18)
    pivot2 = (10,18)
    pivot_nul = (40,18)
    pivot_mol = (0,18)
    pivot_main = (15,-15)
    pivot_pied = (32,-17)
    pivot_tete = (50,140)

    torse = Image(torse_image,(375,460),pivot0)
    torse.blitRotate(screen, torse.angle)

    tete = Image(tete_img,torse,pivot_tete, attached = True)
    tete.blitRotate(screen, tete.angle)
    
    cuisse = Image(cuisse_img,torse,pivot_nul, attached = True, down = False)
    cuisse.blitRotate(screen, cuisse.angle)

    mollet = Image(mollet_img,cuisse,pivot_mol,attached=True)
    mollet.blitRotate(screen,mollet.angle)

    pied_d = Image(pied,mollet,pivot_pied,attached=True)
    pied_d.blitRotate(screen,pied_d.angle)
    
    cuisse2 = Image(cuisse_img,torse,pivot_nul, attached = True, down = False)
    cuisse2.blitRotate(screen, cuisse2.angle)

    mollet2 = Image(mollet_img,cuisse2,pivot_mol,attached=True)
    mollet2.blitRotate(screen,mollet2.angle)

    pied_g = Image(pied,mollet2,pivot_pied,attached=True)
    pied_g.blitRotate(screen,pied_g.angle)
        
    img = Image(image,torse,pivot,attached=True)
    img.blitRotate(screen,img.angle)
        
    img2 = Image(image2,img,pivot2,attached=True)
    img2.blitRotate(screen,img2.angle)

    main_d = Image(main,img2,pivot_main,attached=True)
    main_d.blitRotate(screen,main_d.angle)
    
    bras_g = Image(image,torse,pivot,attached=True)
    bras_g.blitRotate(screen,bras_g.angle)
        
    av_bras = Image(image2,bras_g,pivot2,attached=True)
    av_bras.blitRotate(screen,av_bras.angle)

    main_g = Image(main,av_bras,pivot_main,attached=True)
    main_g.blitRotate(screen,main_g.angle)

    clock = pygame.time.Clock()
    
    walk = False
    
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_z:
                    frame = 0
                    walk = True


                    
        screen.blit(fond,(0,0))

        pos0 = torse.originPos
        
        if walk :
            tete.angle = tete.anim_sin(frame, 5, 20)
            
            cuisse.angle = cuisse.anim_sin(frame, 30, 20)
            mollet.angle = mollet.anim_sin(frame, 60, 20, h = -6)
            pied_d.angle = pied_d.anim_sin(frame, 60, 20, h = -6)
            cuisse2.angle = cuisse2.anim_sin(frame, -30, 20)
            mollet2.angle = mollet2.anim_sin(frame, -60, 20, h = 6)
            pied_g.angle = pied_g.anim_sin(frame, -60, 20, h = 6)

            img.angle = img.anim_sin(frame, 10, 20)
            img2.angle = img2.anim_sin(frame, 45, 20, h = -6)
            main_d.angle = main_d.anim_sin(frame, 45, 20, h = -6)
            bras_g.angle = bras_g.anim_sin(frame, -10, 20)
            av_bras.angle = av_bras.anim_sin(frame, -45, 20, h = -6)
            main_g.angle = main_g.anim_sin(frame, -45, 20, h = -6)
            
        if img.angle > img2.angle :
            img2.angle = img.angle
        if img2.angle > main_d.angle :
            main_d.angle = img2.angle
            
        if bras_g.angle > av_bras.angle :
            av_bras.angle = bras_g.angle
        if av_bras.angle > main_g.angle :
            main_g.angle = av_bras.angle

        if cuisse.angle < mollet.angle :
            mollet.angle = cuisse.angle
        if mollet.angle < pied_d.angle :
            pied_d.angle = mollet.angle

        if cuisse2.angle < mollet2.angle :
            mollet2.angle = cuisse2.angle
        if mollet2.angle < pied_g.angle :
            pied_g.angle = mollet2.angle
            
        pos = img.pos
        pos2 = img2.pos
        pos3 = cuisse.pos
        pos4 = mollet.pos

        tete = Image(tete_img,torse,pivot_tete, attached = True, angle=tete.angle)
        tete.blitRotate(screen, tete.angle)
        
        bras_g = Image(image,torse,bras_g.originPos,attached=True, angle=bras_g.angle)
        bras_g.blitRotate(screen,bras_g.angle)
            
        av_bras = Image(image2,bras_g,av_bras.originPos,attached=True, angle=av_bras.angle)
        av_bras.blitRotate(screen,av_bras.angle)

        main_g = Image(main,av_bras,pivot_main,attached=True, angle=main_g.angle)
        main_g.blitRotate(screen,main_g.angle)
        
        cuisse = Image(cuisse_img,torse,cuisse.originPos, attached = True, down = False, angle=cuisse.angle)
        cuisse.blitRotate(screen, cuisse.angle)
      
        cuisse2 = Image(cuisse_img,torse,cuisse2.originPos, attached = True, down = False, angle=cuisse2.angle)
        cuisse2.blitRotate(screen, cuisse2.angle)
                
        torse.blitRotate(screen, torse.angle)

        mollet = Image(mollet_img,cuisse,mollet.originPos,attached=True, angle=mollet.angle)
        mollet.blitRotate(screen,mollet.angle)
        
        pied_d = Image(pied,mollet,pivot_pied,attached=True, angle=pied_d.angle)
        pied_d.blitRotate(screen,pied_d.angle)
        
        mollet2 = Image(mollet_img,cuisse2,mollet2.originPos,attached=True, angle=mollet2.angle)
        mollet2.blitRotate(screen,mollet2.angle)

        pied_g = Image(pied,mollet2,pivot_pied,attached=True, angle=pied_g.angle)
        pied_g.blitRotate(screen,pied_g.angle)
        
        img = Image(image,torse,img.originPos,attached=True, angle = img.angle)
        img.blitRotate(screen,img.angle)

        img2 = Image(image2,img,img2.originPos,attached=True, angle=img2.angle)
        img2.blitRotate(screen,img2.angle)

        main_d = Image(main,img2,pivot_main,attached=True, angle=main_d.angle)
        main_d.blitRotate(screen,main_d.angle)

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

        # if punch and frame <= 20 :
        #     base = torse.anim_punch(frame, 0, -5)
        #     angle = img.anim_punch(frame, 60, 90)
        #     angle2 = img2.anim_punch(frame, 160, 100)
        # else:
        #     frame = 0



        print(cuisse.angle, mollet.angle)

        
        pygame.display.flip()
        pygame.display.update()

        clock.tick(100)        

boucle()
pygame.quit()

