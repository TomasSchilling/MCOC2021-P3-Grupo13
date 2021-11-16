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
