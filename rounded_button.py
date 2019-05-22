import pygame,os,ctypes,time,random,sys,csv,random
from pygame import *

################### SCREEN SETUP ###################
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (6,28)
SM_CXSCREEN = 0
SM_CYSCREEN = 1
width_screen = ctypes.windll.user32.GetSystemMetrics(SM_CXSCREEN)
height_screen = ctypes.windll.user32.GetSystemMetrics(SM_CYSCREEN)
print ("Résolution écran : %d x %d" % (width_screen, height_screen))


x= 50
y = 50
height = 50
width = 200


def display_text(texte,positionx,positiony,police,taille,couleur):
    police=font.SysFont(police, taille, bold = True)
    texte=police.render(texte, 1, couleur)
    rectangle=texte.get_rect()
    rectangle.centerx = positionx
    rectangle.centery = positiony
    screen.blit(texte, rectangle)

def display_rounded_button(surface,rect,color,radius=0.4):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)
    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = Rect(rect)
    color        = Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = Surface(rect.size,SRCALPHA)

    circle       = Surface([min(rect.size)*3]*2,SRCALPHA)
    draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((300,300))
screen.fill(-1)
display_rounded_button(screen,(x,y,width,height),(200,20,20),0.5)
display_text("Button",x+width/2,y+height/2,"HELVETICA",20,(255,255,255))
pygame.display.flip()
while event.wait().type != QUIT: pass

