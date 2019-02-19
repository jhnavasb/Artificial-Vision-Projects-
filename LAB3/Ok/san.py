# !/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#from imageio import imread

import cv2

t = True
coord = []
# templates
templa = cv2.imread('masima.png', 0)
small = cv2.imread('mas.png', 0)
small1 = cv2.imread('ma3.png', 0)

#
# Examen1  = cv2.imread('Examen.png',0)
img_rgb = cv2.imread('pai.jpg')
# img_rgb = cv2.imread('lab3_2.jpg')
# img_rgb = cv2.imread('Examen.png')
# img_rgb=cv2.erode(img_rgb, None, iterations=2)

rows, cols = templa.shape
rows1, cols1 = small1.shape

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

HistorialPuntos = np.zeros((4, 2), dtype=int)  # Crea una matriz, donde las filas son los puntos
PHP = 0  # Puntero Historial Puntos
for i in range(-1, 90):
    M1 = cv2.getRotationMatrix2D((cols / 2, rows / 2), -i, 1.2)  # coly row/2
    M2 = cv2.getRotationMatrix2D((cols / 2, rows / 2), -i, 1)  # coly row/2
    M3 = cv2.getRotationMatrix2D((cols1 / 2, rows1 / 2), -i, 1.1)  # coly row/2

    template = cv2.warpAffine(templa, M1, (cols, rows))
    template2 = cv2.warpAffine(small, M2, (cols, rows))
    template3 = cv2.warpAffine(small1, M3, (cols1, rows1))

    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    res2 = cv2.matchTemplate(img_gray, template2, cv2.TM_CCOEFF_NORMED)
    res3 = cv2.matchTemplate(img_gray, template3, cv2.TM_CCOEFF_NORMED)

    offset = 150
    threshold = 0.65
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        l = (pt[0] + w, pt[1] + h)
        cv2.rectangle(img_gray, pt, l, (0, 0, 255), 1)

        if t:
            x = pt[0]

        if np.abs(x - pt[0]) > 40 or t:
            k = [pt, (pt[0] + w, pt[1]), (pt[0], pt[1] + h), (pt[0] + w, pt[1] + h)]
            k = np.asarray(k)
            length = k.shape[0]
            sum_x = np.sum(k[:, 0])
            sum_y = np.sum(k[:, 1])
            coord.append([sum_x / length, sum_y / length])
            x = pt[0]
            t = False
        else:
            t = False
            # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    # cv2.imwrite('res.png',img_rgb)
    threshold = 0.725
    loc = np.where(res2 >= threshold)
    for pt in zip(*loc[::-1]):
        l = (pt[0] + w, pt[1] + h)
        cv2.rectangle(img_gray, pt, l, (0, 0, 255), 1)

        if t:
            x = pt[0]

        if np.abs(x - pt[0]) > 40 or t:
            k = [pt, (pt[0] + w, pt[1]), (pt[0], pt[1] + h), (pt[0] + w, pt[1] + h)]
            k = np.asarray(k)
            length = k.shape[0]
            sum_x = np.sum(k[:, 0])
            sum_y = np.sum(k[:, 1])
            coord.append([sum_x / length, sum_y / length])
            x = pt[0]
            t = False
        else:
            t = False
    threshold = 0.8
    loc = np.where(res3 >= threshold)
    for pt in zip(*loc[::-1]):
        l = (pt[0] + w, pt[1] + h)
        cv2.rectangle(img_gray, pt, l, (0, 0, 255), 1)

        if t:
            x = pt[0]

        if np.abs(x - pt[0]) > 40 or t:
            k = [pt, (pt[0] + w, pt[1]), (pt[0], pt[1] + h), (pt[0] + w, pt[1] + h)]
            k = np.asarray(k)
            length = k.shape[0]
            sum_x = np.sum(k[:, 0])
            sum_y = np.sum(k[:, 1])
            coord.append([sum_x / length, sum_y / length])
            x = pt[0]
            t = False
        else:
            t = False
            '''P = HistorialPuntos[PHP]
            Pu = P+10
            Pd = P-10
            if np.any(P==0) and PHP==0:
                HistorialPuntos[PHP] = pt
            else:
                if Pd[0]<=pt[0] and pt[0]<=Pu[0]:
                    if Pd[1]<=pt[1] and pt[1]<=Pu[1]:
                        HistorialPuntos[PHP] = pt
                    else:
                        if not (np.any( (HistorialPuntos-offset)<= pt) and np.any( pt<=(HistorialPuntos+offset)   )):
                            print('Entro punto critico segtat   5')
                            PHP += 1
                            HistorialPuntos[PHP] = pt
                else:
                    if not (np.any( (HistorialPuntos-offset)<= pt) and np.any( pt<=(HistorialPuntos+offset)   )):
                        print('Entro punto critico segtat    6')
                        PHP += 1
                        HistorialPuntos[PHP] = pt'''
            # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

print(coord)

# plt.imshow(cv2.cvtColor(img_rgb,cv2.COLOR_BGR2RGB))
# plt.show()
# cv2.imwrite('res.png',img_rgb)

pt = tuple(coord[0])
cv2.rectangle(img_rgb, pt, (pt[0] + 100, pt[1] + 100), (0, 255, 0), 2)

pt = tuple(coord[1])
cv2.rectangle(img_rgb, pt, (pt[0] + 100, pt[1] + 100), (0, 255, 0), 2)

pt = tuple(coord[2])
cv2.rectangle(img_rgb, pt, (pt[0] + 100, pt[1] + 100), (0, 255, 0), 2)

pt = tuple(coord[3])
cv2.rectangle(img_rgb, pt, (pt[0] + 100, pt[1] + 100), (0, 255, 0), 2)

plt.imshow(cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))
plt.show()

"""
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('masima.png',0)
template2 = cv2.imread('masima2.png',0)
template3 = cv2.imread('masmia3.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
res1 = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
res2 = cv2.matchTemplate(img_gray,template3,cv2.TM_CCOEFF_NORMED)


threshold = 0.63
loc3= np.where( res2 >= threshold)

loc = np.where( res >= threshold)

loc2 = np.where( res1 >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

for pt in zip(*loc2[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

for pt in zip(*loc3[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('res.png',img_rgb)

cv2.imwrite('res1.png',img_rgb)

cv2.imwrite('res2.png',img_rgb)
"""

'''

pts1 = np.float32([[45,80],[817,80],[60,500],[817,500]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]]) 
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(Examen1,M,(300,300))
plt.subplot(121)
imgBuilding2 = Examen1.copy()
cv2.circle(imgBuilding2,(pts1[0][0],pts1[0][1]), 5, 255, -1) 
cv2.circle(imgBuilding2,(pts1[1][0],pts1[1][1]), 5, 255, -1) 
cv2.circle(imgBuilding2,(pts1[2][0],pts1[2][1]), 5, 255, -1) 
cv2.circle(imgBuilding2,(pts1[3][0],pts1[3][1]), 5, 255, -1) 

dilata=cv2.erode(dst, None, iterations=1)

'''
'''

plt.imshow(imgBuilding2, cmap = 'gray') 
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122) 
plt.imshow(dilata, cmap = 'gray') 
plt.title('Projective'), plt.xticks([]), plt.yticks([]) 
plt.show()
'''