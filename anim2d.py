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

class Bonhomme():
    def __init__(self,liste_element, side = True):
        self.path = "bank\\image"
        
        self.side = side
        
        if side :        
            self.img_tete = pygame.image.load(self.path+"\\"+str(liste_element[0])+".png")    
            self.img_buste = pygame.image.load(self.path+"\\"+str(liste_element[1])+".png")    
            self.img_cuisse = pygame.image.load(self.path+"\\"+str(liste_element[2])+".png")    
            self.img_mollet = pygame.image.load(self.path+"\\"+str(liste_element[3])+".png")    
            self.img_pied = pygame.image.load(self.path+"\\"+str(liste_element[4])+".png")    
            self.img_bras = pygame.image.load(self.path+"\\"+str(liste_element[5])+".png")    
            self.img_av_bras = pygame.image.load(self.path+"\\"+str(liste_element[6])+".png")    
            self.img_main = pygame.image.load(self.path+"\\"+str(liste_element[7])+".png") 
            
        else : 
            self.img_tete = pygame.transform.flip(pygame.image.load(self.path+"\\"+str(liste_element[0])+".png"), True, False)    
            self.img_buste = pygame.transform.flip(pygame.image.load(self.path+"\\"+str(liste_element[1])+".png"), True, False)    
            self.img_cuisse = pygame.transform.flip(pygame.image.load(self.path+"\\"+str(liste_element[2])+".png"), True, False)    
            self.img_mollet = pygame.transform.flip(pygame.image.load(self.path+"\\"+str(liste_element[3])+".png"), True, False)    
            self.img_pied = pygame.transform.flip(pygame.image.load(self.path+"\\"+str(liste_element[4])+".png"), True, False)    
            self.img_bras = pygame.transform.flip(pygame.image.load(self.path+"\\"+str(liste_element[5])+".png"), True, False)    
            self.img_av_bras = pygame.transform.flip(pygame.image.load(self.path+"\\"+str(liste_element[6])+".png"), True, False)    
            self.img_main = pygame.transform.flip(pygame.image.load(self.path+"\\"+str(liste_element[7])+".png"), True, False) 
        
        self.x = 375
        self.y = 460
        self.move_x = 0
        self.move_y = 0
        self.base = (self.x,self.y)
        
        self.gauche = pygame.key.key_code("LEFT")
        self.droite = pygame.key.key_code("RIGHT")
        
        self.pivot_tete = (50,140)
        self.pivot_buste = (50,175)
        self.pivot_cuisse = (40,18)
        self.pivot_mol = (0,18)
        self.pivot_pied = (32,-17)
        self.pivot_bras = (25, 18)
        self.pivot_avbras = (10,18)
        self.pivot_main = (15,-15)

        self.buste = Image(self.img_buste,self.base,self.pivot_buste)
        self.buste.blitRotate(screen, self.buste.angle)
        self.tete = Image(self.img_tete,self.buste,self.pivot_tete, attached = True)        
        self.tete.blitRotate(screen, self.tete.angle)

        self.cuisse_d = Image(self.img_cuisse,self.buste,self.pivot_cuisse, attached = True, down = False)
        self.cuisse_d.blitRotate(screen, self.cuisse_d.angle)
        self.mollet_d = Image(self.img_mollet,self.cuisse_d,self.pivot_mol,attached=True)
        self.mollet_d.blitRotate(screen,self.mollet_d.angle)
        self.pied_d = Image(self.img_pied,self.mollet_d,self.pivot_pied,attached=True)
        self.pied_d.blitRotate(screen,self.pied_d.angle)

        self.cuisse_g = Image(self.img_cuisse,self.buste,self.pivot_cuisse, attached = True, down = False)
        self.cuisse_g.blitRotate(screen, self.cuisse_g.angle)
        self.mollet_g = Image(self.img_mollet,self.cuisse_g,self.pivot_mol,attached=True)
        self.mollet_g.blitRotate(screen,self.mollet_g.angle)
        self.pied_g = Image(self.img_pied,self.mollet_g,self.pivot_pied,attached=True)
        self.pied_g.blitRotate(screen,self.pied_g.angle)

        self.bras_d = Image(self.img_bras,self.buste,self.pivot_bras,attached=True)
        self.bras_d.blitRotate(screen,self.bras_d.angle)
        self.av_bras_d = Image(self.img_av_bras,self.bras_d,self.pivot_avbras,attached=True)
        self.av_bras_d.blitRotate(screen,self.av_bras_d.angle)
        self.main_d = Image(self.img_main,self.av_bras_d,self.pivot_main,attached=True)
        self.main_d.blitRotate(screen,self.main_d.angle)

        self.bras_g = Image(self.img_bras,self.buste,self.pivot_bras,attached=True)
        self.bras_g.blitRotate(screen,self.bras_g.angle)
        self.av_bras_g = Image(self.img_av_bras,self.bras_g,self.pivot_avbras,attached=True)
        self.av_bras_g.blitRotate(screen,self.av_bras_g.angle)
        self.main_g = Image(self.img_main,self.av_bras_g,self.pivot_main,attached=True)
        self.main_g.blitRotate(screen,self.main_g.angle)
        
        self.liste_membre = [self.buste,self.tete,self.bras_d,self.bras_g,self.av_bras_d,
                             self.av_bras_g,self.main_d,self.main_g,self.cuisse_d,
                             self.cuisse_g,self.mollet_d,self.mollet_g,self.pied_d,self.pied_g]


    def check_angle(self):
        
        if self.bras_d.angle > self.av_bras_d.angle :
            self.av_bras_d.angle = self.bras_d.angle
        if self.av_bras_d.angle > self.main_d.angle :
            self.main_d.angle = self.av_bras_d.angle
            
        if self.bras_g.angle > self.av_bras_g.angle :
            self.av_bras_g.angle = self.bras_g.angle
        if self.av_bras_g.angle > self.main_g.angle :
            self.main_g.angle = self.av_bras_g.angle

        if self.cuisse_d.angle < self.mollet_d.angle :
            self.mollet_d.angle = self.cuisse_d.angle
        if self.mollet_d.angle + 45 < self.pied_d.angle :
            self.pied_d.angle = self.mollet_d.angle
        
        if self.cuisse_g.angle < self.mollet_g.angle :
            self.mollet_g.angle = self.cuisse_g.angle
        if self.mollet_g.angle + 45 < self.pied_g.angle :
            self.pied_g.angle = self.mollet_g.angle
            
    def Move(self,evenement,frame):           
          # Condition becomes true when keyboard is pressed   
        if evenement.type == pygame.KEYDOWN:
       
            # if e.key == self.saut :
            #     self.jump = True
                
            # if e.key == self.descend :
            #     self.fall = True
                
            if evenement.key == self.gauche :
                self.move_x = -5
                
            if evenement.key == self.droite :
                self.move_x = 5
                                
        if evenement.type == pygame.KEYUP:
       
            # if e.key == self.saut :
            #     self.jump = False
                
            # if e.key == self.descend :
            #     self.fall = False
                
            if evenement.key == self.gauche :
                self.move_x = 0
    
            if evenement.key == self.droite :
                self.move_x = 0
                
        return(self.move_x,self.move_y)
    
    def Deplacement(self, frame, val):
        
        if val :
    
            self.tete.angle = self.tete.anim_sin(frame, 1, 5)
            
            self.cuisse_d.angle = self.cuisse_d.anim_sin(frame, -5, 5, h = 10) - 15
            self.mollet_d.angle = self.mollet_d.anim_sin(frame, -5, 5, h = 20) - 35 
            self.pied_d.angle = self.pied_d.anim_sin(frame, -5, 5, h = 20) - 10
    
            self.cuisse_g.angle = self.cuisse_g.anim_sin(frame, 5, 5) + 30
            self.mollet_g.angle = self.mollet_g.anim_sin(frame, 5, 5, h = -10)
            self.pied_g.angle = self.pied_g.anim_sin(frame, 5, 5, h = -10)
    
            self.bras_d.angle = self.bras_d.anim_sin(frame, 2, 5) + 35
            self.av_bras_d.angle = self.av_bras_d.anim_sin(frame, 1, 5) + 160
            self.main_d.angle = self.main_d.anim_sin(frame, 1, 5) + 160
    
            self.bras_g.angle = self.bras_d.anim_sin(frame, 2, 5) + 80
            self.av_bras_g.angle = self.av_bras_g.anim_sin(frame, 1, 5) + 150
            self.main_g.angle = self.main_g.anim_sin(frame, 1, 5) + 150
            
        else :
            
            self.Garde()
            
        self.check_angle()
        
    def Collision(self,objet,frame):
        
        if abs(objet.image_rect.left - self.main_g.image_rect.right) < 10:
            objet.angle = objet.anim_parabole(frame + 1, 45, 0)
            objet.image_rect.left = self.main_g.image_rect.right + 10
        if abs(objet.image_rect.left - self.main_d.image_rect.right) < 10:
            objet.angle = objet.anim_parabole(frame, 45, 0)
        if abs(objet.image_rect.left - self.pied_g.image_rect.right) < 10:
            objet.angle = objet.anim_parabole(frame, 45, 0)
        if abs(objet.image_rect.left - self.pied_d.image_rect.right) < 10:
            objet.angle = objet.anim_parabole(frame, 45, 0)
            
        else:
            objet.angle = 0
            
        objet.blitRotate(screen, objet.angle)
            
    def Update(self,screen,objet,frame):

        self.tete = Image(self.img_tete,self.buste,self.pivot_tete, attached = True, angle = self.tete.angle)        
        self.tete.blitRotate(screen, self.tete.angle)

        self.bras_g = Image(self.img_bras,self.buste,self.pivot_bras,attached=True, angle = self.bras_g.angle)
        self.bras_g.blitRotate(screen,self.bras_g.angle)
        self.av_bras_g = Image(self.img_av_bras,self.bras_g,self.pivot_avbras,attached=True, angle = self.av_bras_g.angle)
        self.av_bras_g.blitRotate(screen,self.av_bras_g.angle)
        self.main_g = Image(self.img_main,self.av_bras_g,self.pivot_main,attached=True, angle = self.main_g.angle)
        self.main_g.blitRotate(screen,self.main_g.angle)

        self.cuisse_g = Image(self.img_cuisse,self.buste,self.pivot_cuisse, attached = True, down = False, angle = self.cuisse_g.angle)
        self.cuisse_g.blitRotate(screen, self.cuisse_g.angle)
        self.mollet_g = Image(self.img_mollet,self.cuisse_g,self.pivot_mol,attached=True, angle = self.mollet_g.angle)
        self.mollet_g.blitRotate(screen,self.mollet_g.angle)
        self.pied_g = Image(self.img_pied,self.mollet_g,self.pivot_pied,attached=True, angle = self.pied_g.angle)
        self.pied_g.blitRotate(screen,self.pied_g.angle)
        
        self.buste = Image(self.img_buste,self.base,self.pivot_buste, angle = self.buste.angle)
        self.buste.blitRotate(screen, self.buste.angle)
        
        self.cuisse_d = Image(self.img_cuisse,self.buste,self.pivot_cuisse, attached = True, down = False, angle = self.cuisse_d.angle)
        self.cuisse_d.blitRotate(screen, self.cuisse_d.angle)
        self.mollet_d = Image(self.img_mollet,self.cuisse_d,self.pivot_mol,attached=True, angle = self.mollet_d.angle)
        self.mollet_d.blitRotate(screen,self.mollet_d.angle)
        self.pied_d = Image(self.img_pied,self.mollet_d,self.pivot_pied,attached=True, angle = self.pied_d.angle)
        self.pied_d.blitRotate(screen,self.pied_d.angle)

        self.bras_d = Image(self.img_bras,self.buste,self.pivot_bras,attached=True, angle = self.bras_d.angle)
        self.bras_d.blitRotate(screen,self.bras_d.angle)
        self.av_bras_d = Image(self.img_av_bras,self.bras_d,self.pivot_avbras,attached=True, angle = self.av_bras_d.angle)
        self.av_bras_d.blitRotate(screen,self.av_bras_d.angle)
        self.main_d = Image(self.img_main,self.av_bras_d,self.pivot_main,attached=True, angle = self.main_d.angle)
        self.main_d.blitRotate(screen,self.main_d.angle)
        
        self.Collision(objet,frame)
        
        self.check_angle()
        
    def Garde(self):
        if self.side :
            self.buste.angle = 0
                
            self.bras_d.angle = 35
            self.av_bras_d.angle = 160
            self.main_d.angle = 160
    
            self.bras_g.angle = 80
            self.av_bras_g.angle = 150
            self.main_g.angle = 150
    
            self.cuisse_g.angle = 20
            self.mollet_g.angle = 0
            self.pied_g.angle = 0
    
            self.cuisse_d.angle = -10
            self.mollet_d.angle = -20
            self.pied_d.angle = -2
            
        else: 
            self.buste.angle = 0
                
            self.bras_d.angle = -35
            self.av_bras_d.angle = -160
            self.main_d.angle = -160
    
            self.bras_g.angle = -80
            self.av_bras_g.angle = -150
            self.main_g.angle = -150
    
            self.cuisse_g.angle = -20
            self.mollet_g.angle = 0
            self.pied_g.angle = 0
    
            self.cuisse_d.angle = 10
            self.mollet_d.angle = 20
            self.pied_d.angle = 2
            
        self.check_angle()       
        
                
    def Walk(self,frame,val):

        if val:
            self.tete.angle = self.tete.anim_sin(frame, 5, 20)
            
            self.cuisse_d.angle = self.cuisse_d.anim_sin(frame, 30, 20)
            self.mollet_d.angle = self.mollet_d.anim_sin(frame, 60, 20, h = -6)
            self.pied_d.angle = self.pied_d.anim_sin(frame, 60, 20, h = -6)
    
            self.cuisse_g.angle = self.cuisse_g.anim_sin(frame, -30, 20)
            self.mollet_g.angle = self.mollet_g.anim_sin(frame, -60, 20, h = -6)
            self.pied_g.angle = self.pied_g.anim_sin(frame, -60, 20, h = -6)
    
            self.bras_d.angle = self.bras_d.anim_sin(frame, 10, 20)
            self.av_bras_d.angle = self.av_bras_d.anim_sin(frame, 45, 20, h = -6)
            self.main_d.angle = self.main_d.anim_sin(frame, 45, 20, h = -6)
    
            self.bras_g.angle = self.bras_g.anim_sin(frame, -10, 20)
            self.av_bras_g.angle = self.av_bras_g.anim_sin(frame, -45, 20, h = -6)
            self.main_g.angle = self.main_g.anim_sin(frame, -45, 20, h = -6)
        else:
            self.Garde()

        self.check_angle()
        
    def Punch(self, frame):
        if frame < 20 :
            self.buste.angle = self.buste.anim_parabole(frame, 0, -5)
            
            self.bras_d.angle = self.bras_d.anim_parabole(frame, 35, 90)
            self.av_bras_d.angle = self.av_bras_d.anim_parabole(frame, 160, 100)
            self.main_d.angle = self.main_d.anim_parabole(frame, 160, 100)

            self.bras_g.angle = 80
            self.av_bras_g.angle = self.av_bras_g.anim_parabole(frame, 150, 180)
            self.main_g.angle = self.main_g.anim_parabole(frame, 150, 180)

            self.cuisse_g.angle = self.cuisse_g.anim_parabole(frame, 20, 30)
            self.mollet_g.angle = self.mollet_g.anim_parabole(frame, 0, -10)
            self.pied_g.angle = self.pied_d.anim_parabole(frame, 0, -10)

            self.cuisse_d.angle = -10
            self.mollet_d.angle = -20
            self.pied_d.angle = self.pied_d.anim_parabole(frame, -2, 0)
            
            val = True
            
        else:
            frame = 0
            val = False
            self.Garde()
            
        return(frame,val)
            
        self.check_angle()

    def Gauche(self, frame):
        if frame < 20 :
            self.buste.angle = self.buste.anim_parabole(frame, 0, -5)
            
            self.bras_g.angle = self.bras_g.anim_parabole(frame, 75, 105)
            self.av_bras_g.angle = self.av_bras_g.anim_parabole(frame, 150, 100)
            self.main_g.angle = self.main_g.anim_parabole(frame, 150, 100)

            self.bras_d.angle = self.bras_d.anim_parabole(frame, 35, 50)
            self.av_bras_d.angle = 160
            self.main_d.angle = 160

            self.cuisse_g.angle = self.cuisse_g.anim_parabole(frame, 20, 30)
            self.mollet_g.angle = self.mollet_g.anim_parabole(frame, 0, -10)
            self.pied_g.angle = self.pied_g.anim_parabole(frame, 0, -2)

            self.cuisse_d.angle = -10
            self.mollet_d.angle = -20
            self.pied_d.angle = self.pied_d.anim_parabole(frame, -2, 0)
            
            val = True
            
        else:
            frame = 0
            val = False
            self.Garde()
            
        return(frame,val)
            
        self.check_angle()

    def Upercut_D(self, frame):
        if frame < 20 :
            self.tete.angle = self.tete.anim_parabole(frame, 0, -8)
            
            self.buste.angle = self.buste.anim_parabole(frame, 0, -5)
            
            self.bras_d.angle = self.bras_d.anim_sin(frame, -50, 4) + 50
            self.av_bras_d.angle = self.av_bras_d.anim_sin(frame, -50, 10) + 160
            self.main_d.angle = self.main_d.anim_sin(frame, -50, 10) + 160

            self.bras_g.angle = 80
            self.av_bras_g.angle = self.av_bras_g.anim_parabole(frame, 150, 180)
            self.main_g.angle = self.main_g.anim_parabole(frame, 150, 180)

            self.cuisse_g.angle = 20
            self.mollet_g.angle = 0
            self.pied_g.angle = 0

            self.cuisse_d.angle = self.cuisse_d.anim_parabole(frame, -10, 0)
            self.mollet_d.angle = self.mollet_d.anim_parabole(frame, -20, -30)
            self.pied_d.angle = -2
            
            val = True
            
        else:
            frame = 0
            val = False
            self.Garde()
            
        return(frame,val)
            
        self.check_angle()

    def Upercut_G(self, frame):
        if frame < 20 :
            self.tete.angle = self.tete.anim_parabole(frame, 0, -8)

            self.buste.angle = self.buste.anim_parabole(frame, 0, -5)
            
            self.bras_d.angle = self.bras_d.anim_parabole(frame, 35, 50)
            self.av_bras_d.angle = 160
            self.main_d.angle = 160

            self.bras_g.angle = self.bras_g.anim_sin(frame, -80, 5) + 80
            self.av_bras_g.angle = self.av_bras_g.anim_sin(frame, -50, 6) + 150
            self.main_g.angle = self.main_g.anim_sin(frame, -50, 6) + 150

            self.cuisse_g.angle = 20
            self.mollet_g.angle = 0
            self.pied_g.angle = 0

            self.cuisse_d.angle = self.cuisse_d.anim_parabole(frame, -10, 0)
            self.mollet_d.angle = self.mollet_d.anim_parabole(frame, -20, -30)
            self.pied_d.angle = -2
            
            val = True
            
        else:
            frame = 0
            val = False
            self.Garde()
            
        return(frame,val)
            
        self.check_angle()
        
    def Chasse_G(self, frame):
        if frame < 30 :
            self.tete.angle = self.tete.anim_parabole(frame, 0, -8, halframe = 15)

            self.buste.angle = self.buste.anim_parabole(frame, 0, 10, halframe = 15)
            
            self.bras_d.angle = self.bras_d.anim_parabole(frame, 35, 50, halframe = 15)
            self.av_bras_d.angle = 160
            self.main_d.angle = 160
    
            self.bras_g.angle = 80
            self.av_bras_g.angle = self.av_bras_g.anim_parabole(frame, 150, 180, halframe = 15)
            self.main_g.angle = self.main_g.anim_parabole(frame, 150, 180, halframe = 15)

            self.cuisse_g.angle = self.cuisse_g.anim_parabole(frame, 20, 110, halframe = 15)
            if frame < 12:
                self.mollet_g.angle = 0
                self.pied_g.angle = 0
            else:
                self.mollet_g.angle = self.mollet_g.anim_parabole(frame - 12, 0, 75, halframe = 9)
                self.pied_g.angle = self.pied_g.anim_parabole(frame - 12, 0, 75, halframe = 9)

            self.cuisse_d.angle = self.cuisse_d.anim_parabole(frame, -10, 0, halframe = 15)
            self.mollet_d.angle = self.mollet_d.anim_parabole(frame, -20, -30, halframe = 15)
            self.pied_d.angle = -2
            
            val = True
            
        else:
            frame = 0
            val = False
            self.Garde()
            
        return(frame,val)
            
        self.check_angle()

    def Chasse_D(self, frame):
        if frame < 30 :
            self.tete.angle = self.tete.anim_parabole(frame, 0, -8, halframe = 15)

            self.buste.angle = self.buste.anim_parabole(frame, 0, 10, halframe = 15)
            
            self.bras_d.angle = self.bras_d.anim_parabole(frame, 35, 50, halframe = 15)
            self.av_bras_d.angle = 160
            self.main_d.angle = 160
    
            self.bras_g.angle = 80
            self.av_bras_g.angle = self.av_bras_g.anim_parabole(frame, 150, 180, halframe = 15)
            self.main_g.angle = self.main_g.anim_parabole(frame, 150, 180, halframe = 15)

            self.cuisse_d.angle = self.cuisse_d.anim_parabole(frame, 20, 110, halframe = 15)
            if frame < 12:
                self.mollet_d.angle = 0
                self.pied_d.angle = 0
            else:
                self.mollet_d.angle = self.mollet_d.anim_parabole(frame - 12, 0, 75, halframe = 9)
                self.pied_d.angle = self.pied_d.anim_parabole(frame - 12, 0, 75, halframe = 9)

            self.cuisse_g.angle = self.cuisse_g.anim_parabole(frame, 20, -10, halframe = 15)
            self.mollet_g.angle = self.mollet_g.anim_parabole(frame, 0, -35, halframe = 15)
            self.pied_g.angle = self.pied_g.anim_parabole(frame, 0, -5, halframe = 15)
            
            val = True
            
        else:
            frame = 0
            val = False
            self.Garde()
            
        return(frame,val)
            
        self.check_angle()

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
        
    def update(self,surf,objet):
        print(abs(objet.image_rect.left - self.image_rect.right))
        # self.__init__(self.image, self.pos, self.originPos, self.attached, self.down, self.angle)
        # self.blitRotate(surf, self.angle)
        
    def update_pos(self,pos):
        if not self.attached:
            self.pos = pos
        else:
            if self.down:
                self.pos = pos.rotated_image_rect.center[0]-pos.rotated_offset[0],pos.rotated_image_rect.center[1]-pos.rotated_offset[1]
            elif not self.down:
                self.pos = pos.rotated_offset[0]-pos.rotated_image_rect.center[0],pos.rotated_offset[1]-pos.rotated_image_rect.center[1]
            
        return(self.pos)

    def anim_parabole(self,frame, angle_max, angle_min, halframe = 10):
        ##FONCTION PARABOLE MOUVEMENT
        # angle = (frame-(max_frame/2))?? * ((angle_max-angle_min)/((frame-(max_frame/2))?? -angle_min)+angle_min
        
        self.angle = (frame - halframe)**2 * ((angle_max-angle_min)/((halframe)**2)) + angle_min
        
        return(self.angle)
    
    def anim_sin(self,frame,angle_cote,per,h=0):
        
        angle = angle_cote*(math.sin((1/per)*(frame+h)))
        
        return(angle)
    
        
def boucle():
    gameExit=False
    
    pb_img = pygame.image.load("bank\\image\\punching_ball.png") 
    pivot_pb = (25,-100)
    pb = Image(pb_img,(575,50),pivot_pb)
    
    frame = 0
    
    pygame.init()
    size = (800,800)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    
    pb.blitRotate(screen, 0)
    
    liste_element = [
        "tete",
        "torse",
        "cuisse",
        "mollet",
        "shoe",
        "bras",
        "avant-bras",
        "main"
        ]

    Gus = Bonhomme(liste_element)
    

    clock = pygame.time.Clock()
    
    walk = False
    bouge = False
    punch = False
    gauche = False
    upercut_d = False
    upercut_g = False
    chasse_g = False
    chasse_d = False
    
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            Gus.move_x, Gus.move_y = Gus.Move(event,frame)
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_z:
                    # frame = 0
                    walk = True

                if event.key == pygame.K_p:
                    frame = 0
                    punch = True
                    gauche = False
                    upercut_d = False
                    upercut_g = False
                    chasse_g = False
                    chasse_d = False

                if event.key == pygame.K_a:
                    frame = 0
                    gauche = True
                    punch = False
                    upercut_d = False
                    upercut_g = False
                    chasse_g = False
                    chasse_d = False

                if event.key == pygame.K_l:
                    frame = 0
                    gauche = False
                    punch = False
                    upercut_d = True
                    upercut_g = False
                    chasse_g = False
                    chasse_d = False

                if event.key == pygame.K_q:
                    frame = 0
                    gauche = False
                    punch = False
                    upercut_d = False
                    upercut_g = True
                    chasse_g = False
                    chasse_d = False

                if event.key == pygame.K_s:
                    frame = 0
                    gauche = False
                    punch = False
                    upercut_d = False
                    upercut_g = False
                    chasse_g = True
                    chasse_d = False

                if event.key == pygame.K_k:
                    frame = 0
                    gauche = False
                    punch = False
                    upercut_d = False
                    upercut_g = False
                    chasse_g = False
                    chasse_d = True
                    
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_z:
                    # frame = 0
                    walk = False

                # if event.key == pygame.K_a:
                #     punch = False

        if Gus.move_x != 0:
            bouge = True
        else:
            bouge = False
            
        Gus.x += Gus.move_x
        Gus.y += Gus.move_y
        
        Gus.base = (Gus.x,Gus.y)
                    
        screen.blit(fond,(0,0))
        
        Gus.Walk(frame, walk)
        Gus.Deplacement(frame, bouge)
            
        if punch :
            frame,punch = Gus.Punch(frame)

        if gauche :
            frame,gauche = Gus.Gauche(frame)

        if upercut_d :
            frame,upercut_d = Gus.Upercut_D(frame)

        if upercut_g :
            frame,upercut_g = Gus.Upercut_G(frame)

        if chasse_g :
            frame,chasse_g = Gus.Chasse_G(frame)

        if chasse_d :
            frame,chasse_d = Gus.Chasse_D(frame)

        Gus.Update(screen,pb,frame)
        
        
                    
        pb.blitRotate(screen, pb.angle)
        
        frame += 1
        
        pygame.display.flip()
        pygame.display.update()

        clock.tick(100)        

boucle()
pygame.quit()

