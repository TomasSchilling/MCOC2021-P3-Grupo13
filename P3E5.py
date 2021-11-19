import networkx as nx
import geopandas as gps
import osmnx as ox
import matplotlib.pyplot as plt
import numpy as np

def costo(q,L,k):
    return L/k["v"] + (k["u"]-5)*12 + 900*( 10*q-k["u"]*k["p"]+np.sqrt( 
        (10*q-k["u"]*k["p"])**2+ q/9  )  ) /(k["u"]*k["p"])




def transformar (lugar):
    lista=[]
    for i in range(lugar[0],lugar[1]+1):
        lista.append(str(i))
    return lista

def unificar(Gran_lista):
    lista_entrega=[]
    for lista in Gran_lista:
        for i in lista:
            lista_entrega.append(i)
    return lista_entrega

def chequeo_singular(Gran_lista,OR,DE):
    for lista in Gran_lista:
        
        if OR in lista and DE in lista:
            return True
    return False

def chequeo_comparativo(Gran_lista,OR,DE):
    if OR in Gran_lista and DE in Gran_lista:
        return True
    return False





lugares0 = [1,52]     #centro
lugares1 = [53,68]    #sur oeste
lugares2 = [69,82]    #oeste
lugares3 = [83,102]   #centro-norte
lugares4 = [103,119]  #sur
lugares5 = [120,142]  #oeste
lugares6 = [143,156]  #la piramide
lugares7 = [157,171]  #centro
lugares8 = [172,188]  #sur
lugares9 = [189,264]  #sur este
lugares9_1=[300,323]  #este norte
lugares10 = [324,336] #norte-este
lugares11 = [337,347] #sur oeste
lugares12 = [348,359] #sur oeste
lugares12_1=[360,377] #sur este
lugares13 = [378,418] #sur oeste
lugares13_1=[419,448] #centro-este
lugares14 = [449,465] #centro sur
lugares14_1=[466,493] #este
lugares14_2=[494,516] #centro este
lugares15 = [517,556] #oeste
lugares16 = [557,577] #oeste
lugares16_1=[578,601] #centro norte
lugares17_1=[602,618] #oeste
lugares17 = [619,665] #sur
lugares17_2=[666,684] #este
lugares18 = [685,727] #bien sur1
lugares19 = [728,757] #norte
lugares20 = [758,1000]#sur afuera


lugares0 = transformar(lugares0)
lugares1 = transformar(lugares1)
lugares2 = transformar(lugares2)
lugares3 = transformar(lugares3)
lugares4 = transformar(lugares4)
lugares5 = transformar(lugares5)
lugares6 = transformar(lugares6)
lugares7 = transformar(lugares7)
lugares8 = transformar(lugares8)
lugares9 = transformar(lugares9)
lugares9_1= transformar(lugares9_1)
lugares10 = transformar(lugares10)
lugares11 = transformar(lugares11)
lugares12 = transformar(lugares12)
lugares12_1= transformar(lugares12_1)
lugares13 = transformar(lugares13)
lugares13_1= transformar(lugares13_1)
lugares14 = transformar(lugares14)
lugares14_1 = transformar(lugares14_1)
lugares14_2 = transformar(lugares14_2)
lugares15 = transformar(lugares15)
lugares16 = transformar(lugares16)
lugares16_1 = transformar(lugares16_1)
lugares17 = transformar(lugares17)
lugares17_1=transformar(lugares17_1)
lugares17_2=transformar(lugares17_2)
lugares18 = transformar(lugares18)
lugares19 = transformar(lugares19)
lugares20 = transformar(lugares20)

ZONA_SUR1_OESTE= unificar([lugares0,lugares1,lugares2,lugares4,lugares5,lugares8,lugares9,lugares11,lugares12,
                          lugares12_1,lugares13,lugares14,lugares16, lugares17,lugares18,lugares20 ])
ZONA_CENTRO  =unificar( [lugares0,lugares3,lugares7,lugares13_1,lugares14_2,lugares16,lugares16_1] )
ZONA_CEN_NOR =unificar( [lugares0,lugares2,lugares3,lugares5,lugares6,lugares7,lugares12,lugares15,lugares16,lugares16_1,lugares17_1,lugares19])
ZONA_NOR_EST =unificar( [lugares9_1, lugares10, lugares17_2])
ZONA_OESTE   =unificar( [ lugares0, lugares1,lugares2,lugares5,lugares7,lugares11,lugares12,lugares13,lugares15, lugares16 ,lugares16_1,lugares17_1 ,lugares19    ])

LURARES_OUT =[lugares0,lugares1,lugares2,lugares3,lugares4,lugares5,lugares6,lugares7,
          lugares8,lugares9,lugares10,lugares11,lugares12,lugares12_1,lugares13,lugares14,lugares14_1,lugares14_2,lugares15,
          lugares16,lugares16_1,lugares17,lugares17_1,lugares17_2,lugares18,lugares19,lugares20]


Datos_OD_crudo= open("mod.csv")
Matriz_OD= {}
a=0
for i in Datos_OD_crudo:
    a+=1
    linea= i.strip("\n").split(",")
    if linea[0]==linea[1]:
        continue
    if linea[0]== "0" or linea[1]=="0":
        continue
    if chequeo_singular(LURARES_OUT,linea[0],linea[1]):
        continue
    if chequeo_comparativo(ZONA_SUR1_OESTE,linea[0],linea[1]):
        continue
    if chequeo_comparativo(ZONA_CENTRO,linea[0],linea[1]):
        continue
    if chequeo_comparativo(ZONA_CEN_NOR,linea[0],linea[1]):
        continue
    if chequeo_comparativo(ZONA_NOR_EST,linea[0],linea[1]):
        continue
    if chequeo_comparativo(ZONA_OESTE,linea[0],linea[1]):
        continue

    Matriz_OD[linea[0], linea[1]] = float(linea[2])
    
Datos_OD_crudo.close()

LURARES_OUT1= unificar(LURARES_OUT)

zonas_gdf = gps.read_file("eod.json")

fig,ax = plt.subplots(1,1)
area=[]
for i in range (685,757):
    area.append(i)
id_Zonas_graficar = area

el_especial = [146,666,682,683,677,306,287,307,288,289,290,304,291,266,269,434,435,
            281,426,283,440,278,439,471,267]


for i,z in enumerate(id_Zonas_graficar):# no me pregunten pero me funciono solo si es un str()
    id_Zonas_graficar[i]= str(z)        # y no un int() (no lo reconoce sino y no lo anexa)
for i,z in enumerate(el_especial):
    el_especial[i]= str(z)

zonas_seleccionadas= zonas_gdf[ zonas_gdf.id.isin( ZONA_NOR_EST )]
zonas_seleccionadas_cen=zonas_gdf[ zonas_gdf.id.isin( el_especial )]
centroides_seleccionados = zonas_seleccionadas.centroid
centroides_seleccionados_cen = zonas_seleccionadas_cen.centroid

"""
for i, dato in zonas_seleccionadas.iterrows():
    c=dato.geometry.centroid
    ax.annotate(text=dato["id"],xy=(c.x,c.y))

for i, dato in zonas_seleccionadas_cen.iterrows():
    c=dato.geometry.centroid
    ax.annotate(text=dato["id"],xy=(c.x,c.y))

#zonas_seleccionadas.plot(ax=ax, color= "grey")
#zonas_seleccionadas_cen.plot(ax=ax, color= "salmon")
#centroides_seleccionados.plot(ax=ax,marker = "o", color="red",   markersize=1)
"""

norte= -33.38
sur= -33.55
este = -70.5
oeste = -71

ox.config(use_cache=True, log_console=True)
G= ox.graph_from_bbox(north=norte,south=sur,east=este,west=oeste,network_type="drive",
                      clean_periphery=True, custom_filter=('["highway"~"motorway|primary|secondary|construction|tertiary"]'))
gdf_nodes,gdf_edges = ox.graph_to_gdfs(G)


gdf_edges[gdf_edges.highway=="motorway"].plot(ax=ax,color="orange")
gdf_edges[gdf_edges.highway=="primary"].plot(ax=ax,color="yellow")
gdf_edges[gdf_edges.highway=="secondary"].plot(ax=ax,color="green")
gdf_edges[gdf_edges.highway=="tertiary"].plot(ax=ax,color="blue")
gdf_edges[gdf_edges.highway=="construction"].plot(ax=ax,color="red")

#gdf_edges.clip(zonas_seleccionadas.geometry)
#zonas_borde = gps.clip(gdf=gdf_edges ,mask=zonas_seleccionadas.geometry[:])

plt.show()