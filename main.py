# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:09:36 2017

@author: Israël e Renan
"""
#modulo de lista de adjacências
def lista_adj(vertices):
    lista={}
    for i in vertices:
        opt=1
        adj=[]
        while opt==1:
            v=int(input("adjacentes a {}\n".format(i)))
            adj.append(v)
            opt=int(input("Adicionar vizinhos\n1 para sim e 0 para não\n?"))
        lista[i]=adj
    return lista
        
def mostrar_lista(lista):
    for i in lista:
        print(i)
        
def aresta_explorada(l,marc,v,w):
    if v in l.keys():
        if w in l[v]:
            
            
vertices=[int(x) for x in input("Vértices do grafo").split()]
lista=lista_adj(vertices)
marcados=[]#lista dos vértices marcados

