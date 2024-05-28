import subprocess
from agents.base_agent import NeuralNetworkAgent

class AutomationAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("run_script"):
            _, script_path = user_command.split(maxsplit=1)
            return self.run_script(script_path)
        return self.respond(f"Unknown command: {user_command}")

    def run_script(self, script_path):
        try:
            result = subprocess.run([script_path], capture_output=True, text=True)
            return self.respond(f"Script {script_path} run result: {result.stdout}")
        except Exception as e:
            return self.respond(f"Failed to run script {script_path}. Error: {str(e)}")
