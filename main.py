import turtle

tela = turtle.Screen()

tela.title("U.S. States Game")
image = "blank_states_img.gif"
tela.addshape(image)
turtle.shape(image)

def local_clique(x, y):
    print(x, y)
turtle.onscreenclick(local_clique)
turtle.mainloop()



#tela.exitonclick()