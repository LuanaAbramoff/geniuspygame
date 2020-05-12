import sys
import pygame 
 
pygame.init()
 
surf = pygame.display.set_mode([600,700])
pygame.display.set_caption("Genius no escuro")

 
surf.fill([0,0,0])

image = pygame.image.load('assets/imagens/basepretagenius2.png').convert()
image= pygame.transform.scale(image,(850,550))
 


game=True
 
while game:
    eventos  = pygame.event.get()
    for evento in eventos:
        if evento.type==pygame.QUIT:
            game=False
            pygame.quit()
            sys.exit()

    surf.blit(image,(-130,50))
    pygame.display.update()

pygame.quit()