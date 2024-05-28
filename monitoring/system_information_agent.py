import platform
import socket
import re
import uuid
import psutil
from agents.base_agent import NeuralNetworkAgent

class SystemInformationAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("get_system_info"):
            return self.get_system_info()
        return self.respond(f"Unknown command: {user_command}")

    def get_system_info(self):
        try:
            info = {
                'platform': platform.system(),
                'platform-release': platform.release(),
                'platform-version': platform.version(),
                'architecture': platform.machine(),
                'hostname': platform.node(),
                'ip-address': socket.gethostbyname(socket.gethostname()),
                'mac-address': ':'.join(re.findall('..', '%012x' % uuid.getnode())),
                'processor': platform.processor(),
                'ram': str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
            }
            return self.respond(f"System information: {info}")
        except Exception as e:
            return self.respond(f"Failed to retrieve system information. Error: {str(e)}")
