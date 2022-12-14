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

estados_adivinhados = []

while len(estados_adivinhados) < 50: #enquanto a quantidade(len) de estados advinhados for menor que 50:
    resposta_estado = tela.textinput(title=f"{len(estados_adivinhados)}/50 State Correct", prompt="Qual o nome do estado?: ").title() #o .title torna dota a primeira letra em maisculo igual oq está em nossa planilha(.data).
    print(resposta_estado)

    if resposta_estado == "Exit":  #quando escrever "exit" 
        estados_faltantes =[estado for estado in todos_estados if estado not in estados_adivinhados]
        #quando solicitar a saida será verificado e apresentado quais estados faltam
        #para cada estado no loop não estiver na lista de adivinhados ele será acrescentado na lista estados_faltantes:
        novo_data = pandas.DataFrame(estados_faltantes) #criando um novo dataframe com os estados faltantes
        novo_data.to_csv("estados_esquecidos.csv") #com o dataframe criado podemos criar um arquivo csv.
        break
       

        
    if resposta_estado in todos_estados:   #se a resposta estiver dentro da planilha:
        estados_adivinhados.append(resposta_estado)
        t = turtle.Turtle() #cria uma turtle
        t.hideturtle()    #esconde turtle
        t.penup()
        state_data = data[data.state == resposta_estado] #se o estado escolhido for igual a algum estado na tabela
        t.goto(int(state_data.x),int(state_data.y)) #como a variavel receberá a linha da tabela podemos chamar os valores x e y diretamente usando a descrição da coluna.
        t.write(resposta_estado)  #método de escrita da turtle irá escrever a escolha no local correto.





#FUNÇÃO PARA ENCONTRAR AS COORDENADAS DENTRO DO MAPA:
# def local_clique(x, y):
#     print(x, y)
# turtle.onscreenclick(local_clique)
# turtle.mainloop()