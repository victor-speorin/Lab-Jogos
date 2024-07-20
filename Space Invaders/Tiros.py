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
        return None  # Retorna None se o tiro foi removido

    return tiro  # Retorna o tiro se ele não foi removido

def tiro_monstro(monsters, disparos_monstros, max_tiros):
    # Obter uma lista plana de todos os monstros
    todos_monstros = [monster for row in monsters for monster in row]
    # Embaralhar a lista para obter uma ordem aleatória
    random.shuffle(todos_monstros)
    # Selecionar um subconjunto de monstros para atirar
    monstros_atiradores = todos_monstros[:max_tiros]

    for monster in monstros_atiradores:
        tiro = Sprite("Assets\\TiroIn.jpg")
        tiro.x = monster.x + monster.width / 2
        tiro.y = monster.y + monster.height
        disparos_monstros.append(tiro)

    return disparos_monstros

# Função para mover os tiros dos monstros
def move_tiros_monstros(disparos_monstros, delta_time, altura, veltiro):
    for tiro in disparos_monstros[:]:
        tiro.y += veltiro * delta_time
        if tiro.y > altura:  # Se o tiro sair da tela, remova-o
            disparos_monstros.remove(tiro)
    return disparos_monstros

