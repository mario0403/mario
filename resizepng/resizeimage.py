import cv2
import numpy as np



img=cv2.imread('input.png');

T2=img.shape; #
imy2=T2[0] # higt
imx2=T2[1] # wide

path='parameter.txt';#
f=open(path,'r');#
ls=f.read();#
sn=ls.split('\n');#
newx=int(sn[0]);#
newy=int(sn[1]);#
f.close( ) ;#

tempb=np.zeros((max(imy2,newy),max(imx2,newx)));
tempg=np.zeros((max(imy2,newy),max(imx2,newx)));
tempr=np.zeros((max(imy2,newy),max(imx2,newx)));


B=img[:,:,0];
G=img[:,:,1];
R=img[:,:,2];

flB=np.float32(B);
flG=np.float32(G);
flR=np.float32(R);

db=cv2.dct(flB);
dg=cv2.dct(flG);
dr=cv2.dct(flR);

tempb[0:imy2,0:imx2]=db;
newdb=tempb[0:newy,0:newx];
tempg[0:imy2,0:imx2]=dg;
newdg=tempg[0:newy,0:newx];
tempr[0:imy2,0:imx2]=dr;
newdr=tempr[0:newy,0:newx];

imb=cv2.idct(newdb);
img=cv2.idct(newdg);
imr=cv2.idct(newdr);

r=(newx*newy)/(imx2*imy2);
r=r**0.5;

imb=imb*r;
img=img*r;
imr=imr*r;

XX=cv2.merge([imb,img,imr]);
cv2.imwrite('out3.png', XX); 