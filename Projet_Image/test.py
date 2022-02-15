from PIL import Image
import cv2
from numpy import *
from matplotlib.pyplot import *
from skimage.color import *
from math import exp, expm1


def blur(image):
    F = image.copy()
    N,M = image.shape
    h = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
    for i in range(2, N-2):
        for j in range(2, M-2):
            s = 0
            for n in range(-1, 1):
                for m in range(-1, 1):
                    s += h[n + 1][m + 1] * image[i + n][j + m]


            F[i][j] = s

    return F

def Moyenneur(image, taille):
    imagefiltrage = image.copy()
    x = int((taille - 1) / 2)
    for i in range(x, image.shape[0] - x):
        for j in range(x, image.shape[1] - x):
            s = 0
            for n in range(-x, x):
                for m in range(-x, x):
                    s += image[i + n, j + m] / (taille * taille)
            imagefiltrage[i, j] = s
            s = 0
    return imagefiltrage

image = cv2.imread('lena.jpg')
img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#img = rgb2gray(image)
image2 = Moyenneur(image, 5)
#image2 = cv2.blur(image,(3,3))
cv2.imshow("Fermeture",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()