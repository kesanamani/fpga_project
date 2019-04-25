import numpy as np
import serial
import time
import matplotlib.pyplot as plt
import cv2

ser_in = serial.Serial('/dev/ttyACM1',9600)

#~ original image
m=96
n=96
y = []
image = np.asmatrix(np.zeros((m,n)))
image[0:96 , 0:96] = 0.7
image[17:80,17:80] = 0
image[27:70,27:70] = 1
image[32:65,32:65] = 0.2
image[41:56,41:56] = 1
w = [0,0,0,0,0,0,0,0,0,0,0]
w[0]=0
w[1] = -95003
w[2] = -117939
w[3] = 52036
w[4] = -55799
w[5] = -37860
w[6] = 224943
w[7] = 150578
w[8] = 247485
w[9] = 611424
#~ noise 
mean = 0
var = 0.005
sigma = var ** 0.5
gaussian = np.random.normal(mean, sigma, (96, 96)) 

#~ adding noise to image
noisy_image = np.zeros(image.shape, np.float32)
noisy_image = image + gaussian
cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
noisy_image = noisy_image.astype(np.uint8)

#~ adding extra zeros to image for convolution
rows,cols=noisy_image.shape
#~ print rows,cols
#~ print rows,cols
prefixedimage = noisy_image
prefixedimage= np.hstack((noisy_image,(np.zeros((96,2)))))
prefixedimage= np.vstack((prefixedimage,(np.zeros((2,98)))))

y=np.array([0,0,0,0,0,0,0,0,0])
for i1 in range(rows):
	for i2 in range(cols):
		u = prefixedimage[i1:i1+3, i2:i2+3]
		u=np.flip(u,0)
		u=np.flip(u,1)
		u=np.asarray(u)
		#~ print(type(u))
		#~ print(u.shape)
		u=np.reshape(u,9)
		y=np.vstack((y, u))
time.sleep(0.5)
#~ sending to serial
ser_in.write(str("-2")+ '\n')
for i2 in range(len(y)):
	ser_in.write(str("-2")+ '\n')
	time.sleep(0.01)
	ser_in.write(str("-1")+'\n')
	time.sleep(0.01)
	for i in range(9):
			ser_in.write(str(y[i2,i]))
			#~ ser_in.write(" ")
			time.sleep(0.01)
	time.sleep(0.01)	
ser_in.write(str("-2\n"))	
ser_in.close



