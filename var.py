########################################## VARIAVEIS MAPA
largura_mapa, altura_mapa = 1920, 1080
largura_tela, altura_tela = 1920, 2380
#########################################  Condicionais
velocidade_personagem = 30 #velocidade do player
intervalo_disparo = 200  # Intervalo mínimo entre disparos em milissegundos
# Variável para armazenar a pontuação
pontuacao = 0
pontuacao_magia=0
#########################################  CHEFE
LARGURA_CHEFE=780
ALTURA_CHEFE=1080
vida_chefe = 1500  # Ajuste conforme necessário
pos_x_chefe, pos_y_chefe = largura_mapa - 620, 0
velocidade_chefe = 0  # Ajuste conforme necessário
projeteis_chefe = []
intervalo_projeteis = 800  # Intervalo entre disparos em milissegundos
contagem_projeteis_chefe = 0
max_projeteis_chefe = 5
tamanho_projetil_chefe = 40
chefe_atual = 0
tempo_animacao_chefe = 500  # Tempo em milissegundos entre cada quadro
tempo_passado_chefe = 0
#########################################  CORES_GERAIS
amarelo= (255, 255, 0)
vermelho=(255, 0, 0)
#########################################