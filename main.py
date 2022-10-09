import turtle

tela = turtle.Screen()

tela.title("U.S. States Game")
image = "blank_states_img.gif"
tela.addshape(image)
turtle.shape(image)

#FUNÇÃO PARA ENCONTRAR AS COORDENADAS DENTRO DO MAPA:
# def local_clique(x, y):
#     print(x, y)
# turtle.onscreenclick(local_clique)
# turtle.mainloop()

resposta_estado = tela.textinput(title="Escolha um estado", prompt="Qual o nome do estado?: ")



tela.exitonclick()