import numpy as np
import matplotlib.pyplot as plt
text_file = open("img.txt", "r")
lines = text_file.readlines()
a=np.asarray(lines)
b=np.reshape(a,(96,768))
img=np.zeros((96,96),dtype=int)
k=1
for i in range(96):
	for j in range(96):
		k=((j*8)-3)
		img[i,j]=(int(b[i,k],2))

img = np.asmatrix(img)
img.astype(int)
print(img)
plt.imshow(img,"gray")
plt.show()
text_file.close()
