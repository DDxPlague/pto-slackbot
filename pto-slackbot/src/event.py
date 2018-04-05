import command

class Event:
    def __init__(self, bot):
        self.bot = bot
        self.command = command.Command()

    def wait_for_event(self):
        events = self.bot.slack_client.rtm_read()

        if events and len(events) > 0:
            for event in events:
                print (event)
                self.parse_event(event)

    def is_event_in_thread(self, event):
        if event and 'thread_ts' in event:
            is_thread = True
        elif event and 'thread_ts' not in event:
            is_thread = False
        return is_thread

    def parse_event(self, event):
        self.is_event_in_thread(event)
        if event and 'text' in event and self.bot.bot_id in event['text']:
            self.handle_event(event['user'], event['text'].split(self.bot.bot_id)[1].strip().lower(), event['channel'])

    def handle_event(self, user, command, channel):
        if command and channel:
            print("Received command: " + command + " in channel: " + channel + " from user: " + user)
            response = self.command.handle_command(user, command)
            self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)


#TODO
#Need to parse every event
#Determine if it is an @mention
#Determine if it is a reply to a message the bot sent in a thread
#Determine if a user is @mentioned that is on my PTO list
