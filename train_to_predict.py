def get_result_from_model(tree_object,feature_list)->int:
    """
    @param tree_object: tree.DecisionTreeClassifier()
    @type tree_object: object
    @param feature_list: list of feature 2*array float list [[data1],[data2],[data3].....]
    @type feature_list: list   

    @returns: predict result
    @rtype: int
    """
    wantPredict = tree_object.predict(feature_list) 
    return wantPredict

