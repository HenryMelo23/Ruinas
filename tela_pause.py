import pygame
import sys
from var import largura_mapa, altura_mapa, largura_tela, altura_tela,pontuacao,pontuacao_magia

# Definindo algumas cores
branco = (255, 255, 255)
preto = (0, 0, 0)

def tela_atributos():
    global pontuacao_magia
    pausa = True
    tela_pausa = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Tela de Atributos")

    while pausa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tela_pausa.fill(branco)
        
        fonte = pygame.font.Font(None, 36)
        texto_titulo = fonte.render("Escolha um atributo:", True, preto)
        texto_opcoes = fonte.render("1 - Ódio Profundo   2 - Botas do Poder", True, preto)

        # Centraliza o texto na tela
        pos_titulo = ((largura_tela - texto_titulo.get_width()) // 2, altura_tela // 2 - 100)
        pos_opcoes = ((largura_tela - texto_opcoes.get_width()) // 2, altura_tela // 2 - 50)

        tela_pausa.blit(texto_titulo, pos_titulo)
        tela_pausa.blit(texto_opcoes, pos_opcoes)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    escolha_jogador = 1
                    print("SINTA MINHA IRÁ")
                    
                    pausa = False
                    pontuacao=0
                elif event.key == pygame.K_2:
                    escolha_jogador = 2
                    print("ESTOU QUASE FLUTUANDO")
                    
                    pausa = False
                    pontuacao=0
                    pontuacao=0
                if event.key == pygame.K_KP_1:
                    escolha_jogador = 1
                    print("SINTA MINHA IRÁ")
                    
                    pausa = False
                    pontuacao=0
                elif event.key == pygame.K_KP_2:
                    escolha_jogador = 2
                    print("ESTOU QUASE FLUTUANDO")
                    pausa = False
                    
                    pontuacao=0


        pygame.display.flip()
    pontuacao_magia -= 150  # Zera a barra de magia após escolher um atributo
    # Restante da função...
    # Certifique-se de lidar com as outras funcionalidades da tela de pausa aqui

# Inicie a tela de pausa quando necessário
# tela_de_pausa()
