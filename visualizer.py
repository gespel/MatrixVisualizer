import numpy as np
import csv
import matplotlib.pyplot as plt
import glob
import contextlib
from PIL import Image


file1 = open('BTCS_48_48_5000-1.csv', 'r')
Lines = file1.read()
Matrices = Lines.split("\n\n")


out = []
for matrix in Matrices:
    m = []
    matrixLines = matrix.split("\n")
    
    for matrixLine in matrixLines:
        tmp = []
        splitline = matrixLine.strip().split(" ")
        
        for n in splitline:
            if n:
                tmp.append(float(n))
        if len(tmp) > 1:
            m.append(tmp)
    out.append(m)


for x in range(0, len(out), 20):
    plt.imshow(out[x], cmap='copper', interpolation='nearest')
    plt.colorbar()

    plt.savefig(f'{x}.png', dpi=300)
    plt.close()



fp_in = "*.png"
fp_out = "matrix.gif"

# Liste der Dateipfade zu den Bildern sortieren
image_paths = sorted(glob.glob(fp_in), key=lambda x: int(x.split('.')[0]))

# Liste zum Speichern der geladenen Bilder
images = []

# Bilder laden
for path in image_paths:
    images.append(Image.open(path))

# GIF erstellen
images[0].save(fp=fp_out, format='GIF', append_images=images[1:],
               save_all=True, duration=20, loop=0)