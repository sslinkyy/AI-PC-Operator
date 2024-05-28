import subprocess
from agents.base_agent import NeuralNetworkAgent

class UpdateAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("update_system"):
            return self.update_system()
        return self.respond(f"Unknown command: {user_command}")

    def update_system(self):
        try:
            # Example for Linux systems using apt
            result = subprocess.run(["sudo", "apt", "update", "&&", "sudo", "apt", "upgrade", "-y"], capture_output=True, text=True)
            return self.respond(f"System update results: {result.stdout}")
        except Exception as e:
            return self.respond(f"Failed to update system. Error: {str(e)}")
