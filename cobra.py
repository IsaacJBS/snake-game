import random
from turtle import Turtle

class Cobra:
    POSICAO_INICIAL = [(0, 0), (0, 20), (0, 40), (0, 60), (0, 80)]
    VEL = 20
    DIREITA = 0
    ESQUERDA = 180
    CIMA = 90
    BAIXO = 270

    def __init__(self):
        self.corpo = []
        self.inicializar_cobra()
        self.cabeca = self.corpo[0]

    def mover(self):
        for segmento in range(len(self.corpo) - 1, 0, -1):
            nova_posicao = self.corpo[segmento - 1].position()
            self.corpo[segmento].goto(nova_posicao)
        self.cabeca.forward(self.VEL)

    def inicializar_cobra(self):
        for posicao in self.POSICAO_INICIAL:
            self.novo_segmento(posicao)

    def novo_segmento(self, posicao):
        nova_cobra = Turtle("square")
        nova_cobra.color(self.sorteia_cores())
        nova_cobra.penup()
        nova_cobra.goto(posicao)
        self.corpo.append(nova_cobra)

    def sorteia_cores(self):
        return random.choice(["red", "green", "blue", "purple", "orange", "yellow"])

    def mover_para_direita(self):
        if self.cabeca.heading() != self.ESQUERDA:
            self.cabeca.setheading(self.DIREITA)

    def mover_para_esquerda(self):
        if self.cabeca.heading() != self.DIREITA:
            self.cabeca.setheading(self.ESQUERDA)

    def mover_para_cima(self):
        if self.cabeca.heading() != self.BAIXO:
            self.cabeca.setheading(self.CIMA)

    def mover_para_baixo(self):
        if self.cabeca.heading() != self.CIMA:
            self.cabeca.setheading(self.BAIXO)

    def matar_cobra(self):
        for segmento in self.corpo[1:]:
            if self.cabeca.distance(segmento) < 10:
                return True
        return False

    def reset(self):
        for segmento in self.corpo:
            segmento.goto(1000, 1000)
        self.corpo.clear()
        self.inicializar_cobra()
        self.cabeca = self.corpo[0]
