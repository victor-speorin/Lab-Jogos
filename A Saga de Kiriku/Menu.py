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
    space = Sprite("Assets\\Space.png")
    fundo = GameImage("Assets/TutoF.jpg")
    voltar = Sprite("Assets\\Voltar.png")
    voltar.set_position(10, 10)
    jump.set_position(750, 50)
    space.set_position(750, 120)
    djump.set_position(50, -100)
    w.set_position(50, -100)
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
        w.draw()
        janela.update()
def game():
    janela = Window(1100, 619)
    fundo = GameImage("Assets/Fundo3.jpg")
    janela.set_title("JOGAR KIRIKU")
    teclado = janela.get_keyboard()
    while True:
        if teclado.key_pressed("esc"):
            menu()
        fundo.draw()
        janela.update()

def dificuldade():
    janela = Window(1000, 600)
    mouse = janela.get_mouse()
    fundo = GameImage("assets/Fundo.png")
    janela.set_title("DIFICULDADES SPACE INVADERS VICTOR TELES")
    teclado = janela.get_keyboard()
    botaofacil = Sprite("assets/facil.png")
    botaomedio = Sprite("assets/medio.png")
    botaodificil = Sprite("assets/dificil.png")
    botaofacil.set_position((janela.width - botaofacil.width) / 2, botaofacil.height * 2)
    botaomedio.set_position((janela.width - botaomedio.width) / 2, botaomedio.height * 5)
    botaodificil.set_position((janela.width - botaodificil.width) / 2, botaodificil.height * 8)

    while True:
        fundo.draw()
        if teclado.key_pressed("esc"):
            menu()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(botaofacil):
                import Main
                Main.jogar()
            if mouse.is_over_object(botaomedio):
                import Main
                Main.jogar()
            if mouse.is_over_object(botaodificil):
                import Main
                Main.jogar()
                janela.close()
        botaofacil.draw()
        botaomedio.draw()
        botaodificil.draw()
        janela.update()
menu()
