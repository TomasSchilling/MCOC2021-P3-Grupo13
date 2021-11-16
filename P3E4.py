import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.DiGraph()

def costo(i,j, prop):
    fn_arco = prop["costo"]
    fjo_arco = prop["flujo"]
    a= fn_arco(fjo_arco)
    prop["valor"]= a
    return  a



f1= lambda f :10 + f/120.
f2= lambda f :14 + 3*f/240.
f3= lambda f :10 + f/240.


nodos=[ [0,0], [0,-1], [1.5,-1], [1.5,-2], [3,0], [3,-1]] 
Matriz_OD = { ("A","C") :1100, ("A","D") :1110, ("A","E") :1020, 
              ("B","C") :1140, ("B","D") :1160,
              ("C","E") :1170, ("C","G") :1180,
              ("D","C") :350,  ("D","E") :1190, ("D","G") :1200 }
Matriz_OD_respaldo= Matriz_OD.copy()

G.add_node("A", pos=nodos[0])
G.add_node("B", pos=nodos[1])
G.add_node("C", pos=nodos[2])
G.add_node("D", pos=nodos[3])
G.add_node("E", pos=nodos[4])
G.add_node("G", pos=nodos[5])

G.add_edge("A","B",nombre= "r" ,costo=f1, flujo=0, valor=0)
G.add_edge("A","C",nombre= "s" ,costo=f2, flujo=0, valor=0)
G.add_edge("B","C",nombre= "t" ,costo=f3, flujo=0, valor=0)
G.add_edge("B","D",nombre= "u" ,costo=f2, flujo=0, valor=0)
G.add_edge("D","C",nombre= "v" ,costo=f1, flujo=0, valor=0)
G.add_edge("C","E",nombre= "w" ,costo=f2, flujo=0, valor=0)
G.add_edge("C","G",nombre= "x" ,costo=f3, flujo=0, valor=0)
G.add_edge("D","G",nombre= "y" ,costo=f2, flujo=0, valor=0)
G.add_edge("G","E",nombre= "z" ,costo=f1, flujo=0, valor=0)



pos = nx.get_node_attributes(G,"pos")
label= nx.get_edge_attributes(G,"costo")
Dic_costo= nx.get_edge_attributes(G,"costo")


color=[]
for i in Dic_costo :
    if Dic_costo[i] ==f1: 
        color.append("tomato")
        label[i]= "f1= 10+ f/120"
    if Dic_costo[i] ==f2: 
        color.append("aqua")
        label[i]= "f2= 14+ 3*f/240"
    if Dic_costo[i] ==f3: 
        color.append("lime")
        label[i]= "f3= 10+ f/240"
        
continuar = True
termino= len(Matriz_OD)

while continuar:

    for path in Matriz_OD:
        if Matriz_OD[path] <= 0:
            continue
        
        origen =  path[0]
        destino = path[1]
        
        if Matriz_OD_respaldo[path]/Matriz_OD[path] <10:
            cantidad= Matriz_OD_respaldo[path]/100
        else:
            cantidad= Matriz_OD_respaldo[path]/10000
        
        camino = nx.algorithms.shortest_path (G, origen,destino, weight=costo)
        tramos= len(camino)
        
        for i in range(tramos-1):
            ni= camino[i]
            nj= camino[i+1]
            G.edges[ni,nj]["flujo"] +=cantidad
        Matriz_OD[path] -= cantidad
        
        if Matriz_OD[path] <=0.:
            termino-=1
            
    if  termino ==0 :
        continuar = False

flujos  = nx.get_edge_attributes(G,"flujo")

valores = nx.get_edge_attributes(G,"valor")


for i in valores:
    valores[i] = round( valores[i],3)
    flujos[i]  = round( flujos[i],2)


plt.figure(1)
plt.suptitle("Flujo en cada tramo")
plt.grid()
nx.draw_networkx_nodes(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
nx.draw_networkx_edges(G, pos, width=2 , edge_color=color)
nx.draw_networkx_edge_labels(G, pos, edge_labels=flujos)
plt.show()

plt.figure(2)
plt.suptitle("Costo en cada tramo")

plt.grid()
nx.draw_networkx_nodes(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
nx.draw_networkx_edges(G, pos, width=2 , edge_color=color)
nx.draw_networkx_edge_labels(G, pos, edge_labels=valores)
plt.show()



letras= [ "A","B","C","D","E","G" ]
Matriz_verificadora=np.zeros((len(letras),len(letras)))

for i,l1 in enumerate(letras):
    for j,l2 in enumerate(letras):
        try:
            Matriz_verificadora[i,j] += flujos[l1,l2]
        except :
            continue

Origen =np.zeros(len(letras))
Destino =np.zeros(len(letras))

for i in range (len(letras)):
    Origen = Origen+ Matriz_verificadora[:,i]
    Destino= Destino+Matriz_verificadora[i,:]
Puntos= Origen-Destino
print("en el vector puntos se muestra el flujo entrante - saliente")
print(letras)
print(Puntos)
