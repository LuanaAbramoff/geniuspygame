import sys
import pygame 
import random
import time
 
pygame.init()

#cria tela inicial
largura= 700
altura= 700
surf = pygame.display.set_mode((largura, altura))
surf.fill([255,255,255])
pygame.display.set_caption("Genius no escuro")

#dicionário assets
assets = {}
assets['desligado'] = pygame.image.load('assets/imagens/geniusdesligado.png').convert_alpha()
assets['desligado'] = pygame.transform.scale(assets['desligado'], (850,600))
assets['vermelho'] = pygame.image.load('assets/imagens/teclavermelhaligada.png').convert_alpha()
assets['vermelho'] = pygame.transform.scale(assets['vermelho'], (850,600))
assets['amarelo'] = pygame.image.load('assets/imagens/teclaamarelaligada.png').convert_alpha()
assets['amarelo'] = pygame.transform.scale(assets['amarelo'], (850,600))
assets['azul'] = pygame.image.load('assets/imagens/teclaazuligada.png').convert_alpha()
assets['azul'] = pygame.transform.scale(assets['azul'], (850,600)) 
assets['verde'] = pygame.image.load('assets/imagens/teclaverdeigada.png').convert_alpha()
assets['verde'] = pygame.transform.scale(assets['verde'], (850,600))

DESLIGADO=0
VERMELHO=1
AMARELO=2
VERDE = 4
AZUL = 3
# define as classes do jogo (as quatro teclas)
class Teclas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [assets['desligado'], assets['vermelho'], assets['amarelo'], assets['azul'], assets['verde']]
        self.coratual = DESLIGADO
        self.image = self.images[self.coratual]
        self.rect = self.image.get_rect()
        self.teclas = []

    def update(self):
        self.image = self.images[self.coratual]
        self.rect = self.image.get_rect()
  


#funcao que sorteia a seguencia das teclas
def sorteiasequencia(x):
    i=0
    listatecla=[]
    while i<x:
        tecla = random.randint(1,4)
        listatecla.append(tecla)
    return listatecla
a = sorteiasequencia(1)
#definindo a primeira tecla
class Tecla2 (pygame.sprite.Sprite):
    def __init__(self):
        if a[0]==1:
            self.image = self.images[VERMELHO]
        elif a[0]==2:
            self.image = self.images[AMARELO]
        elif a[0]==3:
            self.image =self.images[AZUL]
        else:
            self.image = self.images[VERDE]
       
    def uptade(self):
        self.rect = self.image.get_rect()

tecla1 = Teclas()
all_sprites = pygame.sprite.Group()
all_sprites.add(tecla1)
tecla2 = Tecla2()
all_sprites.add(tecla2)

# loop principal
game=True
 
while game:
    eventos  = pygame.event.get()
    for evento in eventos:
        if evento.type==pygame.QUIT:
            game=False
            pygame.quit()
            sys.exit()

    tecla1.teclas=sorteiasequencia(1)
        # if evento.type==pygame.KEYDOWN:
        #     if evento.key==pygame.K_UP:
        #         tecla1.coratual=VERMELHO
    
    all_sprites.update()
    surf.fill([255,255,255])
    all_sprites.draw(surf)
    pygame.display.update()
     

pygame.quit()


