# System deps
import os
import time

# Packages
from slackclient import SlackClient
from spacy import load as spacy_load
from pyowm import OWM

# Local
from exceptions import MessageProcessingException
from slack_helper import parse_bot_commands
from message_processor import MessageProcessor
from weather_formatter import WeatherFormatter

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
message_processor = MessageProcessor(spacy_load('en_core_web_lg'))
owm = OWM(os.environ.get('OWM_API_KEY'))

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM

"""
    Executes bot command if the command is known
"""
def handle_command(command, channel):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text="Let me check that for you..."
    )

    try:
        query = message_processor.process(command)
        weather_formatter = WeatherFormatter(
            query[1],
            owm.weather_at_place(query[1]).get_weather()
        )

        if (query[0] == 'temperature'):
            response = weather_formatter.format_for_temperature()
        else:
            response = weather_formatter.format_for_weather()
    except MessageProcessingException as e:
        response = str(e)

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        weatherman_id = slack_client.api_call("auth.test")["user_id"]

        while True:
            command, channel = parse_bot_commands(
                slack_client.rtm_read(),
                weatherman_id
            )

            if command:
                handle_command(command, channel)

            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
