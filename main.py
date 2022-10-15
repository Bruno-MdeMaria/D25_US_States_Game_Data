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
    state_data = data[data.state == resposta_estado] #se o estado escolhido for igual a algum estado na tabela
    t.goto(state_data.x, state_data.y) #como a variavel receberá a linha da tabela podemos chamar os valores x e y diretamente usando a descrição da coluna.



tela.exitonclick()
#FUNÇÃO PARA ENCONTRAR AS COORDENADAS DENTRO DO MAPA:
# def local_clique(x, y):
#     print(x, y)
# turtle.onscreenclick(local_clique)
# turtle.mainloop()