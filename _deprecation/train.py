from sklearn import tree
from deprecation.csvfile import access_data
import numpy as np

raw_data = access_data()
processed_features = []
processed_labels = []

for i in range(1,len(raw_data)):
    processed_features.append(int(raw_data[i][2]))
    processed_labels.append(int(raw_data[i][1]))
features = np.array(processed_features).reshape(1, -1)
labels = np.array(processed_labels).reshape(1, -1)
print(features)
print(labels)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

predict_value = np.array(int(50)).reshape(1, -1)#[頻率]
wantPredict = clf.predict(predict_value) 

print(wantPredict)