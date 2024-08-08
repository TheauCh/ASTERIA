import numpy as np

# Fonction pour générer les données de la trajectoire 
def trajectory(t):
    x = t                       
    y = np.zeros_like(t)        
    z = t                       
    return x, y, z