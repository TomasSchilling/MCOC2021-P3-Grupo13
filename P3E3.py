import networkx as nx
import geopandas as gps
import osmnx as ox
import matplotlib.pyplot as plt

zonas_gdf = gps.read_file("eod.json")

fig,ax = plt.subplots(1,1)

el_especial = 674
id_Zonas_graficar =[ 326,324,673,681,680,675,684,672,676,674  ]
for i,z in enumerate(id_Zonas_graficar):# no me pregunten pero me funciono solo si es un str()
    id_Zonas_graficar[i]= str(z)        # y no un int() (no lo reconoce sino y no lo anexa)


zonas_seleccionadas= zonas_gdf[ zonas_gdf.id.isin( id_Zonas_graficar )]
zonas_seleccionadas_cen=zonas_gdf[ zonas_gdf.id.isin( ["674"] )]

centroides_seleccionados = zonas_seleccionadas.centroid
centroides_seleccionados_cen = zonas_seleccionadas_cen.centroid



for i, dato in zonas_seleccionadas.iterrows():
    c=dato.geometry.centroid
    ax.annotate(text=dato["id"],xy=(c.x,c.y))
    

for i, dato in zonas_seleccionadas_cen.iterrows():
    c=dato.geometry.centroid
    ax.annotate(text=dato["id"],xy=(c.x,c.y))


zonas_seleccionadas.plot(ax=ax, color= "grey")
zonas_seleccionadas_cen.plot(ax=ax, color= "salmon")
centroides_seleccionados.plot(ax=ax,marker = "o", color="red",   markersize=4)


norte= -33.28
sur= -33.41
este = -70.615
oeste = -70.51

ox.config(use_cache=True, log_console=True)
G= ox.graph_from_bbox(north=norte,south=sur,east=este,west=oeste,network_type="drive",clean_periphery=True)
gdf_nodes,gdf_edges = ox.graph_to_gdfs(G)

colores=[]
for n,i in gdf_edges.iterrows():
    if i["highway"] == "motorway":
        colores.append("red")
    elif i["highway"] == "secondary":
        colores.append("yellow")
    elif i["highway"] == "tertiary":
        colores.append("blue")
    elif i["highway"] == "primary":
        colores.append("green")
    elif i["highway"] == "residential":
        colores.append("black")
    else:
        colores.append("brown")


#gdf_edges.clip(zonas_seleccionadas.geometry)
gdf_edges.plot(ax=ax, color= colores[:])

#zonas_borde = gps.clip(gdf=gdf_edges ,mask=zonas_seleccionadas.geometry[:])

plt.show()
