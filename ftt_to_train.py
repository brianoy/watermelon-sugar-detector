from sklearn import tree


def get_model_from_list(feature_list,train_labels)->object:
    """
    @param feature_list: features
    @type feature_list: 2*array float list [[data1],[data2],[data3].....]
    @param feature_list: labels
    @type feature_list: 1*array float list [data1,data2,data3.....]

    @returns: tree.DecisionTreeClassifier()
    @rtype: object
    """
    
    features = feature_list
    labels = train_labels
    clf = tree.DecisionTreeClassifier()# 實例化
    clf = clf.fit(features,labels)
    return clf