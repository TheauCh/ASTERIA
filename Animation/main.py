import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

from motion_equation import *
from display import *


# Définir la valeur minimale et maximale de z que nous voulons atteindre
z_min_limit = 0
z_max_limit = 100

# Définir le temps max "t" que nous voulons avoir
t_max_array = 500

# On trouve la valeur maximale de t qui correspond à ces valeurs de z_min_limit et z_max_limit
t_values = np.linspace(0, t_max_array , 1000)  # On prend initialement une grande plage de t
_, _, z_values = trajectory(t_values)

# On trouve les indices où z devient <z_min_limit et > z_max_limit
index_limit_min = np.argmax(z_values < z_min_limit) 
index_limit_max = np.argmax(z_values > z_max_limit)

# Si z_limit n'est jamais atteint, utiliser la valeur maximale de t
if z_values[index_limit_max] > z_max_limit:
    t_max = t_values[index_limit_max]
elif z_values[index_limit_min] <= z_min_limit:
    t_max = t_values[index_limit_min]
else:
    t_max = t_values[-1]

# Maintenant, on définit t en fonction de cette valeur maximale
t = np.linspace(0, t_max, 200)

# Génération des données initiales
x, y, z = trajectory(t)

# Créer la figure et les sous-plots
fig, ax1, ax2, ax3, line1, point1, line2, point2, line3, point3 = create_figure(x, y, z)

# Fonction d'initialisation pour l'animation
def init():
    line1.set_data([], [])
    line1.set_3d_properties([])
    point1.set_data([], [])
    point1.set_3d_properties([])
    
    line2.set_data([], [])
    point2.set_data([], [])
    
    line3.set_data([], [])
    point3.set_data([], [])
    
    return line1, point1, line2, point2, line3, point3

# Fonction de mise à jour pour l'animation
def update(frame):
    # Mise à jour des lignes
    line1.set_data(x[:frame], y[:frame])
    line1.set_3d_properties(z[:frame])

    line2.set_data(x[:frame], z[:frame])

    line3.set_data(y[:frame], z[:frame])
    
    # Mise à jour des points rouges
    point1.set_data([x[frame]], [y[frame]])
    point1.set_3d_properties([z[frame]])
    
    point2.set_data([x[frame]], [z[frame]])
    
    point3.set_data([y[frame]], [z[frame]])
    
    return line1, point1, line2, point2, line3, point3

# Création de l'animation
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=False, repeat=False, interval=100)

plt.show()
