
from ..skills.summary import Summary

from ..slack.resource import MsgResource
from ..slack.slackbot import SlackerAdapter


class DoNotDisturbManager(object):

    def __init__(self):
        self.slackbot = SlackerAdapter()

    def call_is_holiday(self, dnd):
        dnd_enabled = dnd['dnd_enabled']

        # TODO: {'dnd_enabled': True, 'next_dnd_start_ts': 1500711803, 'next_dnd_end_ts': 1500715403}
        # -> dirrenct action with diff_min
        Summary().record_holiday(dnd_enabled)
        if dnd:
            self.slackbot.send_message(text=MsgResource.HOLIDAY)
        else:
            self.slackbot.send_message(text=MsgResource.WEEKDAY)
