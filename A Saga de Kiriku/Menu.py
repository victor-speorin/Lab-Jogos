from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
# Criando o Menu
def menu():
    # fazendo o fundo e colocando os assets das configurações no menu com suas respecitivas posições.
    janela = Window(1100, 561)
    mouse = janela.get_mouse()
    janela.set_title("MENU KIRIKU")
    fundo = GameImage("Assets\\Fundo2.jpg")
    ranking = Sprite("Assets\\BotaoRanking.png")
    jogar = Sprite("Assets\\BotaoJogar.png")
    sair = Sprite("Assets\\BotaoSair.png")
    tutorial = Sprite("Assets\\BotaoTutorial.png")
    titulo = Sprite("Assets\\Titulo.png")
    titulo.set_position(10, 10)
    jogar.set_position(68, 205)
    tutorial.set_position(68, 285)
    ranking.set_position(68, 365)
    sair.set_position(68, 445)

    while True:
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(jogar):
                game()
            if mouse.is_over_object(sair):
                janela.close()
            if mouse.is_over_object(tutorial):
                Tutorial()
        fundo.draw()
        titulo.draw()
        jogar.draw()
        sair.draw()
        tutorial.draw()
        ranking.draw()
        janela.update()


def Tutorial():
    janela = Window(1100, 619)
    mouse = janela.get_mouse()
    jump = Sprite("Assets\\Jump.png")
    djump = Sprite("Assets\\DoubleJump.png")
    w = Sprite("Assets\\W.png")
    w2 = Sprite("Assets\\W.png")
    w3 = Sprite("Assets\\W.png")
    space = Sprite("Assets\\Space.png")
    space2 = Sprite("Assets\\Space.png")
    space3 = Sprite("Assets\\Space.png")
    fundo = GameImage("Assets/TutoF.jpg")
    voltar = Sprite("Assets\\Voltar.png")
    voltar.set_position(10, 10)
    jump.set_position(750, 70)
    space.set_position(700, 140)
    w.set_position(845, 140)
    djump.set_position(750, 270)
    space2.set_position(700, 340)
    space3.set_position(845, 340)
    w2.set_position(700, 420)
    w3.set_position(845, 420)
    janela.set_title("TUTORIAL KIRIKU")
    teclado = janela.get_keyboard()
    while True:
        if teclado.key_pressed("esc"):
            menu()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(voltar):
                menu()
        fundo.draw()
        voltar.draw()
        djump.draw()
        jump.draw()
        space.draw()
        space2.draw()
        space3.draw()
        w.draw()
        w2.draw()
        w3.draw()
        janela.draw_text("or", 813, 146, size=16, font_name="Tempus Sans ITC", bold=True,
                         color=[0, 0, 0])
        janela.draw_text("or", 812, 388, size=16, font_name="Tempus Sans ITC", bold=True,
                         color=[0, 0, 0])
        janela.draw_text("and", 810, 347, size=16, font_name="Tempus Sans ITC", bold=True,
                         color=[0, 0, 0])
        janela.draw_text("and", 810, 427, size=16, font_name="Tempus Sans ITC", bold=True,
                         color=[0, 0, 0])

        janela.update()
def game():
    janela = Window(1100, 619)
    fundo = GameImage("Assets/Fundo3.jpg")
    janela.set_title("JOGAR KIRIKU")
    personagem = Sprite("Assets\\inimigo1.png")
    inimigo2 = Sprite("Assets\\inimigo2.png")
    personagem.x = (janela.width - janela.height) / 2
    personagem.y = janela.height - personagem.height
    inimigo2.x = (janela.width - janela.height) / 2
    inimigo2.y = janela.height - inimigo2.height
    comandos = Window.get_keyboard()
    velini1 = 400
    velini2 = 400
    teclado = janela.get_keyboard()
    # Define a velocidade de pulo
    velocidade_pulo = 3.5

    # Define a gravidade
    gravidade = 0.025

    # Define a velocidade vertical inicial
    velocidade_vertical = 0

    # Define se o personagem está no chão
    no_chao = True

    while True:
        fundo.draw()
        if teclado.key_pressed("esc"):
            menu()
        if (comandos.key_pressed("A")):
            personagem.x -= velini1 * janela.delta_time()
        if (comandos.key_pressed("D")):
            personagem.x += velini1 * janela.delta_time()
        if (personagem.x <= 0):
            personagem.x = 0
        if (personagem.x >= janela.width - personagem.width):
            personagem.x = janela.width - personagem.width

        if (comandos.key_pressed("left")):
            inimigo2.x -= velini2 * janela.delta_time()
        if (comandos.key_pressed("right")):
            inimigo2.x += velini2 * janela.delta_time()
        if (inimigo2.x <= 0):
            inimigo2.x = 0
        if (inimigo2.x >= janela.width - inimigo2.width):
            inimigo2.x = janela.width - inimigo2.width
            # Se a tecla de pulo for pressionada e o personagem estiver no chão
        if teclado.key_pressed("UP") and no_chao:
                # Faz o personagem pular
            velocidade_vertical = -velocidade_pulo
            no_chao = False

            # Aplica a gravidade
        velocidade_vertical += gravidade

            # Atualiza a posição vertical do personagem
        personagem.y += velocidade_vertical

            # Se o personagem estiver abaixo do chão
        if personagem.y > janela.height - personagem.height:
                # Coloca o personagem no chão
            personagem.y = janela.height - personagem.height
            no_chao = True
        personagem.draw()
        inimigo2.draw()
        janela.draw_text("0000 m", 900, 50, size=16, font_name="Tempus Sans ITC", bold=True,
                         color=[0, 0, 0])
        janela.update()

menu()
