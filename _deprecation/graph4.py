import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile


# Load the WAV file
sample_rate, audio_data = wavfile.read('sound_test/input.wav')

# Compute the FFT
fft_data = np.abs(np.fft.fft(audio_data))

# Compute the frequency range
freq_range = np.fft.fftfreq(audio_data.size, d=1/sample_rate)

# Plot the FFT data
fft_data = np.resize(fft_data, freq_range.shape)
plt.plot(freq_range, fft_data)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()