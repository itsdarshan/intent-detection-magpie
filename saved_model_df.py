from magpie import Magpie
from dataset_creation import y_true  # , y_pred
magpie = Magpie()

magpie.train_word2vec('F:/Turabit/Task_423_405_NLP_Magpie/intent_data/intent_data', vec_dim=250)

magpie.init_word_vectors('F:/Turabit/Task_423_405_NLP_Magpie/intent_data/intent_data', vec_dim=250)

labels = y_true

magpie.train('F:/Turabit/Task_423_405_NLP_Magpie/intent_data/intent_data', labels, test_ratio=0.2, epochs=10)

#print((magpie.predict_from_text('Hii'))[:4])
magpie.save_word2vec_model('F:/Turabit/Task_423_405_NLP_Magpie/w2v_model/df_w2v')
magpie.save_scaler('F:/Turabit/Task_423_405_NLP_Magpie/scaler/df_sc', overwrite=True)
magpie.save_model('F:/Turabit/Task_423_405_NLP_Magpie/model/df_model.h5')
# magpie.save_word2vec_model('F:/Turabit/Task_423_405_NLP_Magpie/w2v_model/df_w2v')
# magpie.save_scaler('F:/Turabit/Task_423_405_NLP_Magpie/scaler/df_sc', overwrite=True)
# magpie.save_model('F:/Turabit/Task_423_405_NLP_Magpie/model/df_model.h5')