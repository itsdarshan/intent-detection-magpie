import pandas
import re
from magpie import Magpie
# from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import confusion_matrix, classification_report
from dataset_creation import y_true # , y_pred

mp = Magpie(keras_model='F:/Turabit/Task_423_405_NLP_Magpie/model/model.h5',
            word2vec_model='F:/Turabit/Task_423_405_NLP_Magpie/w2v_model/w2v',
            scaler='F:/Turabit/Task_423_405_NLP_Magpie/scaler/sc',
            labels=y_true)



print((mp.predict_from_text('about our company'))[:3])
# y_t = y_true
# y_p = y_pred
# for i in range(519628, 1129693):
#     try:
#         X = mp.predict_from_file('data/hep-categories/'+str(i)+'.txt')
#
#         with open('data/hep-categories/'+str(i)+'.lab', encoding="utf8") as data:
#             data_text = data.readline()
#         if X:
#             y_p.append(X[0][0])
#         if data_text:
#             data_txt = re.sub('\n', '', data_text)
#             y_t.append(data_txt)
#     except ValueError as e:
#         pass
#
#
df_p = pandas.DataFrame(y_p).values
df_t = pandas.DataFrame(y_t).values

cm = confusion_matrix(df_t, df_p)
print(classification_report(df_t, df_p))



