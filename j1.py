import sys
import pygame 
import random
import time
 
pygame.init()
pygame.mixer.init()

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
assets['azul'] = pygame.image.load('assets/imagens/teclaazulligada.png').convert_alpha()
assets['azul'] = pygame.transform.scale(assets['azul'], (850,600)) 
assets['verde'] = pygame.image.load('assets/imagens/teclaverdeligada.png').convert_alpha()
assets['verde'] = pygame.transform.scale(assets['verde'], (850,600))

#carrega os sons do jogo
pygame.mixer.music.load('assets/som/notadateclavermelha.mp3')
pygame.mixer.music.set_volume(0.4)
assets['som da tecla vermelha'] = pygame.mixer.Sound('assets/som/notadateclavermelha.mp3')
assets['som da tecla amarela'] = pygame.mixer.Sound('assets/som/notadateclaamarela.mp3')
assets['som da tecla azul'] = pygame.mixer.Sound('assets/som/notadateclaazul.mp3')

DESLIGADO=0
VERMELHO=1
AMARELO=2
AZUL = 3
VERDE = 4

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

#definindo a primeira tecla
#recebe a lista tecla
class Animacao (pygame.sprite.Sprite):
    def __init__(self, assets, listatecla):
        pygame.sprite.Sprite.__init__(self)
        listaanimacao = []
        if len(listatecla)==1:
            listaanimacao.append(assets['desligado'])
        for i in listatecla:
            if listatecla[i]== 1:
                listaanimacao.append(assets['vermelho'])
            elif listatecla[i]==2:
                listaanimacao.append(assets['amarelo'])
            elif listatecla[i]==3:
                listaanimacao.append(assets['azul'])
            else:
                listaanimacao.append(assets['verde'])
        self.teclas_animacao = listaanimacao
        self.frame = 0
        self.image = self.teclas_animacao[self.frame]
        self.rect = self.image.get_rect()

        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 5000
    def uptade(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:
            self.last_update = now

            self.frame += 1

            if self.frame == len(self.explosion_anim):
                self.kill()
            else:
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()


tecla1 = Teclas()
all_sprites = pygame.sprite.Group()
all_sprites.add(tecla1)
clock = pygame.time.Clock()
FPS = 30

# loop principal
game=True
x = 1
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        a = sorteiasequencia(x)
        for i in a:
            if a[i]==1:
                animacao = Animacao(assets, sorteiasequencia)
                
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_UP:
                        x+=1
                    else:
                        break
            if a[i]==2:
                animacao = Animacao(assets, sorteiasequencia)
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_LEFT:
                        x+=1
                    else:
                        break
            if a[i]==3:
                animacao = Animacao(assets, sorteiasequencia)
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_DOWN:
                        x+=1
                    else:
                        break
            if a[i]==4:
                animacao = Animacao(assets, sorteiasequencia)
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_RIGHT:
                        x+=1
                    else:
                        break

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



