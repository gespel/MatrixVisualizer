import os
import sys
import shutil
import numpy as np
import csv
import matplotlib.pyplot as plt
import glob
import contextlib
import logging
from PIL import Image

logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)

class MatrixVisualizer:
    def __init__(self):
        pass

    def visualize(self, fileName):
        file1 = open(fileName, 'r')
        Lines = file1.read()
        Matrices = Lines.split("\n\n")
        os.mkdir("tmp")
        logging.info('Parsing File...')
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

        logging.info('Rendering frame images...')
        for x in range(0, len(out), 20):
            plt.imshow(out[x], cmap='plasma', interpolation='nearest')
            plt.colorbar()

            plt.savefig(f'tmp/{x}.png', dpi=300)
            plt.close()
            logging.info(f"{x/len(out)*100}%")


        logging.info('Rendering GIF...')
        fp_in = "tmp/*.png"
        fp_out = f"{fileName.split('.')[0]}.gif"

        image_paths = sorted(glob.glob(fp_in), key=lambda x: int(x.split("/")[1].split('.')[0]))

        images = []

        for path in image_paths:
            images.append(Image.open(path))

        images[0].save(fp=fp_out, format='GIF', append_images=images[1:],
                    save_all=True, duration=20, loop=0)
        logging.info('Cleaning up...')
        shutil.rmtree("tmp")
filename = sys.argv[1]
mv = MatrixVisualizer()
mv.visualize(filename)