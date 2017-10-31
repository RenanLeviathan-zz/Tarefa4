# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:09:36 2017
@author: Israël e Renan
"""
class Grafo:
  def __init__(self,grafo,inicial):
    self.marc=[]
    self.lista={}
    self.lista=grafo
    self.marc.append(inicial)
              
  def mostrar(self):
    print(self.lista)
#explora as arestas do grafo	
  def explorar(self):
    exp=[]
    comecou=False
    inicial=self.marc[0]
    for v in self.lista.keys():
      if v != inicial and not comecou: continue
      else: comecou=True
      if v not in self.marc: self.marc.append(v)
      for w in self.lista[v]:
        if w not in self.marc: self.marc.append(w)
        else: print("Aresta de retorno: ",(v,w))
        if (w in self.lista[v]) and (((v,w) not in exp) and ((w,v) not in exp)):
          exp.append((v,w))
          v=w
    return exp

grafo={
  'a':['b','c'],
  'b':['a','c','d','f'],
  'c':['a','b','d','e'],
  'd':['b','c','e','f'],
  'e':['c','d','f'],
  'f':['b','d','e']
  }
ini=input("Vértice inicial da busca:\n")
g=Grafo(grafo,ini)
exp=g.explorar()
print("Arestas de busca:\n")
print([i for i in exp])
