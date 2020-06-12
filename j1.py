
#Jogo Genius - Ana Barros e Luana Abramoff

#O objetivo do jogo é tentar reproduzir a sequencia de teclas apresentadas. No primeiro nível,
#a sequencia possui uma tecla apenas, no segundo, duas, e assim por diante, até chegar no nível cinco (sequencia
#com cinco teclas). Passando pelo nível 5, o jogador, que estava na fase 1, passa para a próxima fase. Na fase 2,
#a tecla vermelha não acende mais, só seu som é tocado. Nessa etapa, ainda é relativamente simples, pois se um som
#foi tocado mas nenhuma tecla acesa, certamente é a vermelha. Contudo, nas fases 3, 4, 5, gradualmente, as outras
#teclas também deixam de acender, e o jogador passa a utilizar somente o sons para diferenciar as teclas.
#Cada vez que o jogador erra, ele perde uma vida e recomeca do primeiro nível da fase em que está. Cada fase possui 3 vidas.
#Quando perde as tres vidas em uma mesma fase, o jogador perde de vez. Bom jogo!


#importa bibliotecas
import sys
import pygame 
import random
import time

#inicia pygame e pygame mixer
pygame.init()
pygame.mixer.init()

#cria tela inicial
largura= 1000
altura= 601
surf = pygame.display.set_mode((largura, altura))
surf.fill([255,255,255])
pygame.display.set_caption("Genius no escuro")

#define tamanho e posicao das imagens
largura_imagem=603
altura_imagem=601
ximagem=180
yimagem=0

#dicionário assets imagens
assets = {}
assets['desligado'] = pygame.image.load('assets/imagens/geniusdesligado.PNG').convert_alpha()
assets['desligado'] = pygame.transform.scale(assets['desligado'], (largura_imagem,altura_imagem))

assets['desligado vermelho'] = pygame.image.load('assets/imagens/geniusdesligadovermelho.PNG').convert_alpha()
assets['desligado vermelho'] = pygame.transform.scale(assets['desligado vermelho'], (largura_imagem,altura_imagem))

assets['desligado amarelo'] = pygame.image.load('assets/imagens/geniusdesligadoamarelo.PNG').convert_alpha()
assets['desligado amarelo'] = pygame.transform.scale(assets['desligado amarelo'], (largura_imagem,altura_imagem))

assets['desligado azul'] = pygame.image.load('assets/imagens/geniusdesligadoazul.PNG').convert_alpha()
assets['desligado azul'] = pygame.transform.scale(assets['desligado azul'], (largura_imagem,altura_imagem))

assets['desligado verde'] = pygame.image.load('assets/imagens/geniusdesligadoverde.PNG').convert_alpha()
assets['desligado verde'] = pygame.transform.scale(assets['desligado verde'], (largura_imagem,altura_imagem))

assets['vermelho'] = pygame.image.load('assets/imagens/teclavermelhaligada.PNG').convert_alpha()
assets['vermelho'] = pygame.transform.scale(assets['vermelho'], (largura_imagem,altura_imagem))

assets['amarelo'] = pygame.image.load('assets/imagens/teclaamarelaligada.PNG').convert_alpha()
assets['amarelo'] = pygame.transform.scale(assets['amarelo'], (largura_imagem,altura_imagem))

assets['azul'] = pygame.image.load('assets/imagens/teclaazulligada.PNG').convert_alpha()
assets['azul'] = pygame.transform.scale(assets['azul'], (largura_imagem,altura_imagem)) 

assets['verde'] = pygame.image.load('assets/imagens/teclaverdeligada.PNG').convert_alpha()
assets['verde'] = pygame.transform.scale(assets['verde'], (largura_imagem,altura_imagem))

assets['instru1'] = pygame.image.load('assets/imagens/instrucoes.png').convert_alpha()
assets['instru1'] = pygame.transform.scale(assets['instru1'], (largura_imagem,altura_imagem))

assets['instru2'] = pygame.image.load('assets/imagens/instrucoes1.png').convert_alpha()
assets['instru2'] = pygame.transform.scale(assets['instru2'], (largura_imagem,altura_imagem))

assets['instru3'] = pygame.image.load('assets/imagens/instrucoes2.png').convert_alpha()
assets['instru3'] = pygame.transform.scale(assets['instru3'], (largura_imagem,altura_imagem))

assets['instru4'] = pygame.image.load('assets/imagens/instrucoes3.png').convert_alpha()
assets['instru4'] = pygame.transform.scale(assets['instru4'], (largura_imagem,altura_imagem))

assets['instru5'] = pygame.image.load('assets/imagens/instrucoes4.png').convert_alpha()
assets['instru5'] = pygame.transform.scale(assets['instru5'], (largura_imagem,altura_imagem))

#animacaopassardefase
listaanimacao = []
for i in range(36):
    filename = 'assets/imagens/animacaopassadefase{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img,(603,601))
    listaanimacao.append(img)
assets['animacao para passar de fase']=listaanimacao

#animacaodeinicio
listainicio = []
for i in range(158):
    filename = 'assets/imagens/animacaodeinicio ({}).png'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img,(603,601))
    listainicio.append(img)
assets['animacao de inicio']=listainicio

#animacaoespaco
listaespaco = []
for i in range(8):
    filename = 'assets/imagens/aperteespaço ({}).png'.format(i)
    img = pygame.image.load(filename).convert()
    img =  pygame.transform.scale(img,(603,601))
    listaespaco.append(img)
assets['animacao espaco']=listaespaco

#animacaoperdeu
listaperdeu = []
for i in range(20):
    filename = 'assets/imagens/perdeu ({}).png'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img,(603,601))
    listaperdeu.append(img)
assets['animacao perdeu'] = listaperdeu

#dicionario assets som e fonte
pygame.mixer.music.set_volume(0.4)
assets['som da tecla vermelha'] = pygame.mixer.Sound('assets/som/vermelho.ogg')
assets['som da tecla amarela'] = pygame.mixer.Sound('assets/som/amarelo.ogg')
assets['som da tecla azul'] = pygame.mixer.Sound('assets/som/azul.ogg')
assets['som da tecla verde'] = pygame.mixer.Sound('assets/som/verde.ogg')
assets['som de perdeu'] = pygame.mixer.Sound('assets/som/perdeu.ogg')
assets['som passa de fase'] = pygame.mixer.Sound('assets/som/passadefase.ogg')

assets["nivel_fonte"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)

#animacao que acende as teclas enquanto joga
class AnimacaoTecla(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = ximagem
        self.rect.y = yimagem

#animacao das instrucoes antes das fases
class AnimacaoInstrucao(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = ximagem
        self.rect.y = yimagem
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 5000
    
    def restart(self):
        self.last_update = pygame.time.get_ticks()

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            self.kill()

              
#animacao das teclas do jogo
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
        self.rect.x = ximagem
        self.rect.y = yimagem

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
                self.rect.x = ximagem
                self.rect.y = yimagem

            #seleciona o som de acordo com a tecla
            if self.image == assets['vermelho'] or self.image == assets['desligado vermelho']:
                assets['som da tecla vermelha'].play()
            elif self.image == assets['amarelo'] or self.image == assets['desligado amarelo']:
                assets['som da tecla amarela'].play()
            elif self.image == assets['verde'] or self.image == assets['desligado azul']:
                assets['som da tecla verde'].play()
            elif self.image == assets['azul'] or self.image == assets['desligado verde']:
                assets['som da tecla azul'].play()

#animacao inicial
class AnimacaoInicio(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.Terminou = False

        # Armazena a animação 
        self.animacaodeinicio = assets['animacao de inicio']

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.animacaodeinicio[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.x = ximagem
        self.rect.y = yimagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.animacaodeinicio):
                # Se sim, acaba com a animação
                self.Terminou = True
            elif self.frame < len(self.animacaodeinicio):
                # Se ainda não chegou ao fim da animacao, troca de imagem.
                self.image = self.animacaodeinicio[self.frame]
                self.rect = self.image.get_rect()
                self.rect.x = ximagem
                self.rect.y = yimagem

#animacao entre fases
class Animacaopassadefase(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação 
        self.animacaodefase = assets['animacao para passar de fase']


        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.animacaodefase[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.x = ximagem
        self.rect.y = yimagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
       
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        
        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.animacaodefase):
                # Se sim, acaba com a animação
                self.kill()
            else:
                # Se ainda não chegou ao fim da animacao, troca de imagem.
                self.image = self.animacaodefase[self.frame]
                self.rect = self.image.get_rect()
                self.rect.x = ximagem
                self.rect.y = yimagem
           

#animacao para apertar espaco antes de jogar
class AnimacaoEspaco(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação
        self.animacaoespaco = assets['animacao espaco']

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.animacaoespaco[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.x = ximagem
        self.rect.y = yimagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.animacaoespaco):
                # Se sim, acaba com a animação
                self.frame = 0
            else:
                # Se ainda não chegou ao fim da animacao, troca de imagem.
                self.image = self.animacaoespaco[self.frame]
                self.rect = self.image.get_rect()
                self.rect.x = ximagem
                self.rect.y = yimagem

#animacao quando perde
class AnimacaoPerdeu(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação
        self.animacaoperdeu = assets['animacao perdeu']
        self.Terminouu = False

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.animacaoperdeu[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.x = ximagem
        self.rect.y = yimagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 200

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.animacaoperdeu):
                # Se sim, acaba com a animação
                self.Terminouu = True
            elif self.frame < len(self.animacaoperdeu):
                # Se ainda não chegou ao fim da animacao, troca de imagem.
                self.image = self.animacaoperdeu[self.frame]
                self.rect = self.image.get_rect()
                self.rect.x = ximagem
                self.rect.y = yimagem

#funcao que sorteia a seguencia das teclas
def sorteiasequencia(x):
    i=0
    listatecla=[]
    while i<x:
        tecla = random.randint(1,4)
        listatecla.append(tecla)
        i += 1
    return listatecla

#cria o grupo dos objetos 
all_sprites = pygame.sprite.Group()

#tick da animacao
clock = pygame.time.Clock()
FPS=30

#condicoes iniciais
game=True
inicial = True
nivel = 1 
fase = 1
vidas=3
seq = sorteiasequencia(nivel) #cria primeira sequencia
botao_atual = 0 #caminha dentro da sequencia criada
tela_inicial = True
criaanimacaodeespaco = False
animacaodeinicio = AnimacaoInicio(assets)
all_sprites.add(animacaodeinicio)


# ===== Loop principal =====
while tela_inicial:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            tela_inicial = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and animacaodeinicio.Terminou:
                animaespaco.kill()
                tela_inicial = False
 
    # ----- Gera saídas
    if animacaodeinicio.Terminou and not criaanimacaodeespaco:
        animacaodeinicio.kill()
        criaanimacaodeespaco = True
        animaespaco = AnimacaoEspaco(assets)
        all_sprites.add(animaespaco)

    all_sprites.update()
    all_sprites.draw(surf)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador 


instru1=AnimacaoInstrucao(assets["instru1"])
instru2=AnimacaoInstrucao(assets["instru2"])
instru3=AnimacaoInstrucao(assets["instru3"])
instru4=AnimacaoInstrucao(assets["instru4"])
instru5=AnimacaoInstrucao(assets["instru5"])
instru_i = 0
instrucoes = [instru1, instru2, instru3, instru4, instru5]

all_sprites.add(instru1)
instrucao = instru1

mudando_fase = False
mostrando_instrucao = True

botao_vermelho = AnimacaoTecla(assets['vermelho'])
botao_amarelo = AnimacaoTecla(assets['amarelo'])
botao_azul = AnimacaoTecla(assets['azul'])
botao_verde = AnimacaoTecla(assets['verde'])

animaperdeu = None

# loop principal
while game and nivel<6:
    clock.tick(FPS)
    surf.fill([255,255,255])
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if event.type == pygame.KEYDOWN:
            if not animacao.alive():
                if event.key == pygame.K_UP:
                    all_sprites.add(botao_vermelho)
                    print('CIMA')
                elif event.key == pygame.K_RIGHT:
                    all_sprites.add(botao_amarelo)
                    print('DIREITA')
                elif event.key == pygame.K_DOWN:
                    all_sprites.add(botao_azul)
                    print('BAIXO')
                elif event.key == pygame.K_LEFT:
                    all_sprites.add(botao_verde)
                    print('ESQUERDA')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                botao_vermelho.kill()
                if seq[botao_atual]==1:
                    botao_atual += 1 
                else:
                    vidas-=1
                    
                    if vidas==0:
                        animaperdeu = AnimacaoPerdeu(assets)
                        all_sprites.add(animaperdeu)
                    else:
                        botao_atual=0
                        animacao.kill()
                        nivel=1 #volta para o início 
                        seq = sorteiasequencia(nivel)
                        animacao=Animacao(assets,seq, fase)
                        all_sprites.add(animacao)

                    assets['som de perdeu'].play()

            elif event.key == pygame.K_RIGHT:
                botao_amarelo.kill()
                if seq[botao_atual]==2:
                    botao_atual += 1
                else:
                    vidas-=1
                    if vidas==0:
                        animaperdeu = AnimacaoPerdeu(assets)
                        all_sprites.add(animaperdeu)
                    else:
                        botao_atual=0
                        animacao.kill()
                        nivel=1 #volta para o início 
                        seq = sorteiasequencia(nivel)
                        animacao=Animacao(assets,seq, fase)
                        all_sprites.add(animacao)

                    assets['som de perdeu'].play()
                
            elif event.key == pygame.K_DOWN:
                botao_azul.kill()
                if seq[botao_atual]==3:
                    botao_atual += 1
                else:
                    vidas-=1
                    if vidas==0:
                        animaperdeu = AnimacaoPerdeu(assets)
                        all_sprites.add(animaperdeu)
                    else:
                        botao_atual=0
                        animacao.kill()
                        nivel=1 #volta para o início 
                        seq = sorteiasequencia(nivel)
                        animacao=Animacao(assets,seq, fase)
                        all_sprites.add(animacao)

                    assets['som de perdeu'].play()

            elif event.key == pygame.K_LEFT:
                botao_verde.kill()
                if seq[botao_atual]==4:
                    botao_atual += 1
                else:
                    vidas-=1
                    if vidas==0:
                        animaperdeu = AnimacaoPerdeu(assets)
                        all_sprites.add(animaperdeu)
                        
                    else:
                        botao_atual=0
                        animacao.kill()
                        nivel=1 #volta para o início 
                        seq = sorteiasequencia(nivel)
                        animacao=Animacao(assets,seq, fase)
                        all_sprites.add(animacao)

                    assets['som de perdeu'].play()
            if botao_atual == len(seq):
                nivel += 1 # passa para o proximo nivel
                botao_atual = 0
                seq = sorteiasequencia(nivel) #nova sequencia
                animacao.kill()
                animacao = Animacao(assets, seq, fase)#nova animacao
                all_sprites.add(animacao)
            
            if nivel==6:
                assets['som passa de fase'].play()
                botao_atual=0
                fase+=1 # passa para a próxima fase
                nivel=1
                animacao.kill()
                mudando_fase = True
                animacaodefase = Animacaopassadefase(assets)
                all_sprites.add(animacaodefase)

    if mudando_fase and not animacaodefase.alive():
        instru_i += 1
        if instru_i < len(instrucoes):
            instrucao = instrucoes[instru_i]
            instrucao.restart()
            all_sprites.add(instrucao)
        mostrando_instrucao = True
        mudando_fase = False
   
    if mostrando_instrucao and not instrucao.alive():
        seq = sorteiasequencia(nivel)
        animacao= Animacao(assets, seq, fase)
        all_sprites.add(animacao)
        mostrando_instrucao = False

    if animaperdeu is not None and animaperdeu.Terminouu:
        animaperdeu.kill()
        game=False

    all_sprites.update()
    surf.blit(assets['desligado'], (ximagem, yimagem))
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


