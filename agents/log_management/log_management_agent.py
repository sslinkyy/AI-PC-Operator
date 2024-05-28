import logging
from agents.base_agent import NeuralNetworkAgent

class LogManagementAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        logging.basicConfig(filename='system.log', level=logging.INFO)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("log_info"):
            _, message = user_command.split(maxsplit=1)
            return self.log_info(message)
        elif user_command.startswith("log_error"):
            _, message = user_command.split(maxsplit=1)
            return self.log_error(message)
        return self.respond(f"Unknown command: {user_command}")

    def log_info(self, message):
        try:
            logging.info(message)
            return self.respond(f"Logged info: {message}")
        except Exception as e:
            return self.respond(f"Failed to log info. Error: {str(e)}")

    def log_error(self, message):
        try:
            logging.error(message)
            return self.respond(f"Logged error: {message}")
        except Exception as e:
            return self.respond(f"Failed to log error. Error: {str(e)}")
