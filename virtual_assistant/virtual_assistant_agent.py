from datetime import datetime
from agents.base_agent import NeuralNetworkAgent

class VirtualAssistantAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        self.tasks = []
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("add_task"):
            _, time_str, task = user_command.split(maxsplit=2)
            return self.add_task(time_str, task)
        elif user_command.startswith("view_tasks"):
            return self.view_tasks()
        return self.respond(f"Unknown command: {user_command}")

    def add_task(self, time_str, task):
        try:
            task_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            self.tasks.append((task_time, task))
            return self.respond(f"Task added for {time_str}: {task}")
        except Exception as e:
            return self.respond(f"Failed to add task. Error: {str(e)}")

    def view_tasks(self):
        try:
            task_list = "\n".join([f"{t[0]}: {t[1]}" for t in self.tasks])
            return self.respond(f"Tasks:\n{task_list}")
        except Exception as e:
            return self.respond(f"Failed to view tasks. Error: {str(e)}")
