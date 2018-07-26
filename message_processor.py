import spacy
from datetime import datetime

from exceptions import MessageProcessingException

class MessageProcessor:
    def __init__(self, nlp):
        self.nlp = nlp

    def process(self, message):
        doc = self.nlp(message)

        subject = self.get_subject(message)
        location, time = self.get_constraints(doc.ents)

        return subject, location, time

    def get_subject(self, message):
        if "weather" in message:
            return "weather"
        elif "temperature" in message:
            return "temperature"

        raise MessageProcessingException(
            "I don't understand. You can ask me for the weather or temperature in your city."
        )

    def get_constraints(self, entities):
        location = None
        time = datetime.now

        for entity in entities:
            if entity.label_ == "GPE":
                location = entity.text

            if entity.label_ == "DATE" or entity.label_ == "TIME":
                raise MessageProcessingException(
                    "I'm sorry, I do not understand dates or time yet."
                )

        # Unfortunately, we do not have access to a user's IP address. We will
        # require that they specify a location in their Slack message.
        if location is None:
            raise MessageProcessingException(
                "I'm sorry, but Slack cannot give me access to your location.\
You will need to specify a location. Try: `what is the weather in <city>`"
            )

        return location, time
