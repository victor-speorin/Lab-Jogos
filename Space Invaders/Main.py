# Importando
import Tiros
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
# import função
import Menu


# Criando a função principal que será chamada no código do menu e virá para a tela do jogo.
def jogar():
    # Criando a janela
    janela = Window(1000, 600)
    janela.set_title("Space Invaders")

    fundo = Sprite("Assets/Fundo.png", 1)
    fundo.x = 0
    fundo.y = 0

    # Criando a variável de comandos
    comandos = Window.get_keyboard()

    # Defino o frame per second
    FPS = 60
    clock = pygame.time.Clock()

    # Criação da nave
    nave = Sprite("Assets//nave.png")
    nave.x = (janela.width - janela.height) / 2
    nave.y = janela.height - nave.height - 10
    nave.set_sequence_time(0, 2, 200, True)

    velnave = 400

    # CRIAÇÃO DOS DISPAROS
    disparos = []
    recarga = 1
    veltiro = 400

    # Loop
    while True:

        # Conto o fps
        clock.tick(FPS)

        # Se o esc for apertado, retorna para o menu
        if comandos.key_pressed('esc'):
            Menu.menu()
        fundo.draw()

        # COMANDOS RELACIONADOS A NAVE:

        # Movimentação
        if (comandos.key_pressed("A")):
            nave.x -= velnave * janela.delta_time()
        if (comandos.key_pressed("D")):
            nave.x += velnave * janela.delta_time()

        # Limitando a nave na tela
        if (nave.x <= 0):
            nave.x = 0
        if (nave.x >= janela.width - nave.width):
            nave.x = janela.width - nave.width

        # COMANDOS RELACIONADOS A TIROS:

        recarga += janela.delta_time()

        # ativar o tiro assim que o espaço for pressionado e respeitando o tempo de recarga
        if (comandos.key_pressed("space")) and (recarga >= 1 / 2) :
            disparos = Tiros.novo_tiro(nave, disparos)
            recarga = 0

        # desenha, controla e limita o disparo
        if (disparos != []):
            for d in disparos:
                d.draw()
                d.y -= veltiro * janela.delta_time()
                d = Tiros.limitando_tiro(d, disparos)

        nave.draw()
        janela.update()
