import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

from motion_equation import *

# Fonction pour créer la figure et les sous-plots
def create_figure(x, y, z):
    fig = plt.figure(figsize=(15, 8))

    #-------------------------------------------------
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')  
    ax2 = fig.add_subplot(2, 2, 2)  
    ax3 = fig.add_subplot(2, 2, 4)  

    # Limites des axes en fonction des données de la trajectoire
    x_max = np.max(x)
    y_max = np.max(y)
    z_max = np.max(z)

    max_floor_length = max(x_max, y_max)

    # 3D View ----------------------------------------
    line1, = ax1.plot([], [], [], 'b-')
    point1, = ax1.plot([], [], [], 'ro')
    ax1.set_xlim(-max_floor_length, max_floor_length)
    ax1.set_ylim(-max_floor_length, max_floor_length) 
    ax1.set_zlim(0, z_max)
    ax1.set_title("3D View")

    # Plan XZ ----------------------------------------
    line2, = ax2.plot([], [], 'b-')
    point2, = ax2.plot([], [], 'ro')
    ax2.set_xlim(-max_floor_length, max_floor_length)
    ax2.set_ylim(0, z_max)
    ax2.set_xlabel("x")
    ax2.set_ylabel("z")
    ax2.set_title("Plan XZ")
    ax2.grid() 

    # Plan YZ ----------------------------------------
    line3, = ax3.plot([], [], 'b-')
    point3, = ax3.plot([], [], 'ro')
    ax3.set_xlim(-max_floor_length, max_floor_length)
    ax3.set_ylim(0, z_max)
    ax3.set_xlabel("y")
    ax3.set_ylabel("z")
    ax3.set_title("Plan YZ")
    ax3.grid() 

    fig.tight_layout()

    return fig, ax1, ax2, ax3, line1, point1, line2, point2, line3, point3