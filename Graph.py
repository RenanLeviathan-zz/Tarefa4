class Grafo:
  def __init__(self,grafo):
    self.marc=[]
    self.lista={}
    self.lista=grafo
    self.exp=[]
    self.history=""
              
  def get(self):
    return self.lista
    
  def get_history(self):
    return self.history
#explora as arestas do grafo    
  def explorar(self,v):
    self.marc.append(v)
    for w in self.lista[v]:
      if w not in self.marc:
        self.history+="Aresta de busca: ({},{})\n".format(v,w)
        self.exp.append((v,w))
        self.marc.append(w)
        self.explorar(w)
      else:
        if ((v,w) not in self.exp) and ((w,v) not in self.exp):
          self.history+="Aresta de retorno: ({},{})\n".format(v,w)
          self.exp.append((v,w))
