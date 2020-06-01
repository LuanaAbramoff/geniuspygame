import sys
import pygame 
import random
import time
 
pygame.init()
pygame.mixer.init()

#cria tela inicial
largura= 1000
altura= 700
surf = pygame.display.set_mode((largura, altura))
surf.fill([255,255,255])
pygame.display.set_caption("Genius no escuro")

#dicionário assets
assets = {}
assets['desligado'] = pygame.image.load('assets/imagens/geniusdesligado.png').convert_alpha()
assets['desligado'] = pygame.transform.scale(assets['desligado'], (1000,700))
assets['vermelho'] = pygame.image.load('assets/imagens/teclavermelhaligada.png').convert_alpha()
assets['vermelho'] = pygame.transform.scale(assets['vermelho'], (1000,700))
assets['amarelo'] = pygame.image.load('assets/imagens/teclaamarelaligada.png').convert_alpha()
assets['amarelo'] = pygame.transform.scale(assets['amarelo'], (1000,700))
assets['azul'] = pygame.image.load('assets/imagens/teclaazulligada.png').convert_alpha()
assets['azul'] = pygame.transform.scale(assets['azul'], (1000,700)) 
assets['verde'] = pygame.image.load('assets/imagens/teclaverdeligada.png').convert_alpha()
assets['verde'] = pygame.transform.scale(assets['verde'], (1000,700))

#carrega os sons do jogo
pygame.mixer.music.set_volume(0.4)
assets['som da tecla vermelha'] = pygame.mixer.Sound('assets/som/vermelho.wav')
assets['som da tecla amarela'] = pygame.mixer.Sound('assets/som/amarelo.wav')
assets['som da tecla azul'] = pygame.mixer.Sound('assets/som/azul.wav')
assets['som da tecla verde'] = pygame.mixer.Sound('assets/som/verde.wav')
assets['som de perdeu'] = pygame.mixer.Sound('assets/som/perdeu.wav')


#funcao que sorteia a seguencia das teclas
def sorteiasequencia(x):
    i=0
    listatecla=[]
    while i<x:
        tecla = random.randint(1,4)
        listatecla.append(tecla)
        i += 1
    return listatecla

#definindo a primeira tecla
#recebe a lista tecla
class Animacao (pygame.sprite.Sprite):
    def __init__(self, assets, seq):
        pygame.sprite.Sprite.__init__(self)
        listaanimacao = []
        listaanimacao.append(assets['desligado'])
        for i in seq:
            if i== 1:
                listaanimacao.append(assets['vermelho'])
                listaanimacao.append(assets['desligado'])
            elif i==2:
                listaanimacao.append(assets['amarelo'])
                listaanimacao.append(assets['desligado'])
            elif i==3:
                listaanimacao.append(assets['azul'])
                listaanimacao.append(assets['desligado'])
            else:
                listaanimacao.append(assets['verde'])
                listaanimacao.append(assets['desligado'])

        self.teclas_animacao = listaanimacao
        self.frame = 0
        self.image = self.teclas_animacao[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 500

    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:
            self.last_update = now

            self.frame += 1

            if self.frame == len(self.teclas_animacao):
                self.kill()
            else:
                self.image = self.teclas_animacao[self.frame]
                self.rect = self.image.get_rect()



all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
FPS = 30

# loop principal
game=True
x = 1
seq = sorteiasequencia(x)
print(seq)
botao_atual = 0
animacao = Animacao(assets, seq)
all_sprites.add(animacao)
while game and x<9:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if event.type == pygame.KEYDOWN:
            if seq[botao_atual]==1 and event.key == pygame.K_UP:
                botao_atual += 1 
                print('CIMA')
            elif seq[botao_atual]==2 and event.key == pygame.K_RIGHT:
                botao_atual += 1
                print('DIREITA')
            elif seq[botao_atual]==3 and event.key == pygame.K_DOWN:
                botao_atual += 1
                print('BAIXO')
            elif seq[botao_atual]==4 and event.key == pygame.K_LEFT:
                botao_atual += 1
                print('ESQUERDA')
            if botao_atual == len(seq):
                x += 1
                seq = sorteiasequencia(x)
                animacao.kill()
                animacao = Animacao(assets, seq)
                all_sprites.add(animacao)
                print("aqui")
                botao_atual = 0

    all_sprites.update()
    all_sprites.draw(surf)
    pygame.display.update()
   
    
pygame.quit()


