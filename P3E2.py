import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()

def funcion_costo(ni, nf, atributos_arco):
	return atributos_arco["costo"]

def dist(a,b):
    return np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

nodos = [[1,2],[4,3],[1,6],[7,3],[10,1],[0,10],[4,0],[5,8],[9,7],[8,10]]
gris=120
verde=60
cafe=40
reductor=3


G.add_node("0", pos=nodos[0])
G.add_node("1", pos=nodos[1])
G.add_node("2", pos=nodos[2])
G.add_node("3", pos=nodos[3])
G.add_node("4", pos=nodos[4])
G.add_node("5", pos=nodos[5])
G.add_node("6", pos=nodos[6])
G.add_node("7", pos=nodos[7])
G.add_node("8", pos=nodos[8])
G.add_node("9", pos=nodos[9])

G.add_edge("0","2", costo=round(dist(nodos[0],nodos[2])/gris,reductor))
G.add_edge("0","1", costo=round(dist(nodos[0],nodos[1])/cafe,reductor))
G.add_edge("0","6", costo=round(dist(nodos[0],nodos[6])/gris,reductor))
G.add_edge("2","1", costo=round(dist(nodos[2],nodos[1])/cafe,reductor))
G.add_edge("6","3", costo=round(dist(nodos[6],nodos[3])/cafe,reductor))
G.add_edge("6","4", costo=round(dist(nodos[6],nodos[4])/gris,reductor))
G.add_edge("1","3", costo=round(dist(nodos[1],nodos[3])/verde,reductor))
G.add_edge("1","7", costo=round(dist(nodos[1],nodos[7])/cafe,reductor))
G.add_edge("7","9", costo=round(dist(nodos[7],nodos[9])/verde,reductor))
G.add_edge("7","3", costo=round(dist(nodos[7],nodos[3])/verde,reductor))
G.add_edge("3","8", costo=round(dist(nodos[3],nodos[8])/cafe,reductor))
G.add_edge("3","4", costo=round(dist(nodos[3],nodos[4])/verde,reductor))
G.add_edge("9","8", costo=round(dist(nodos[9],nodos[8])/verde,reductor))
G.add_edge("8","4", costo=round(dist(nodos[8],nodos[4])/gris,reductor))
G.add_edge("5","2", costo=round(dist(nodos[5],nodos[2])/cafe,reductor))
G.add_edge("5","7", costo=round(dist(nodos[5],nodos[7])/gris,reductor))



pos = nx.get_node_attributes(G,"pos")
labels = nx.get_edge_attributes(G,"costo")

 ############################# p1 vista colorida ###################
colores = []
edgelist = []
grosor=[]
for  ni, nf in G.edges:
    if round(dist(pos[ni],pos[nf])/gris,reductor) == labels[(str(ni),str(nf))]:
        colores.append("grey")
    elif round(dist(pos[ni],pos[nf])/verde,reductor) == labels[(str(ni),str(nf))]:
        colores.append("green")
    elif round(dist(pos[ni],pos[nf])/cafe,reductor) == labels[(str(ni),str(nf))]:
        colores.append("brown")
    edgelist.append((ni,nf))
    grosor.append(2.5)

plt.figure()
plt.grid()
nx.draw_networkx_nodes(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
nx.draw_networkx_edges(G, pos, edgelist=edgelist,width=grosor, edge_color=colores)


plt.suptitle(f" Mapeado nodos y rutas")
plt.xlabel( "X (km)")
plt.ylabel( "Y (km)")
xTicks = [0,1,2,3,4,5,6,7,8,9,10]
xTicks_Text = ["0","1","2","3","4","5","6","7","8","9","10"]
plt.yticks(xTicks, xTicks_Text)
plt.xticks(xTicks, xTicks_Text)

plt.savefig("fig1.png")
plt.show()


 ############################# p2 vista rutas ###################
caminos = [[0,9],[4,5],[0,4]]
for cam in range (3):
    print ("\n"*2)
    
    path = nx.shortest_path(G, source=str(caminos[cam][0]), target=str(caminos[cam][1]), weight="costo")
    ruta = nx.dijkstra_path(G, source=str(caminos[cam][0]), target=str(caminos[cam][1]), weight=funcion_costo)
    rutas = nx.all_shortest_paths(G, source=str(caminos[cam][0]), target=str(caminos[cam][1]), weight="costo")
    
    for ruta in rutas:
        costo_ruta = 0.
        Nparadas = len(ruta)
        print(f"Ruta {cam+1}, Nparadas = {Nparadas}, ruta: {ruta}")
        for i in range(Nparadas-1):
            parada_i = ruta[i]
            parada_f = ruta[i+1]
            costo_tramo_i = G.edges[parada_i, parada_f]["costo"]
            print(f"Tramo {i}:  {parada_i} a {parada_f} costo={costo_tramo_i}")
            costo_ruta += costo_tramo_i
            
        print( f"Costo de ruta {cam+1}: {caminos[cam][0]} a {caminos[cam][1]}  =  {round(costo_ruta,5)} " )
        
        colores = []
        edgelist = []
        grosor=[]
        for ni, nf in G.edges:
            if ni in ruta and nf in ruta:
                colores.append("r")
                grosor.append(3.2)
            else:
                colores.append("k")
                grosor.append(0.8)
            edgelist.append((ni,nf))
    plt.figure()
    plt.grid()
    xTicks = [0,1,2,3,4,5,6,7,8,9,10]
    xTicks_Text = ["0","1","2","3","4","5","6","7","8","9","10"]
    plt.yticks(xTicks, xTicks_Text)
    plt.xticks(xTicks, xTicks_Text)
    plt.xlabel( "X (km)")
    plt.ylabel( "Y (km)")


    nx.draw_networkx_nodes(G, pos=pos)
    nx.draw_networkx_labels(G, pos=pos)
    nx.draw_networkx_edges(G, pos, edgelist=edgelist,width=grosor, edge_color=colores)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.suptitle(f"Ruta minima: {ruta} costo= {round(costo_ruta,5)} [horas]")
    plt.savefig(f"fig{cam+2}.png")
    plt.show()
    




