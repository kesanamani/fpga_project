import numpy as np
import matplotlib.pyplot as plt
import cv2
def update(img,noise_img):
	rows,cols=img.shape
	filtersize=3
	step=5*1e-7
	errorImage = np.zeros((rows, cols))
	outputImage = np.zeros((rows, cols))
	mean = 0
	var = 0.5
	sigma = var ** 0.5
	filt=np.random.normal(mean, sigma, (3,3)) 
	prefixedimage = noise_img
	prefixedimage= np.hstack((noise_img,(np.zeros((96,2)))))
	prefixedimage= np.vstack((prefixedimage,(np.zeros((2,98)))))
	for i in range(0,500):
		print (filt)
		for i1 in range(0,rows-1):
			for i2 in range(0,cols-1):
				u = prefixedimage[i1:i1+3, i2:i2+3]
				u=np.flip(u,0)
				u=np.flip(u,1)
				ex1 = np.multiply(filt,u)
				outputImage[i1,i2] = np.sum(ex1)
				errorImage[i1,i2] = img[i1,i2] - outputImage[i1,i2]
				print (filt)
				filt = filt + (2*step*errorImage[i1,i2]*u)
	for i1 in range(0,rows):
   		for i2 in range(0,cols):
   			u = prefixedimage[i1:i1+3, i2:i2+3]
   			u=np.flip(u,0)
   			u=np.flip(u,1)
   			ex1 = np.multiply(filt,u)
   			outputImage[i1,i2] = np.sum(ex1)
   			errorImage[i1,i2] = img[i1,i2] - outputImage[i1,i2]
   			filt = filt + (2*step*errorImage[i1,i2]*u)
	return outputImage
# [[-0.05333825 -0.06383114  0.14045789]
#  [-0.05494474 -0.02433676  0.21326375]
#  [ 0.14493338  0.209317    0.52354688]]


# generating image
m=96
n=96
image = np.asmatrix(np.zeros((m,n)))
print (image.shape)

image[0:96 , 0:96] = 0.7
image[17:80,17:80] = 0
image[27:70,27:70] = 1
image[32:65,32:65] = 0.2
image[41:56,41:56] = 1

mean = 0
var = 0.005
sigma = var ** 0.5
gaussian = np.random.normal(mean, sigma, (96, 96)) 
noisy_image = np.zeros(image.shape, np.float32)
# plt.imshow(gaussian,"gray")
# plt.show()
noisy_image = image + gaussian
cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
noisy_image = noisy_image.astype(np.uint8)
# print noisy_image
# plt.imshow(noisy_image,"gray")
cv2.normalize(image, image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
image= image.astype(np.uint8)
# out=update(image,noisy_image)
plt.imshow(noisy_image,"gray")
plt.show()
# print out
plt.imshow(out,"gray")
plt.show()
