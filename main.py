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
    self.widget1 = Frame(master,width=500,height=500)
    self.graph=Grafo(graph)
    self.widget1.pack()
    self.canvas=Canvas(self.widget1)
    self.canvas.pack()
    ini=input("Vértice inicial da busca:\n")
    self.graph.explorar(ini)
    seed(7)
    plotados=[]
    #plota os vértices do grafo
    for l in self.graph.get():
      sort=False
      while not sort:
        x=randint(10,200)
        y=randint(10,200)
        if (x,y) not in plotados:
          plotados.append((x,y))
          sort=True
      self.canvas.create_oval(x-10,y-10,x+10,y+10,fill="red")
      self.canvas.create_text(x,y,text=l)
      #desenha as arestas
    for i in range(1,len(plotados)):
      self.canvas.create_line(plotados[i-1][0],plotados[i-1][1],plotados[i][1],plotados[i][1])
    self.msg=Label(self.widget1,text=self.graph.get_history())
    self.msg.pack()
         
    
        
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
root.mainloop()
