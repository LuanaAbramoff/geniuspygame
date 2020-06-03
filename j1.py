
#Jogo Genius - Ana Barros e Luana Abramoff

# O jogo consiste em tentar reproduzir a sequencia de teclas apresentadas ao jogador. No primeiro nível, 
# a sequencia possui uma tecla apenas, no segundo, duas, e assim por diante, até chegar no nível oito (sequencia
# com oito teclas). Passando pelo nível 8, o jogador, que estava na Fase 1, passa para a próxima fase. Na fase 2, 
# a tecla vermelha não acende mais, só seu som é tocado. Nessa etapa, ainda é relativamente simples, pois se um som
# foi tocado mas nenhuma tecla acesa, certamente é a vermelha. Contudo, nas fases 3, 4, 5, gradualmente, as outras
# teclas também deixam de acender, e o jogador passa a utilizar somente o sons para diferenciar as teclas. Bom jogo!


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
assets['desligado'] = pygame.image.load('assets/imagens/geniusdesligado.PNG').convert_alpha()
assets['desligado'] = pygame.transform.scale(assets['desligado'], (1000,700))

assets['desligado vermelho'] = pygame.image.load('assets/imagens/geniusdesligadovermelho.PNG').convert_alpha()
assets['desligado vermelho'] = pygame.transform.scale(assets['desligado vermelho'], (1000,700))

assets['desligado amarelo'] = pygame.image.load('assets/imagens/geniusdesligadoamarelo.PNG').convert_alpha()
assets['desligado amarelo'] = pygame.transform.scale(assets['desligado amarelo'], (1000,700))

assets['desligado azul'] = pygame.image.load('assets/imagens/geniusdesligadoazul.PNG').convert_alpha()
assets['desligado azul'] = pygame.transform.scale(assets['desligado azul'], (1000,700))

assets['desligado verde'] = pygame.image.load('assets/imagens/geniusdesligadoverde.PNG').convert_alpha()
assets['desligado verde'] = pygame.transform.scale(assets['desligado verde'], (1000,700))

assets['vermelho'] = pygame.image.load('assets/imagens/teclavermelhaligada.png').convert_alpha()
assets['vermelho'] = pygame.transform.scale(assets['vermelho'], (1000,700))

assets['amarelo'] = pygame.image.load('assets/imagens/teclaamarelaligadaa.PNG').convert_alpha()
assets['amarelo'] = pygame.transform.scale(assets['amarelo'], (1000,700))

assets['azul'] = pygame.image.load('assets/imagens/teclaazulligadaa.PNG').convert_alpha()
assets['azul'] = pygame.transform.scale(assets['azul'], (1000,700)) 

assets['verde'] = pygame.image.load('assets/imagens/teclaverdeligadaa.PNG').convert_alpha()
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
    def __init__(self, assets, seq, fase):
        pygame.sprite.Sprite.__init__(self)
        listaanimacao = []
        listaanimacao.append(assets['desligado'])
        if fase==1:
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

        if fase==2: # a tecla vermelha nao acende mais, só seu som é tocado
            for i in seq:
                if i== 1:
                    listaanimacao.append(assets['desligado vermelho'])
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

        if fase==3: # nem a tecla vermelha nem amarela acendem mais, porém continuam tendo som
            for i in seq:
                if i== 1:
                    listaanimacao.append(assets['desligado vermelho'])
                    listaanimacao.append(assets['desligado'])
                elif i==2:
                    listaanimacao.append(assets['desligado amarelo'])
                    listaanimacao.append(assets['desligado'])
                elif i==3:
                    listaanimacao.append(assets['azul'])
                    listaanimacao.append(assets['desligado'])
                else:
                    listaanimacao.append(assets['verde'])
                    listaanimacao.append(assets['desligado'])

        if fase==4: #só resta a tecla verde acendendo
            for i in seq:
                if i== 1:
                    listaanimacao.append(assets['desligado vermelho'])
                    listaanimacao.append(assets['desligado'])
                elif i==2:
                    listaanimacao.append(assets['desligado amarelo'])
                    listaanimacao.append(assets['desligado'])
                elif i==3:
                    listaanimacao.append(assets['desligado azul'])
                    listaanimacao.append(assets['desligado'])
                else:
                    listaanimacao.append(assets['verde'])
                    listaanimacao.append(assets['desligado'])

        if fase==5: #nenhuma tecla acende mais e o jogador deve jogar se baseando somente nos sons
            for i in seq:
                if i== 1:
                    listaanimacao.append(assets['desligado vermelho'])
                    listaanimacao.append(assets['desligado'])
                elif i==2:
                    listaanimacao.append(assets['desligado amarelo'])
                    listaanimacao.append(assets['desligado'])
                elif i==3:
                    listaanimacao.append(assets['desligado azul'])
                    listaanimacao.append(assets['desligado'])
                else:
                    listaanimacao.append(assets['desligado verde'])
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
            if self.image == assets['vermelho'] or self.image == assets['desligado vermelho']:
                assets['som da tecla vermelha'].play()
            elif self.image == assets['amarelo'] or self.image == assets['desligado amarelo']:
                assets['som da tecla amarela'].play()
            elif self.image == assets['verde'] or self.image == assets['desligado azul']:
                assets['som da tecla verde'].play()
            elif self.image == assets['azul'] or self.image == assets['desligado verde']:
                assets['som da tecla azul'].play()


#cria o grupo dos objetos 
all_sprites = pygame.sprite.Group()

#tick da animacao
clock = pygame.time.Clock()
FPS=30

game=True
nivel = 1 # indica o nível
fase = 1
vidas=3
seq = sorteiasequencia(nivel) #cria primeira sequencia

botao_atual = 0 #caminha dentro da sequencia criada
animacao = Animacao(assets, seq, fase) #cria uma animacao
all_sprites.add(animacao) #adiciona animacao

# loop principal
while game and nivel<9:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if event.type == pygame.KEYDOWN:
            if not animacao.alive():
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
                    nivel=1 #volta para o início 
                    seq = sorteiasequencia(nivel)
                    animacao=Animacao(assets,seq, fase)
                    all_sprites.add(animacao)
            
                if botao_atual == len(seq):
                    nivel += 1 # passa para o proximo nivel
                    botao_atual = 0
                    seq = sorteiasequencia(nivel) #nova sequencia
                    animacao.kill()
                    animacao = Animacao(assets, seq, fase)#nova animacao
                    all_sprites.add(animacao)
                
                if nivel==9:
                    fase+=1 # passa para a próxima fase
                    nivel=1
                    botao_atual=0
                    seq = sorteiasequencia(nivel)
                    animacao.kill()
                    animacao= Animacao(assets, seq, fase)
                    all_sprites.add(animacao)
              

    all_sprites.update()
    all_sprites.draw(surf)
    text_surface = assets['nivel_fonte'].render('Nível: {0}'.format(nivel), True, (0, 0, 255))#mostra o nível na tela
    text_rect = text_surface.get_rect()
    text_rect.midtop = (largura -150,  10)
    surf.blit(text_surface, text_rect)

    text_surface = assets['nivel_fonte'].render('Fase: {0}'.format(fase), True, (0, 0, 255))#mostra o nível na tela
    text_rect = text_surface.get_rect()
    text_rect.midtop = (largura-150, 60)
    surf.blit(text_surface, text_rect)

    text_surface2 = assets['nivel_fonte'].render('Vidas: {0}'.format(vidas), True, (0, 0, 255))#mostra as vidas na tela
    text_rect = text_surface.get_rect()
    text_rect.midtop = (140,  altura-50)
    surf.blit(text_surface2, text_rect)
    pygame.display.update()
   
   
    
pygame.quit()


