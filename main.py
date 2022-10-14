import turtle
import pandas


tela = turtle.Screen()

tela.title("U.S. States Game")
image = "blank_states_img.gif"
tela.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
todos_estados = data.state.to_list()
print(todos_estados)


resposta_estado = tela.textinput(title="Escolha um estado", prompt="Qual o nome do estado?: ")

if resposta_estado == todos_estados:
    t = turtle.Turtle() #cria uma turtle
    t.hideturtle()    #esconde turtle
    t.penup()
    t.goto()



tela.exitonclick()
#FUNÇÃO PARA ENCONTRAR AS COORDENADAS DENTRO DO MAPA:
# def local_clique(x, y):
#     print(x, y)
# turtle.onscreenclick(local_clique)
# turtle.mainloop()