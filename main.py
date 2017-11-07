# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:09:36 2017
Busca em profundidade
@author: Israël e Renan
"""
from Graph import *
from tkinter import *
from random import *
class Main:
  def __init__(self,master=None,graph=None):
    self.widget1 = Frame(master,width=600,height=500)
    self.graph=Grafo(graph)
    self.widget1.pack()
    self.canvas=Canvas(self.widget1,width=500,height=500)
    self.canvas.pack(side=RIGHT)
    ini=input("Vértice inicial da busca:\n")
    self.graph.explorar(ini)
    seed(7)
    pares=[]
    plot={}
    #posiciona os vértices no canvas
    for v in self.graph.get():
      x=randint(10,100)
      y=randint(10,100)
      plot[v]=(x*5,y*5)
    #organiza os pares
    for i in self.graph.get():
      for j in self.graph.get()[i]:
        if ((i,j) not in pares) and ((j,i) not in pares):
          pares.append((i,j))
    for p in pares:
      #primeiro vértice do par
      self.canvas.create_oval(plot[p[0]][0]-10,plot[p[0]][1]-10,plot[p[0]][0]+10,plot[p[0]][1]+10,fill="red")
      self.canvas.create_text(plot[p[0]][0],plot[p[0]][1],text=p[0])
      #segundo vértice do par
      self.canvas.create_oval(plot[p[1]][0]-10,plot[p[1]][1]-10,plot[p[1]][0]+10,plot[p[1]][1]+10,fill="red")
      self.canvas.create_text(plot[p[1]][0],plot[p[1]][1],text=p[1])
      #criando linhas
      self.canvas.create_line(plot[p[0]][0],plot[p[0]][1],plot[p[1]][0],plot[p[1]][1])
    self.msg=Label(self.widget1,text=self.graph.get_history())
    self.msg.pack(side=LEFT)
         
    
        
grafo={
  'a':['b','c'],
  'b':['a','c','d','f'],
  'c':['a','b','d','e'],
  'd':['b','c','e','f'],
  'e':['c','d','f'],
  'f':['b','d','e']
  }
#visualização do grafo
root=Tk()
Main(root,grafo)
root.title("Busca em Profundidade")
root.mainloop()
