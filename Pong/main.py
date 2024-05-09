from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import randint

# inicializando a janela, fundo, bolinha e pads
janela = Window(800, 600)
teclado = janela.get_keyboard()
janela.set_background_color((0,0,0))
janela.set_title("Pong_Victor_Teles")
fundo = GameImage("assets\\Fundo.jpg")
bolinha = Sprite("assets\\vicente.jpg")
pad1 = Sprite("assets\\PadD.png")
pad2 = Sprite("assets\\PadE.png")

# Colocando os pads e bolinha nas posições iniciais"
pad1.set_position((janela.width - pad1.width - 50), (janela.height - pad1.height) / 2)
pad2.set_position((50) , (janela.height - pad2.height) / 2)
bolinha.set_position((janela.width - bolinha.width) / 2, (janela.height - bolinha.height) / 2)

# configurando as velocidades dos pads e bola
velx = 0
vely = 0
vpad2 = 400
vpad1 = 400

tempoInicial = time.time()

# inicializando a pontuação
pontEsquerdo = 0
pontDireito = 0

# contador para o efeito especial
cont = 0
cont2 = 0
x = 0
y = 0
z = 0

while True:

# criando delta time
    tempoAtual = time.time()
    deltaTime = tempoAtual - tempoInicial
    tempoInicial = tempoAtual
    bolinha.x += velx*janela.delta_time()
    bolinha.y += vely*janela.delta_time()

# se a bolinha passar pros lados soma os pontos e volta ela pro meio
    if (bolinha.x < 0):
        bolinha.set_position((janela.width - bolinha.width) / 2, (janela.height - bolinha.height) / 2)
        velx = 0
        vely = 0
        pontEsquerdo += 1
    if (bolinha.x + bolinha.width > janela.width):
        bolinha.set_position((janela.width - bolinha.width) / 2, (janela.height - bolinha.height) / 2)
        vely = 0
        velx = 0
        pontDireito += 1

# se a bolinha colidir com eixo y ela volta
    if (bolinha.y < 0):
        vely *= -1
        bolinha.y += 2
    if (bolinha.y + bolinha.height > janela.height):
        vely *= -1
        bolinha.y -= 2

# colocando as teclas pra comandar os pads
    if (teclado.key_pressed("w")) and (pad2.y > 0):
        pad2.y -= vpad2 * deltaTime
    if (teclado.key_pressed("s")) and (pad2.y <= janela.height - pad2.height):
        pad2.y += vpad2 * deltaTime

    if (pad1.y > bolinha.y and abs(pad1.y - bolinha.y) > 10) and (pad1.y > 0):
        pad1.y -= vpad1 * deltaTime
    if (pad1.y < bolinha.y and abs(pad1.y - bolinha.y) > 10) and (pad1.y <= janela.height - pad2.height):
        pad1.y += vpad1 * deltaTime

# adicionado a colisão com os pads e fazendo voltar pro outro lado
    if bolinha.collided(pad2):
        velx *= -1
        bolinha.x += 1.5
        if y == 1:
            cont2 += 1
        elif z == 1:
            cont2 += 1
        else:
            cont += 1

    if bolinha.collided(pad1):
        velx *= -1
        bolinha.x -= 1.5
        if y == 1:
            cont2 += 1
        elif z == 1:
            cont2 += 1
        else:
            cont += 1

# inicializando a tecla espaço para começar o jogo
    if (teclado.key_pressed("space")):
        velx = 500
        vely = 500
        x = randint(1, 2)

    if cont == 3:
        if x == 1:
            pad1.height /= 2
            x = 0
            y = 1
        if x == 2:
            pad2.height /= 2
            x = 0
            z = 1
        x = randint(1, 2)
        cont = 0
    if cont2 == 2:
        if y == 1:
            pad1.height *= 2
            y = 0
        if z == 1:
            pad2.height *= 2
            z = 0
            cont2=0

# se atingir a pontuação o jogo acaba
    if pontEsquerdo >= 5 or pontDireito >= 5:
        time.sleep(1)
        janela.close()


# colocando nome na janela
    janela.set_title("Candy Pong")

# Chamo as imagens inicializadas no começo
    fundo.draw()
    bolinha.draw()
    pad1.draw()
    pad2.draw()

# colocando "jogador 1" e "2"
    janela.draw_text("Vicente", (janela.width /2) - 350, 30, size=30, font_name="ComicSans", bold=True,color=[255, 255, 255])
    janela.draw_text("Amélia", (janela.width / 2) + 200, 30, size=30, font_name="ComicSans", bold=True,color = [255, 255, 255])

# colocando a pontuação escrita
    janela.draw_text(str(pontDireito), (janela.width / 2) - 75, 60, size=52, font_name="ComicSans", bold=True,
                     color=[255, 255, 255])
    janela.draw_text(str(pontEsquerdo), (janela.width / 2) + 60, 60, size=52, font_name="ComicSans", bold=True,
                     color=[255, 255, 255])

# finaliza o loop
    janela.update()