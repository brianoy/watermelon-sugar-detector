from sound_to_ftt import get_list_from_ftt,get_fft_from_wav
from ftt_to_train import get_model_from_list
from train_to_predict import get_result_from_model

predict_filepath = "predict.txt"
get_fft_from_wav("for_train_sound")
ftt_list = get_list_from_ftt("fft_data")
print(ftt_list)

label_list = [1,3,5,7,9]#甜度 label
model_object = get_model_from_list(ftt_list,label_list)
print(model_object)

predict_features_list = eval(open(predict_filepath, 'r').read())
print(predict_features_list)
result_int = get_result_from_model(model_object, [predict_features_list])
print(result_int)#get result label

