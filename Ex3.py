# 1
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
# import winsound

def saw(t, p):
    T = t - np.floor (t / p) * p
    return (T - p/2) / p * 2

Fs = 44100  # sampling frequency
f = 261.63   # The frequency of Do is 261.63 Hz
f1 = 262.63   

T = 10       # Duration time

t = np.linspace(0., T, T*Fs+1)
# t1 = np.linspace(0., T, T*Fs+1)

Amplitude = (np.iinfo(np.int16).max)/10
y  = Amplitude * np.sin(2. * np.pi * f * t)
y1  = Amplitude * np.sin(2. * np.pi * f1 * t)
yf=y+y1
#y = Amplitude * saw (t, 1/f)

wav.write ('example.wav', Fs, yf.astype(np.int16))

filename = 'example.wav'  
# winsound.PlaySound (filename, winsound.SND_FILENAME)

Fs2, y2 = wav.read (filename)
t2 = np.arange ( len (y2) ) / Fs2
plt.plot ( t2, y2 )
# plt.plot()



# 2

# img = plt.imread (r'C:\Users\user\Desktop\a.jpg')
img = plt.imread (r'D:\東卯山.jpg')
nimg=np.zeros(img.shape,dtype='uint8')
a=img[:,:,0]*0.299+img[:,:,1]*0.587+img[:,:,2]*0.114
nimg[:,:,0]=a#img[:,:,0]*0.299
nimg[:,:,1]=a#img[:,:,1]*0.587
nimg[:,:,2]=a#img[:,:,2]*0.114
# nimg.shape
# nimg[:,:,2]
# a.shape
# img.shape

plt.imshow(nimg)
