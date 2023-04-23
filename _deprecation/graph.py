import numpy as np
from numpy import fft
from scipy.io import wavfile
#import matplotlib.pyplot as plt
#from pylab import show
import datetime
import pytz

def WavFtt(file_name)->None:
    fs_rate, signal = wavfile.read(file_name)
    #print(fs_rate) #48000Hz

    signal = signal.mean(axis=1) #2*n陣列 雙聲道轉單聲道
    sp = fft.fft(signal)

    dtime = datetime.datetime.now()
    timezone = pytz.timezone("Asia/Taipei")
    dtzone = timezone.localize(dtime)
    tstamp = round(dtzone.timestamp())


    with open("train_data/"+str(tstamp)+".txt", "w") as a:
        a.write(str(list(sp.real[:1000])))


#WavFtt("小玉拍擊.wav")
#WavFtt("小玉密集指骨.wav")
WavFtt("sound_test\input.wav")