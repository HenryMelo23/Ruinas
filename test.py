import pygame
import sys
from var import largura_mapa, altura_mapa,largura_tela, altura_tela,velocidade_personagem,intervalo_disparo

escolha_jogador = None
def tela_de_pausa():
    global escolha_jogador, pontuacao_magia,velocidade_personagem,intervalo_disparo

    pausa = True
    tela_pausa = pygame.display.set_mode((largura_mapa, altura_mapa))
    pygame.display.set_caption("Tela de Atributos")

    while pausa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    escolha_jogador = 1
                    print("SINTA MINHA IRÁ")
                    intervalo_disparo = max(100, intervalo_disparo - 8.5)
                    pausa = False
                    
                elif event.key == pygame.K_2:
                    escolha_jogador = 2
                    print("ESTOU QUASE FLUTUANDO")
                    velocidade_personagem += 20

                    pausa = False
                    
                if event.key == pygame.K_KP_1:
                    escolha_jogador = 1
                    print("SINTA MINHA IRÁ")
                    intervalo_disparo = max(100, intervalo_disparo - 8.5)
                    pausa = False
                    
                elif event.key == pygame.K_KP_2:
                    escolha_jogador = 2
                    print("ESTOU QUASE FLUTUANDO")
                    pausa = False
                    velocidade_personagem += 20
                    
                

                
                    

            tela_pausa.fill((255, 255, 255))
            fonte = pygame.font.Font(None, 36)
            cor_do_texto = (0, 255, 255)  # Cor preta

            texto_titulo = fonte.render("Escolha um atributo:", True, cor_do_texto)
            texto_opcoes = fonte.render("1 - Ódio Profundo   2 - Botas do Poder", True, cor_do_texto)

            # Centraliza o texto no meio da tela
            pos_titulo = ((largura_mapa - texto_titulo.get_width()) // 2, altura_mapa // 2 - 100)
            pos_opcoes = ((largura_mapa - texto_opcoes.get_width()) // 2, altura_mapa // 2 - 50)

            tela_pausa.blit(texto_titulo, pos_titulo)
            tela_pausa.blit(texto_opcoes, pos_opcoes)
            pygame.display.flip()

    pontuacao_magia = 0  # Zera a barra de magia após escolher um atributo
    # Retornar ao jogo
    pygame.display.set_mode((largura_tela, altura_tela))




