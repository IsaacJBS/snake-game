import time
from turtle import Screen
from campo import Campo
from cobra import Cobra
from maca import Maca
from pontuacao import Pontuacao

tela = Screen()

tela.title("Snake game")
tela.setup(width=600, height=620)
tela.tracer(0)
tela.bgcolor("beige")

campo = Campo()
cobra = Cobra()
maca = Maca()
pontuacao = Pontuacao()

tela.listen()
tela.onkey(cobra.mover_para_cima, "Up")
tela.onkey(cobra.mover_para_baixo, "Down")
tela.onkey(cobra.mover_para_direita, "Right")
tela.onkey(cobra.mover_para_esquerda, "Left")

jogo_on = True
while jogo_on:
    time.sleep(0.1)
    if cobra.cabeca.distance(maca) < 20:
        maca.nova_maca()
        cobra.novo_segmento(cobra.corpo[-1].position())
        pontuacao.aumentar_pontos()

    cobra.mover()

    if cobra.matar_cobra():
        jogo_on = False
        pontuacao.game_over()
        cobra.reset()
        print("Fim de jogo")
        time.sleep(2)
        # reiniciar o jogo
        jogo_on = True
        pontuacao.reset()
        cobra.reset()
        cobra.mover()

    if cobra.cabeca.xcor() > 285 \
            or cobra.cabeca.xcor() < -285 \
            or cobra.cabeca.ycor() > 285 \
            or cobra.cabeca.ycor() < -285:
        jogo_on = False
        pontuacao.game_over()
        jogo_on = True
        pontuacao.reset()
        cobra.reset()
        print("Fim de jogo")
        time.sleep(2)
        cobra.mover()

    tela.update()

tela.exitonclick()
