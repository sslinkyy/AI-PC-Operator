import datetime
from agents.base_agent import NeuralNetworkAgent

class PersonalAssistantAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        self.reminders = []
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("set_reminder"):
            _, time_str, message = user_command.split(maxsplit=2)
            return self.set_reminder(time_str, message)
        elif user_command.startswith("view_reminders"):
            return self.view_reminders()
        return self.respond(f"Unknown command: {user_command}")

    def set_reminder(self, time_str, message):
        try:
            reminder_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            self.reminders.append((reminder_time, message))
            return self.respond(f"Reminder set for {time_str}: {message}")
        except Exception as e:
            return self.respond(f"Failed to set reminder. Error: {str(e)}")

    def view_reminders(self):
        try:
            reminder_list = "\n".join([f"{rem[0]}: {rem[1]}" for rem in self.reminders])
            return self.respond(f"Reminders:\n{reminder_list}")
        except Exception as e:
            return self.respond(f"Failed to view reminders. Error: {str(e)}")
