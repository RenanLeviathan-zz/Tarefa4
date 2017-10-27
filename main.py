# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:09:36 2017
@author: Israël e Renan
"""
class Grafo:
	def __init__(self,vertices,inicial):
		self.marc=[]
		self.lista={}
		self.marc.append(inicial)
		for v in vertices:
			w=[x for x in input("Adjacentes a {}:\n".format(v)).split()]
			self.lista[v]=w
			
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
				if (w in self.lista[v]) and (((v,w) not in exp) and ((w,v) not in exp)):
					exp.append((v,w))
					v=w
		return exp
   
vertices=[x for x in input("Vértices do grafo:\n").split()]
ini=input("Vértice inicial da busca:\n")
g=Grafo(vertices,ini)
exp=g.explorar()
g.mostrar()
print([i for i in exp])
