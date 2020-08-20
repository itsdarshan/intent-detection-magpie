import dialogflow
import os

project_id = 'tcc-chatbot-kyhwfw'
session_id = 'session_id'
ln = 'en'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'F:/Turabit/Task_423_405_NLP_Magpie/tcc-chatbot-cb71e7360a01.json'

def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)         # getting text input
        query_input = dialogflow.types.QueryInput(text=text_input)  # preparing query input for intent detection
        response = session_client.detect_intent(
            session=session, query_input=query_input)       # preparing response

        return response.query_result                        # accessing query