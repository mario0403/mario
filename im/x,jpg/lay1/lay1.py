import cv2                    # 匯入 OpenCV 函式庫
  #      
ph='L1.jpg'
img = cv2.imread(ph)  # 讀取圖片
T=img.shape #
imy=T[0]#
imx=T[1]#
#cv2.imshow('oxxostudio',img)        # 賦予開啟的視窗名稱，開啟圖片
path='L1.txt'#f=open(path,'r')#
ls=f.read()#
sn=ls.split('\n')#
px=int(sn[0])#
py=int(sn[1])#
buf=int(sn[2])#
f.close( ) #)

crop_img = img[0:py+buf, 0:px+buf]        # 取出陣列的範圍
cv2.imwrite('1L11.jpg', crop_img) # 儲存圖片
crop_img = img[py-buf:imy, 0:px+buf]        # 取出陣列的範圍
cv2.imwrite('1L21.jpg', crop_img) # 儲存圖片
crop_img = img[0:py+buf, px-buf:imx]        # 取出陣列的範圍
cv2.imwrite('1L12.jpg', crop_img) # 儲存圖片
crop_img = img[py-buf:imy, px-buf:imx]        # 取出陣列的範圍
cv2.imwrite('1L22.jpg', crop_img) # 儲存圖片
