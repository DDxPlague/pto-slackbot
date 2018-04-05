class Command(object):
    def __init__(self):
        self.commands = {
            "help" : self.help,
            "schedule pto" : self.schedule_pto
        }

    def handle_command(self, user, command):
        #response = "<@" + user + ">: "
        response = ""

        if command in self.commands:
            response += self.commands[command]()
        else:
            response += "Sorry I don't understand the command: " + command + ". " + self.help()

        return response

    def help(self):
        response = "Currently I support the following commands:\r\n"
        response += "```"

        for command in self.commands:
            response += command + "\r\n"

        response += "```"
        return response

    def schedule_pto(self):
        return "Working on building this functionality."
