import serial
import numpy as np
import time
# ser_in = serial.Serial('/dev/ttyACM1',9600)
ser_out = serial.Serial('/dev/ttyACM0',9600)
# a = np.array([1,2,3,4,5,6,7,8,9])
#print a
f = open("img.txt",'w')
img=np.empty(shape=(0,0))
while(1):
	x = ser_out.readline()
	f.write(str(x))
	#~ print (x)
f.close()
# ser_in.close
ser_out.close
