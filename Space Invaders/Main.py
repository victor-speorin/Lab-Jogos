# Importando
import Tiros
from PPlay.sprite import Sprite
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *



def criamonstros(lin, cols, spacing, screen_width):
    monsters = []
    start_x = spacing // 2
    start_y = 50
    for i in range(lin):
        row = []
        for j in range(cols):
            monster = Sprite('Assets\\inimigo1.png')
            monster.x = start_x + j * (monster.width + spacing)
            monster.y = start_y + i * (monster.height + spacing)
            row.append(monster)
        monsters.append(row)
    return monsters

def monstroslimite(monsters, player):
    for row in monsters:
        for monster in row:
            if monster.y + monster.height >= player.y:
                return True
    return False

def desenhamonstros(monsters):
    for row in monsters:
        for monster in row:
            monster.draw()
def move_monsters(monsters, direction, delta_time, screen_width):
    vel = 300  # velocidade dos monstros
    move_monstro = False

    # Verificar colisões com as bordas da tela
    for row in monsters:
        for monster in row:
            if direction == "right" and monster.x + monster.width >= screen_width:
                direction = "left"
                move_monstro = True
            elif direction == "left" and monster.x <= 0:
                direction = "right"
                move_monstro = True

  # Movimentar monstros
    for row in monsters:
        for monster in row:
            if direction == "right":
                monster.x += vel * delta_time
            else:
                monster.x -= vel * delta_time
    # Mover para baixo se necessário
    if move_monstro:
        for row in monsters:
            for monster in row:
                monster.y += monster.height // 2
    return direction

# Criando a função principal que será chamada no código do menu e virá para a tela do jogo.
def jogar():
    # Criando a janela
    janela = Window(1000, 600)
    janela.set_title("Space Invaders")

    fundo = Sprite("Assets/Fundo.png", 1)
    fundo.x = 0
    fundo.y = 0

    largura = 1000
    altura = 600

    # Criando a variável de comandos
    comandos = Window.get_keyboard()

    c=0

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


    # Crie os monstros
    rows = 5
    cols = 10
    spacing = 20
    monsters = criamonstros(rows, cols, spacing, largura)

    # Variável para controlar a direção dos monstros

    monster_direction = "right"

    # Loop
    while True:
        delta_time = janela.delta_time()

        # Conto o fps
        clock.tick(FPS)


        # Se o esc for apertado, retorna para o menu
        if comandos.key_pressed('esc'):
            import Menu
            Menu.menu()
        fundo.draw()

        # COMANDOS RELACIONADOS A NAVE:

        # Movimentação
        if (comandos.key_pressed("A") or comandos.key_pressed("left")):
            nave.x -= velnave * janela.delta_time()
        if (comandos.key_pressed("D") or comandos.key_pressed("right")):
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

                # Verificar colisão com monstros
                if d is not None:
                    for row in monsters[:]:
                        for monster in row[:]:
                            if d.collided(monster):
                                row.remove(monster)
                                disparos.remove(d)
                                c+=1
                                break  # Sai do loop interno
                        else:
                            continue  # Continua se o loop interno não foi quebrado
                        break  # Quebra o loop externo se o loop interno foi quebrado

        # Mover e desenhar os monstros
        monster_direction = move_monsters(monsters, monster_direction, delta_time, largura)
        # Desenhe os monstros
        desenhamonstros(monsters)

        # Verificar se os monstros alcançaram o jogador
        if monstroslimite(monsters, nave):
            gameover()

        if c==50:
            gamewin()

        janela.draw_text("score:" + str(int(c)), (janela.width /2) - 420, 30, size=25, font_name="Courier New", bold=True,
                         color=[255, 255, 255])

        nave.draw()
        janela.update()

def gameover():
    janela = Window(1000, 563)
    fundo = GameImage("Assets/FundoGO.jpg")
    janela.set_title("GAME OVER")
    mouse = janela.get_mouse()
    teclado = janela.get_keyboard()
    botaojogar = Sprite("Assets\\Jogar.png")
    botaosair = Sprite("Assets\\Sair.png")
    botaojogar.set_position((janela.width - botaojogar.width) / 2, botaojogar.height * 1.5)
    botaosair.set_position((janela.width - botaosair.width) / 2, botaosair.height * 6.7)
    while True:
        fundo.draw()
        botaojogar.draw()
        botaosair.draw()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(botaojogar):
                import Menu
                Menu.menu()
            if mouse.is_over_object(botaosair):
                janela.close()
        if teclado.key_pressed("esc"):
            import Menu
            Menu.menu()
        janela.update()

def gamewin():
    janela = Window(1000, 750)
    fundo = GameImage("Assets/FundoV.png")
    janela.set_title("VITORIA")
    mouse = janela.get_mouse()
    teclado = janela.get_keyboard()
    botaojogar = Sprite("Assets\\Jogar.png")
    botaosair = Sprite("Assets\\Sair.png")
    botaojogar.set_position((janela.width - botaojogar.width) / 2, botaojogar.height * 1.5)
    botaosair.set_position((janela.width - botaosair.width) / 2, botaosair.height * 6.7)
    while True:
        fundo.draw()
        botaojogar.draw()
        botaosair.draw()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(botaojogar):
                import Menu
                Menu.menu()
            if mouse.is_over_object(botaosair):
                janela.close()
        if teclado.key_pressed("esc"):
            import Menu
            Menu.menu()
        janela.update()

