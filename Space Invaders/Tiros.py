#Importando
from PPlay.sprite import*
import random

def novo_tiro(nave, lista_de_tiros):

    tiro = Sprite("Assets//tiro.jpg", 5)
    tiro.set_sequence_time(0, 4, 300, True)

    tiro.x = nave.x + 33
    tiro.y = nave.y - tiro.height

    lista_de_tiros.append(tiro)

    return lista_de_tiros


def limitando_tiro(tiro, lista_de_tiros):
    if (tiro.y <= tiro.height * 3):
        tiro.update()

    if (tiro.y <= 0):
        lista_de_tiros.remove(tiro)