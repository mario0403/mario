import cv2   #
import numpy as np

path='L1.txt'#
f=open(path,'r')#
ls=f.read()#
sn=ls.split('\n')#
px=int(sn[0])#
py=int(sn[1])#
buf=int(sn[2])#
f.close( ) #)

img11 = cv2.imread('L11.png')  # 讀取圖片
img12 = cv2.imread('L12.png')  # 讀取圖片
img21 = cv2.imread('L21.png')  # 讀取圖片
img22 = cv2.imread('L22.png')  # 讀取圖片
##
T1=img11.shape #
T2=img22.shape #
imy2=T2[0] # higt
imx2=T2[1] # wide
##
M11=img11[0:py,0:px] #
M21=img21[buf:imy2,0:px] #
M12=img12[0:py,buf:imx2] #
M22=img22[buf:imy2,buf:imx2] #

c1=np.hstack((M11,M12));
c2=np.hstack((M21,M22));
M=np.vstack((c1,c2));

cv2.imwrite('Merge.png',M ); # 儲存圖片