# lecturas archivo.csv de estación meteorológica
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#INGRESO
narchivo = "C:\\xampp\\htdocs\\phaser\\Mia.txt"
 
#PROCEDIMIENTO
tabla = pd.read_csv(narchivo, sep=';',decimal=',')
n = len(tabla)



# # Cargar los datos desde el CSV
# df = pd.read_csv('C:\\xampp\\htdocs\\phaser\\Mia.txt', header=None, names=['x1', 'x2', 'target'], dtype=float )

# # Crear la figura
# fig = plt.figure()

# # Agregar un subplot 3D
# ax = fig.add_subplot(111, projection='3d')

# # Graficar los puntos tridimensionales
# ax.scatter(df['x1'], df['x2'], df['target'], c='r', marker='o')

# # Etiquetas de los ejes
# ax.set_xlabel('x1')
# ax.set_ylabel('x2')
# ax.set_zlabel('Target')

# # Mostrar el gráfico
# plt.show()



# Cargar los datos desde el CSV especificando que la primera fila es un encabezado
df = pd.read_csv('C:\\xampp\\htdocs\\phaser\\Mia.txt', header=None, names=['x1', 'x2', 'x3', 'target'], dtype=float)
# Crear la figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Graficar puntos con target=0
ax.scatter(df[df['target'] == 0]['x1'], df[df['target'] == 0]['x2'], df[df['target'] == 0]['target'], c='blue', marker='o', label='target=0')
# Graficar puntos con target=1
ax.scatter(df[df['target'] == 1]['x1'], df[df['target'] == 1]['x2'], df[df['target'] == 1]['target'], c='red', marker='x', label='target=1')
# Etiquetas de los ejes
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('Target')
# Mostrar leyenda
ax.legend()
# Mostrar el gráfico
plt.show()



# # Cargar los datos desde el CSV especificando que la primera fila es un encabezado
# df = pd.read_csv('C:\\xampp\\htdocs\\phaser\\Mia.txt', header=None, names=['x1', 'x2', 'target'], dtype=float)

# # Crear la figura
# plt.figure()

# # Graficar los puntos en 2D
# plt.scatter(df['x1'], df['x2'], c=df['target'], cmap='viridis', marker='o')

# # Etiquetas de los ejes
# plt.xlabel('x1')
# plt.ylabel('x2')

# # Mostrar el gráfico
# plt.show()





# # Cargar los datos desde el CSV especificando que la primera fila es un encabezado
# df = pd.read_csv('C:\\xampp\\htdocs\\phaser\\Mia.txt', header=None, names=['x1', 'x2', 'target'], dtype=float)

# # Crear la figura
# plt.figure()

# # Graficar los puntos en 2D con colores diferentes para target=0 y target=1
# plt.scatter(df[df['target'] == 0]['x1'], df[df['target'] == 0]['x2'], color='blue', label='target=0', marker='o')
# plt.scatter(df[df['target'] == 1]['x1'], df[df['target'] == 1]['x2'], color='red', label='target=1', marker='x')

# # Etiquetas de los ejes
# plt.xlabel('x1')
# plt.ylabel('x2')

# # Mostrar leyenda
# plt.legend()

# # Mostrar el gráfico
# plt.show()