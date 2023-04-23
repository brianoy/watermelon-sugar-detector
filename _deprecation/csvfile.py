import csv

# 開啟 CSV 檔案
def access_data()->list:
    with open('data.csv', newline='') as csvfile:
        return list(csv.reader(csvfile, delimiter='	'))