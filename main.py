import psutil
import pygame

# Iniciando a janela principal
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Uso de memória")
pygame.display.init()

rosa = (255,20,147)
claro = (255,192,203)
choque = 	(220,20,60)
branco = (255, 255, 255)

pygame.font.init()
font = pygame.font.Font(None, 32)
font2 = pygame.font.Font(None, 32)

# Mostar uso de memória
def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2*20
    tela.fill(branco)
    pygame.draw.rect(tela, rosa, (20, 50, larg, 70))
    larg = larg*mem.percent/100
    pygame.draw.rect(tela, claro, (20, 50, larg, 70))
    total = round(mem.total/1024**2,2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "MB):"
    text = font.render(texto_barra, 1, choque)
    tela.blit(text, (20, 10))
    porcentagem = round(mem.percent,2)
    textinho = f'O uso em porcentagem é: {str(porcentagem)} %'
    texto = font2.render(textinho, 1, choque)
    tela.blit(texto, (20, 140))
    
def mostra_uso_cpu():
    capacidade = psutil.cpu_percent(interval=0)
    larg = largura_tela - 2*20
    #tela.fill(preto)
    pygame.draw.rect(tela, rosa, (20, 250, larg, 70))
    larg = larg*capacidade/100
    pygame.draw.rect(tela, claro, (20, 250, larg, 70))
    text = font.render("Uso de CPU:", 1, choque)
    tela.blit(text, (20, 210))  
    mensagem = f'O uso da CPU em porcentagem é:   {str(capacidade)} %'
    msg = font.render(mensagem, 1, choque)
    tela.blit(msg,(20,330))


# Cria relógio
clock = pygame.time.Clock()

cont = 60

terminou = False
while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  terminou = True
    if cont == 60:
                
                mostra_uso_memoria()
                mostra_uso_cpu()
                cont = 0

    # Atualiza o desenho na tela
    pygame.display.update()
    # 60 frames por segundo
    clock.tick(60)
    cont = cont + 1

# Finaliza a janela
pygame.display.quit()
