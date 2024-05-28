import os
from agents.base_agent import NeuralNetworkAgent

class OperatingSystemAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("navigate_directory"):
            _, directory = user_command.split(maxsplit=1)
            return self.navigate_directory(directory)
        elif user_command.startswith("list_directory"):
            return self.list_directory()
        elif user_command.startswith("create_file"):
            _, file_name = user_command.split(maxsplit=1)
            return self.create_file(file_name)
        return self.respond(f"Unknown command: {user_command}")

    def navigate_directory(self, directory):
        try:
            os.chdir(directory)
            return self.respond(f"Navigated to directory: {directory}")
        except Exception as e:
            return self.respond(f"Failed to navigate to directory: {directory}. Error: {str(e)}")

    def list_directory(self):
        try:
            files = os.listdir()
            return self.respond(f"Current directory files: {files}")
        except Exception as e:
            return self.respond(f"Failed to list directory files. Error: {str(e)}")

    def create_file(self, file_name):
        try:
            with open(file_name, 'w') as f:
                f.write('')
            return self.respond(f"Created file: {file_name}")
        except Exception as e:
            return self.respond(f"Failed to create file: {file_name}. Error: {str(e)}")
