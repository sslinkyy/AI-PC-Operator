import subprocess
from agents.base_agent import NeuralNetworkAgent

class ApplicationAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("open_application"):
            _, app_name = user_command.split(maxsplit=1)
            return self.open_application(app_name)
        return self.respond(f"Unknown command: {user_command}")

    def open_application(self, app_name):
        try:
            subprocess.Popen([app_name])
            return self.respond(f"Opened application: {app_name}")
        except Exception as e:
            return self.respond(f"Failed to open application: {app_name}. Error: {str(e)}")
