# 傅立葉轉換
from scipy.io.wavfile import read
from scipy.fftpack import fft
import matplotlib.pyplot as plt

# 讀取 WAV 檔案
rate, data = read("sound_test/input.wav")
print("Sample rate: {} Hz".format(rate))
print("Data type: {}".format(data.dtype))

dataFFT = fft(data[0:1024])
dataFFTAbs = abs(dataFFT[1:500])

# 繪製頻譜圖
plt.figure(figsize=(15, 5))
plt.plot(dataFFTAbs, 'r')
plt.show()

