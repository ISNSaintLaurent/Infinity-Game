"""
Licence Musique
"""
##### Titre:  Cascade 
###   Auteur: Kubbi 
##    Source: http://www.kubbimusic.com/
###    Licence: https://creativecommons.org/licenses/by-sa/3.0/deed.fr
####   Telechargement (8MB): http://www.auboutdufil.com/index.php?id=485

import  pygame
import time
from random import*

pygame.init()

noir = (8,8,8) 
blanc = (255,255,255)
fond = (253,237,176)
blue = (135,206,250)
blue2 = (105,176,220)
red = (254,29,83)
red2 = (220,0,49)

surfaceW = 1500
surfaceH = 1000
persoW = persoH = 50
murW = 100
murH = 1000
score = 0

fenetre = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("Infinity Game")

IronMenu = pygame.transform.scale(pygame.image.load("IronMenu.png"),(300,300)).convert()
CaptainMenu = pygame.transform.scale(pygame.image.load("CaptainMenu.png"),(300,300)).convert()
FruitMenu = pygame.transform.scale(pygame.image.load("FruitMenu.png"),(300,300)).convert_alpha()

IronMenu2 = pygame.transform.scale(pygame.image.load("IronMenu2.png"),(300,300)).convert()
CaptainMenu2 = pygame.transform.scale(pygame.image.load("CaptainMenu2.png"),(300,300)).convert()
FruitMenu2 = pygame.transform.scale(pygame.image.load("FruitMenu2.png"),(300,300)).convert()

InfoMenu = pygame.transform.scale(pygame.image.load("infos.png"),(1500,886)).convert()

SonOff = pygame.transform.scale(pygame.image.load("sonoff.png"),(45,45)).convert()
SonOff2 = pygame.transform.scale(pygame.image.load("sonoff2.png"),(45,45)).convert()
SonOn = pygame.transform.scale(pygame.image.load("sonon.png"),(60,45)).convert()
SonOn2 = pygame.transform.scale(pygame.image.load("sonon2.png"),(60,45)).convert()

calibri_font = pygame.font.Font("PixelFont.TTF",40)
calibri_menu = pygame.font.Font("PixelFont.TTF",200)
pygame.mixer.music.load("KubbiCascade.wav")

theme = 1
bestscore = 0

"""
CLASSES
"""

class Player:
    def __init__(self):
        if theme == 1 :
            self.img = pygame.image.load("iron.png")
            self.img = pygame.transform.scale(self.img,(persoW,persoH)).convert()
        if theme == 2 :
            self.img = pygame.image.load("captain.png")
            self.img = pygame.transform.scale(self.img,(persoW,persoH)).convert()
        if theme == 3 :
            self.img = pygame.image.load("fruit.png")
            self.img = pygame.transform.scale(self.img,(persoW,persoH)).convert()
        self.rect = self.img.get_rect()
        self.y=475
        self.x=100
        #joue = 1

    def update (self, saut):
        self.position = (self.x, self.y)
        self.rect = pygame.Rect(self.position, (persoW,persoH))
        fenetre.blit(self.img, self.position)
        
        if saut > 0:
            self.y -= ((saut/6)^(1/2))
        if saut < 0:
            self.y += ((-saut/9)^(1/2))

class Mur:
    def __init__(self):
        if theme == 1:
            self.img_mur = pygame.image.load("muriron.png")
            self.img_mur = pygame.transform.scale(self.img_mur,(murW,murH)).convert()
        if theme == 2:
            self.img_mur = pygame.image.load("murcaptain.png")
            self.img_mur = pygame.transform.scale(self.img_mur,(murW,murH)).convert()
        if theme == 3:
            self.img_mur = pygame.image.load("murfruit.png")
            self.img_mur = pygame.transform.scale(self.img_mur,(murW,murH)).convert()
        
        self.rect = self.img_mur.get_rect()
        self.x = surfaceW - murW -50
        self.y = randint(-850,-450)
    def update(self):
        global score
        global bestscore

        vitesse = 6

        self.position = (self.x, self.y)
        self.position2 = (self.x, self.y + 1000 + 300)
        self.rect = pygame.Rect(self.position,(murW,murH))
        self.rect2 = pygame.Rect(self.position2,(murW,murH))
        fenetre.blit(self.img_mur, self.position)
        fenetre.blit(self.img_mur, self.position2)
        
        if self.x < -100 :
            self.x = surfaceW
            self.y = randint(-850,-450)
        if -3<=self.x<=2 :
            score += 1
            if bestscore < score :
                bestscore = score
        self.x -= vitesse

"""
FONCTIONS
"""
 
def gameOver():
    print ("perdu")
    pygame.display.update()
    time.sleep(0.2)

    while menu() == None :
        pygame.time.wait(16)    
    main() 

def menu():
    global score
    rect_pointeur = pygame.Rect(pygame.mouse.get_pos(),(1,1))
    rect_jouer = pygame.Rect((170,125), (580,150))
    rect_skins = pygame.Rect((170,408), (1060,210))
    rect_infos = pygame.Rect((170,731), (555,150))
    rect_quit = pygame.Rect((50,25), (140,35))
    rect_son = pygame.Rect((1350,850),(60,45))
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_pointeur.colliderect(rect_jouer):
                return 1
            elif rect_pointeur.colliderect(rect_skins):
                while menu_skins() == None:
                    pygame.time.wait(16)   
            elif rect_pointeur.colliderect(rect_infos):
                while menu_info() == None:
                    pygame.time.wait(16)
            elif rect_pointeur.colliderect(rect_son):
                pygame.mixer.music.set_volume(abs(pygame.mixer.music.get_volume()-1))
            elif rect_pointeur.colliderect(rect_quit):
                abientot()
                pygame.quit()
                quit()

    fenetre.fill(blanc)
    fenetre.blit(calibri_font.render("Quitter", True, red), (50, 30))
    fenetre.blit(calibri_font.render("Score precedent: "+ str(score), True, blue), (1063, 25))
    fenetre.blit(calibri_font.render("Meilleur score: "+ str(bestscore), True, blue), (1063, 75))
    fenetre.blit(calibri_menu.render("Infos", True, blue) , (170, 731))
    fenetre.blit(calibri_menu.render("Jouer", True, blue), (170, 115))
    fenetre.blit(calibri_menu.render("Apparence", True, blue), (170, 398))

    if pygame.mixer.music.get_volume() == 1:
        fenetre.blit(SonOn,(1350,850))
    else :
        fenetre.blit(SonOff,(1350,850)) 

    if rect_pointeur.colliderect(rect_jouer):
        fenetre.blit(calibri_menu.render("Jouer", True, blue2), (170, 115))
    elif rect_pointeur.colliderect(rect_skins):
        fenetre.blit(calibri_menu.render("Apparence", True, blue2) , (170, 398))
    elif rect_pointeur.colliderect(rect_infos):
        fenetre.blit(calibri_menu.render("Infos", True, blue2) , (170, 731))
    elif rect_pointeur.colliderect(rect_quit):
        fenetre.blit(calibri_font.render("Quitter (ne fais pas ca !)", True, red2) , (50, 30))
    elif rect_pointeur.colliderect(rect_son):
        if pygame.mixer.music.get_volume() == 1:
            fenetre.blit(SonOn2,(1350,850))
        else :
            fenetre.blit(SonOff2,(1350,850))
        
    pygame.display.flip()
    return  None 

def menu_skins():
    global theme
    global fond
    rect_pointeur = pygame.Rect(pygame.mouse.get_pos(),(1,1))
    rect_IronMenu = pygame.Rect((200,350), (300,300))
    rect_CaptainMenu = pygame.Rect((600,350), (300,300))
    rect_FruitMenu = pygame.Rect((1000,350), (300,300))
    rect_retour = pygame.Rect((50,25), (180,35))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            abientot()
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_pointeur.colliderect(rect_IronMenu):
                theme = 1
                fond = (253,237,176)
                return 1
            elif rect_pointeur.colliderect(rect_CaptainMenu):
                theme = 2
                fond = (214,234,248)
                return 1
            elif rect_pointeur.colliderect(rect_FruitMenu):
                theme = 3
                fond = (200,250,193)
                return 1
            elif rect_pointeur.colliderect(rect_retour):
                return 1

    fenetre.fill(blanc)
    fenetre.blit(IronMenu, (200,350))
    fenetre.blit(CaptainMenu, (600,350))
    fenetre.blit(FruitMenu, (1000,350))
    fenetre.blit(pygame.font.Font("PixelFont.TTF",60).render("Choisissez le theme avec lequel", True, blue), (240, 100))
    fenetre.blit(pygame.font.Font("PixelFont.TTF",60).render("vous souhaitez jouer :", True, blue), (350, 170))
    fenetre.blit(calibri_font.render("< Retour", True, blue), (50, 30))    

    if rect_pointeur.colliderect(rect_IronMenu):
        fenetre.blit(IronMenu2, (200,350))
    elif rect_pointeur.colliderect(rect_CaptainMenu):
        fenetre.blit(CaptainMenu2, (600,350))
    elif rect_pointeur.colliderect(rect_FruitMenu):
        fenetre.blit(FruitMenu2, (1000,350))
    elif rect_pointeur.colliderect(rect_retour):
        fenetre.blit(calibri_font.render("< Retour", True, blue2), (50, 30))

    pygame.display.flip()

    return None    

def menu_info():
    rect_pointeur = pygame.Rect(pygame.mouse.get_pos(),(1,1))
    rect_retour = pygame.Rect((50,25), (180,35))
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            abientot()
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_pointeur.colliderect(rect_retour):
                return 1

    fenetre.fill(blanc)
    fenetre.blit(calibri_font.render("< Retour", True, blue), (50, 30))
    fenetre.blit(InfoMenu, (0,80))

    if rect_pointeur.colliderect(rect_retour):
        fenetre.blit(calibri_font.render("< Retour", True, blue2), (50, 30))
    pygame.display.flip()

def abientot ():
    pygame.mixer.music.load("Amnesia.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(1,0.0)
    fenetre.fill(noir)
    fenetre.blit(pygame.font.Font("Molot.otf",340).render("Merci !", True, blanc), (170, 260))
    pygame.display.flip()
    pygame.time.wait(4000)
    
"""
MAIN
"""

def main():
    global score
    saut = 20
    score = 0
    player = Player()
    mur = Mur()
    mur02 = Mur()
    mur03 = Mur()
    mur02.x += 533
    mur03.x += 1066
    fenetre.fill(fond)
    player.update(saut)
    mur.update()
    pygame.display.flip()
    game_over = False
    pygame.time.wait(500)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                abientot()
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    saut = 40
             
        if saut > -50:
            saut -=1

        fenetre.fill(fond)
        player.update(saut)
        mur.update()
        mur02.update()
        mur03.update()
        fenetre.blit(calibri_font.render("Score: "+ str(score), True, blue), (1300, 25))
        pygame.display.update()
        if player.rect.colliderect (mur.rect) or player.rect.colliderect(mur.rect2) or player.rect.colliderect(mur02.rect) or player.rect.colliderect(mur02.rect2) or player.rect.colliderect(mur03.rect) or player.rect.colliderect(mur03.rect2):
            print "collision"
            gameOver()

        if player.y<0 or player.y>950 :
            print "sortie"
            gameOver()
        
        pygame.time.wait(2)


"""
Lancement du programme
"""
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1,0.0)
gameOver()
main()
pygame.quit()
quit()
