import cv2
import matplotlib.pyplot as plt

resim = cv2.imread('watch.jpg')
#pixel = resim[200,200]
#resim[200,200] = [0,0,0]
#print pixel

print resim.shape
print resim.size
print resim.dtype
