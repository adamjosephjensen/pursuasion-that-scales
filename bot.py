import os
import time
from slackclient import SlackClient

import nlp as nl
import response

# starterbot's ID as an environment variable
BOT_ID = 'U22EJ4NAD'

# constants
AT_BOT = "<@" + BOT_ID + ">"

# instantiate Slack & Twilio clients
slack_client = SlackClient('xoxb-70494158353-8x9n5Q9Uh2eLNtQYM9MPJyb0')


def handle_text(command, channel):
    intent = nl.p(command)
    say = response.for_intent(intent)
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=say, as_user=True)


def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                parsed = output['text'].split(AT_BOT)[1].strip().lower()
                return parsed, output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            text, channel = parse_slack_output(slack_client.rtm_read())
            if text and channel:
                handle_text(text, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
