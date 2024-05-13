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
    inimigo = Sprite("Assets\\inimigo1.png")
    inimigo2 = Sprite("Assets\\inimigo2.png")
    inimigo.x = (janela.width - janela.height) / 2
    inimigo.y = janela.height - inimigo.height
    inimigo2.x = (janela.width - janela.height) / 2
    inimigo2.y = janela.height - inimigo2.height
    comandos = Window.get_keyboard()
    velini1 = 400
    velini2 = 400
    teclado = janela.get_keyboard()
    while True:
        fundo.draw()
        if teclado.key_pressed("esc"):
            menu()
        if (comandos.key_pressed("A")):
            inimigo.x -= velini1 * janela.delta_time()
        if (comandos.key_pressed("D")):
            inimigo.x += velini1 * janela.delta_time()
        if (inimigo.x <= 0):
            inimigo.x = 0
        if (inimigo.x >= janela.width - inimigo.width):
            inimigo.x = janela.width - inimigo.width

        if (comandos.key_pressed("left")):
            inimigo2.x -= velini2 * janela.delta_time()
        if (comandos.key_pressed("right")):
            inimigo2.x += velini2 * janela.delta_time()
        if (inimigo2.x <= 0):
            inimigo2.x = 0
        if (inimigo2.x >= janela.width - inimigo2.width):
            inimigo2.x = janela.width - inimigo2.width
        inimigo.draw()
        inimigo2.draw()
        janela.draw_text("0000 m", 900, 50, size=16, font_name="Tempus Sans ITC", bold=True,
                         color=[0, 0, 0])
        janela.update()

menu()
