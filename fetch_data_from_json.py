import json
import os
import os.path
from df_intent_detection import detect_intent_texts
from google.protobuf.json_format import MessageToDict


DIR_json = 'F:\Turabit\Task_423_405_NLP_Magpie\intent_data\intents'
DIR_data = 'F:\Turabit\Task_423_405_NLP_Magpie\intent_data\intent_data'
project_id = 'tcc-chatbot-kyhwfw'
session_id = 'session_id'
ln = 'en'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'F:/Turabit/Task_423_405_NLP_Magpie/tcc-chatbot-cb71e7360a01.json'

def count_json(DIR):
    return len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])


def fetch_data(json_dir, data_dir):
    os.chdir(json_dir)
    y_true = []
    # y_pred = []
    random_list = [i for i in range(0, 10000)]
    for file in os.listdir():
        if '_usersays_en' in file:
            f_open = open(file, )
            phrase_list = json.load(f_open)
            intent_name = file.replace('_usersays_en.json', '')
            os.chdir(data_dir)
            for phrases in range(0, len(phrase_list)):
                x_create = open(str(random_list[phrases])+".txt", "w+")
                x_create.write(phrase_list[phrases]['data'][0]['text'])

                # x_create = open(intent_name+ ".txt", "w+")
                # x_create.write(phrase_list[0]['data'][0]['text'])

                x_create.close()

                y_create = open(str(random_list[phrases])+".lab", "w+")
                # y_create = open(intent_name + ".lab", "w+")

                y_create.write(intent_name)
                y_create.close()
            # df_intent = detect_intent_texts(project_id, session_id, phrase_list[0]['data'][0]['text'], 'en')
            # dict_data = MessageToDict(message=df_intent)
            # y_pred.append(dict_data['intent']['displayName'])
            random_list = random_list[len(phrase_list):]

            y_true.append(intent_name)
            f_open.close()
            os.chdir(json_dir)

    return y_true
