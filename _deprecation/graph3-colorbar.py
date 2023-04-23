import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from pylab import show
# 讀取 WAV 檔案
rate, data = read("sound_test/input.wav")
# 產生時間資料
time = np.arange(0, len(data)) / rate

plt.figure(figsize=(15, 5))

# 繪製波形圖
plotA = plt.subplot(211)
plotA.plot(time, data)
plotA.set_ylabel("Amplitude")
plotA.set_xlim(0, len(data) / rate)

# 繪製時頻譜圖
plotB = plt.subplot(212)
data = data.mean(axis=1) #2*n陣列 雙聲道轉單聲道
plotB.specgram(data, NFFT=1024, Fs=rate, noverlap=900)
plotB.set_ylabel("Frequency")
plotB.set_xlabel("Time")

show()