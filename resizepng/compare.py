import cv2
import numpy as np



image=cv2.imread('input.png');

T2=image.shape; #
imy2=T2[0] # higt
imx2=T2[1] # wide

path='parameter.txt';#
f=open(path,'r');#
ls=f.read();#
sn=ls.split('\n');#
newx=int(sn[0]);#
newy=int(sn[1]);#
f.close( ) ;#




img1 = cv2.resize(image, (newx, newy), interpolation=cv2.INTER_NEAREST);
img2 = cv2.resize(image, (newx, newy), interpolation=cv2.INTER_LINEAR);
img3 = cv2.resize(image, (newx, newy), interpolation=cv2.INTER_AREA);
img4 = cv2.resize(image, (newx, newy), interpolation=cv2.INTER_CUBIC);
img5 = cv2.resize(image, (newx, newy), interpolation=cv2.INTER_LANCZOS4);

cv2.imwrite('INTER_NEAREST.png',img1);
cv2.imwrite('INTER_LINEAR.png',img2);
cv2.imwrite('INTER_AREA.png',img3);
cv2.imwrite('INTER_CUBIC.png',img4);
cv2.imwrite('INTER_LANCZOS4.png',img5);
