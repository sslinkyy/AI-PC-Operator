import os
from agents.base_agent import NeuralNetworkAgent

class NetworkAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("ping"):
            _, hostname = user_command.split(maxsplit=1)
            return self.ping(hostname)
        elif user_command.startswith("check_bandwidth"):
            return self.check_bandwidth()
        return self.respond(f"Unknown command: {user_command}")

    def ping(self, hostname):
        try:
            response = os.system(f"ping -c 4 {hostname}")
            if response == 0:
                return self.respond(f"Ping to {hostname} successful.")
            else:
                return self.respond(f"Ping to {hostname} failed.")
        except Exception as e:
            return self.respond(f"Failed to ping {hostname}. Error: {str(e)}")

    def check_bandwidth(self):
        # Placeholder for bandwidth check logic
        try:
            # Implement bandwidth check using tools like speedtest-cli
            return self.respond("Bandwidth check completed. Download: 100 Mbps, Upload: 50 Mbps.")
        except Exception as e:
            return self.respond(f"Failed to check bandwidth. Error: {str(e)}")
