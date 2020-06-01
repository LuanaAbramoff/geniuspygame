#importa bibliotecas
import sys
import pygame 
import random
import time

#inicia pygame
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
assets["nivel_fonte"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)

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


#Classe Animacao
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

            #seleciona o som de acordo com a tecla
            if self.image == assets['vermelho']:
                assets['som da tecla vermelha'].play()
            elif self.image == assets['amarelo']:
                assets['som da tecla amarela'].play()
            elif self.image == assets['verde']:
                assets['som da tecla verde'].play()
            elif self.image == assets['azul']:
                assets['som da tecla azul'].play()


#cria o grupo dos objetos 
all_sprites = pygame.sprite.Group()

#tick da animacao
clock = pygame.time.Clock()
FPS=30

game=True
x = 1 # x indica o nível
vidas=3
seq = sorteiasequencia(x) #cria primeira sequencia

botao_atual = 0 #caminhando dentro da sequencia criada
animacao = Animacao(assets, seq) #cria uma animacao
all_sprites.add(animacao) #adiciona animacao

# loop principal
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
            else: # se a pessoa erra alguma tecla
                vidas-=1
                if vidas==0:
                    game=False
                    #fazer animacao para comecar tudo de novo
                assets['som de perdeu'].play()
                botao_atual=0
                animacao.kill()
                x=1 #volta para o início 
                seq = sorteiasequencia(x)
                animacao=Animacao(assets,seq)
                all_sprites.add(animacao)
                
                break
           
            if botao_atual == len(seq):
                x += 1 # passa para o proximo nivel
                seq = sorteiasequencia(x) #nova sequencia
                animacao.kill()
                animacao = Animacao(assets, seq)#nova animacao
                all_sprites.add(animacao)
                botao_atual = 0
            
            

    all_sprites.update()
    all_sprites.draw(surf)
    text_surface = assets['nivel_fonte'].render('Nível: {0}'.format(x), True, (0, 0, 255))#mostra o nível na tela
    text_rect = text_surface.get_rect()
    text_rect.midtop = (largura / 2,  10)
    surf.blit(text_surface, text_rect)
    text_surface2 = assets['nivel_fonte'].render('Vidas: {0}'.format(vidas), True, (0, 0, 0))#mostra as vidas na tela
    text_rect = text_surface.get_rect()
    text_rect.midtop = (140,  altura-50)
    surf.blit(text_surface2, text_rect)
    pygame.display.update()
   
    
pygame.quit()


