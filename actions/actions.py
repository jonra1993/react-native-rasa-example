# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json

# returns JSON object as a dictionary
MOCK_SCHEMA = json.load(open("actions/schemas/checkbox.json", "r"))


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_count_of_insults = tracker.get_slot("products")
        print("products: {}".format(current_count_of_insults))

        return []


class ActionAskFeelings(Action):

    def name(self) -> Text:
        return "action_ask_feelings"

    async def run(self,
                  dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        app_dict = {
            'products': ['messenger', 'messenger2']
        }
        app_list = ['messenger', 'messenger2']
        app_json = json.dumps(app_dict)
        # dispatcher.utter_message(
        #     text='How do you feel',
        #     buttons=[
        #         {
        #             "title": "great",
        #             "type": "postback",
        #             #"payload": "/tell_hello_world{}".format(app_json),
        #             "payload": "/tell_hello_world{}".format(app_json),
        #         },
        #         {
        #             "title": "super sad",
        #             "type": "postback",
        #             "payload": "/mood_sad",
        #         }
        #     ]
        # )
        dispatcher.utter_message(text= 'What do you choose?',attachment=MOCK_SCHEMA)
        return []
