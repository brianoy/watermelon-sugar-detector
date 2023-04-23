import os
import glob
from numpy import fft
from scipy.io import wavfile


def get_fft_from_wav(folder_path)->None:
    file_pattern = os.path.join(folder_path, '*.wav')# 合併路徑\txt
    file_list = glob.glob(file_pattern)# 搜尋符合條件的檔案
    print(file_list)
    for file_path in file_list:
        print(file_path)
        fs_rate, signal = wavfile.read(file_path)
        print(fs_rate) #48000Hz

        signal = signal.mean(axis=1) #2*n陣列 雙聲道轉單聲道
        sp = fft.fft(signal) # fft

        open("fft_data/"+str(file_path).replace("for_train_sound\\","").replace(".wav","")+".txt", "w",encoding="utf-8").write(str(list(sp.real[:1000])))



def get_list_from_ftt(folder_path)->list:
    """
    @param folder_path: folder_path
    @type folder_path: str

    @returns: list of ftt 2*array data [[data1],[data2],[data3].....]
    @rtype: list
    """

    file_pattern = os.path.join(folder_path, '*.txt')# 合併路徑\txt
    file_list = glob.glob(file_pattern)# 搜尋符合條件的檔案
    print(file_pattern)
    content_list = []# 將檔案內容存入list中 #2D list[[n,n,n,n,.....],[],[],[],....]
    for file_path in file_list:
        with open(file_path, 'r') as file:
            content = eval(file.read())
            content_list.append(content)
            
    return content_list

get_list_from_ftt("fft_data")