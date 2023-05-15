from turtle import Turtle

class Pontuacao(Turtle):
    def __init__(self):
        super(Pontuacao, self).__init__()
        self.pontos = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.atualizar_pontos()

    def atualizar_pontos(self):
        self.clear()
        self.write(f"Pontos: {self.pontos}", align="center", font=("Arial", 20, "normal"))

    def aumentar_pontos(self):
        self.pontos += 1
        self.atualizar_pontos()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))
