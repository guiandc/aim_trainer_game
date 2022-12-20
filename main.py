import tkinter
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import time
import random

initial_parameters = {
    'x_resolution': 1024
    ,'y_resolution': 786
}

window = tkinter.Tk()
window.configure(width=initial_parameters['x_resolution'], height=initial_parameters['y_resolution'])
window.geometry("{}x{}".format(initial_parameters['x_resolution'], initial_parameters['y_resolution']))

images = {
    'background': None
    ,'target': r"./img/target.png"
}

global hit, data_inicial, data_final, hist

hit = 0
data_inicial = 0
data_final = 0
hist = []

class Target:
    def __init__(self, window, image_dir, x_max, y_max):

        #CARREGA SPRITE
        self.img = Image.open(image_dir)                                                                                #CARREGA SPRITE
        self.img_resized  = self.img.resize((int(x_max/30), int(x_max/30)))                                             #REDIMENDSIONA SPRITE
        self.my_img = ImageTk.PhotoImage(self.img_resized)                                                              #CARREGA SPRITE NO FORMATO TKINTER

        self.target = tkinter.Button(window                                                                             #INSTANCIA BOTÃO TKINTER PASSANDO: JANELA
                                     , image=self.my_img                                                                    #SPRITE
                                     , height = (x_max/30)                                                                  #ALTURA
                                     , width = (x_max/30)                                                                   #LARGURA
                                     , command=self.destroyTarget)                                                          #COMANDO PÓS CLIQUE

        self.x = random.randint(0, (x_max-int(x_max/30)))                                                               #DEFINE POSIÇÃO X ALEATÓRIA
        self.y = random.randint(0, (y_max-int(x_max/30)))                                                               #DEFINE POSIÇÃO Y ALEATÓRIA
        self.target.place(x = self.x, y = self.y)                                                                       #POSICIONA OBJETO

    def destroyTarget(self):
        self.target.destroy()                                                                                           #DESTROY TARGET

        global hit, data_inicial, data_final, hist
        hit = hit + 1

        if hit == 1:
            data_inicial = datetime.now()

        t = datetime.now() - data_inicial
        print("target: {} time since begining: {}".format(hit, t))

        if hit == 15:
            data_final = datetime.now()
            pontuação = (data_final - data_inicial)
            hist.append(str(pontuação))
            print(hist)
            hit = 0
            time.sleep(3)
            print("click to start a new game!")

        Target(window, images['target'], initial_parameters['x_resolution'], initial_parameters['y_resolution'])

Target(window, images['target'], initial_parameters['x_resolution'], initial_parameters['y_resolution'])
print("click to start a new game!")
window.mainloop()
