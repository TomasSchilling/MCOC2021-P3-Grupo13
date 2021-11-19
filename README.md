# MCOC2021-P3-Grupo13
un crack de MCOC

Grupo numero 13
Integrantes: Tomas Schilling A


ENTREGA 2

![grafico1](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/fig1.png)
![grafico2](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/fig2.png)
![grafico3](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/fig3.png)
![grafico4](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/fig4.png)


ENTREGA 3
Grafico del unico integrante Tomas Schilling
![grafico5](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/Mapa%20casi%20bonito.png)


Entrega 4
Para la entrega se asigno un equilibrio porcentual para cada demanda. EN primer intancia se asignaron flujos usando un 1% de la demanda exigida. 
Luego, cuando la demanda se encuentra en un 90% de lo exigido finalmente, se aprixmima entregando un 0.1% para cada iteracion. con el fin de no
perturbas las deciciones finas en el sistema.
En las lineas 15-45 se definen los parametros del sistema. El ciclo continuo donde se resuelve la asignacion de la matriz OD se contembla desde 65-95,
dondesi la demanda que queda es menor al 90% del total (para cada  par prigen-destino) se itera con un 1% de la demanda inicial. Cuando se sobrepasa este
valor se utiliza la exigencia/10.000. luego se le asigna y se actualizan los valores de la demanda restante.

En los graficos se ensenna el costo y el fjujo sobre cada ruta

![grafico6](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/Figure_Costos.png)
![grafico7](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/Figure_Flujos.png)

Para revisar que se respetan el trafico de vehiculos sobre la matriz OD se calculo el flujo entrante y saliente en cada nodo,
lo que se puede ver en el print() de al final del codigo. Al analizar los resultados se comprbuena que la matriz entrega valores casi identicos a los resutos por el profesor,
la diferencia, si bien es marginal para la escala del numero (0.1%, 0.01%) puede deberse a la resta de los valores, que estan sobre un arcivo float 16, que al ser evaluado 1000 veces presenta estas diferencias marginales, que se acumulan para cada iteracion.


Entrega 5
Para esta entrega se analizo la matroz origen destino. se reducionren segmentos de esta matriz en tanto no tengan una influencia en la zona de analisis. Se puede contemplar una vista geografica de una seccion del mapa o grafo a utilizar, donde se representan por colores, de naranjo para autopistas, amarillo para calles primarias, verde para calles secundarias, azul para terciarias y en rojo, se reprezenta la zona de contruccion de AVO.:
![https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/vista%20calle.png)


¿Cómo seleccionó las zonas a incluir?
Para la selaccion se dejo la matriz en su format ooriginal. se eliminaron primero, todos los viajes que provengan y se dirijan al mismo sector. eg, 457 --> 457. Tambien se eliminaron sobre varias comunas el transito interno( comunas no aledanas a AVO, vease LURARES_OUT ). Tambien en distintos sectores, se eliminaron los viajes entre macrozonas las cuales no alteran el flujo de AVO. a continuacion se muestran las  imagenes de las macrozonas eliminadas:
![grafico6](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/Z_Centro.png)  ![grafico6](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/Z_cennorte.png)  ![grafico6](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/Z_estenor.png)  ![grafico6](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/Z_oeste.png) ![grafico7](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/Z_sur.png)
Y de las comunas, las cuales se analizan por separado. no se descartan viajes entre comunas; permanecen intactas:
![grafico7](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/Total.png) ![grafico7](https://github.com/TomasSchilling/MCOC2021-P3-Grupo13/blob/main/vista%20cercana.png)

¿Cuántas zonas quedaron seleccionadas son?
como se menciono anteriormente, no se eliminaron zonas en especifico, mas bien espacios de la matriz OD. si bien eesto generara una mayor demanda computacional, promueve resutados mas realistas sobre el analisis, puesto que viejas entre comunas de mayo dsitancia pueden ser exelentes casos para el uso de AVO.

¿Cuántos viajes deberá asignar?
la matriz OD oroginalmente es de 2832 pares. con la reduccion quedo a 922, lo que equivale a un 33% aproimandamente del total.

¿Cuales son los pares OD que espera Ud. que generen mayor flujo en AVO?
la mayor cantidad de viajes que se esperan recibir son los que van ded norte a sur, por el lado este y los que conectan las comunas de vitacura, las condes, la reina con zonas mas alejadas de santiago.




