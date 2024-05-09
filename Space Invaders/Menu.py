from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

def menu():
    janela = Window(1000, 600)
    mouse = janela.get_mouse()
    janela.set_title("MENU SPACE INVADERS VICTOR TELES")
    fundo = GameImage("assets\\fundo.png")
    jogar = Sprite("assets\\Jogar.png")
    ranking = Sprite("assets\\Ranking.png")
    dific = Sprite("assets\\Dificuldade.png")
    sair = Sprite("assets\\Sair.png")
    titulo = Sprite("assets\\titulo.png")
    titulo2 = Sprite("assets\\titulo.png")
    titulo2.set_position(35, (janela.height - titulo.height)/2)
    titulo.set_position((janela.width-titulo.width)/2 + 300, (janela.height - titulo.height)/2)
    jogar.set_position((janela.width - jogar.width) / 2, jogar.height * 2)
    ranking.set_position((janela.width - ranking.width) / 2, ranking.height * 4)
    dific.set_position((janela.width - dific.width) / 2, dific.height * 6)
    sair.set_position((janela.width - jogar.width) / 2, jogar.height * 8)


    while True:
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(jogar):
                game()
            if mouse.is_over_object(dific):
                dificuldade()
            if mouse.is_over_object(sair):
                janela.close()
        fundo.draw()
        titulo.draw()
        titulo2.draw()
        jogar.draw()
        ranking.draw()
        dific.draw()
        sair.draw()
        janela.update()

def game():
    janela = Window(1000, 600)
    fundo = GameImage("assets\\fundo.png")
    janela.set_title("JOGO SPACE INVADERS VICTOR TELES")
    teclado = janela.get_keyboard()
    while True:
        if teclado.key_pressed("esc"):
            menu()
        fundo.draw()
        janela.update()

def dificuldade():
    janela = Window(1000, 600)
    fundo = GameImage("assets\\fundo.png")
    janela.set_title("DIFICULDADES SPACE INVADERS VICTOR TELES")
    teclado = janela.get_keyboard()
    botaofacil = Sprite("assets\\facil.png")
    botaomedio = Sprite("assets\\medio.png")
    botaodificil = Sprite("assets\\dificil.png")
    botaofacil.set_position((janela.width - botaofacil.width) / 2, botaofacil.height * 2)
    botaomedio.set_position((janela.width - botaomedio.width) / 2, botaomedio.height * 5)
    botaodificil.set_position((janela.width - botaodificil.width) / 2, botaodificil.height * 8)
    while True:
        fundo.draw()
        if teclado.key_pressed("esc"):
            menu()
        botaofacil.draw()
        botaomedio.draw()
        botaodificil.draw()
        janela.update()
menu()