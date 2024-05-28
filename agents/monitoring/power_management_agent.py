import psutil
import os
from agents.base_agent import NeuralNetworkAgent

class PowerManagementAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("check_battery"):
            return self.check_battery()
        elif user_command.startswith("shutdown_system"):
            return self.shutdown_system()
        return self.respond(f"Unknown command: {user_command}")

    def check_battery(self):
        try:
            battery = psutil.sensors_battery()
            if battery:
                return self.respond(f"Battery status: {battery.percent}% remaining, plugged in: {battery.power_plugged}")
            else:
                return self.respond(f"No battery information available.")
        except Exception as e:
            return self.respond(f"Failed to check battery status. Error: {str(e)}")

    def shutdown_system(self):
        try:
            os.system('shutdown -h now')
            return self.respond(f"System is shutting down.")
        except Exception as e:
            return self.respond(f"Failed to shutdown system. Error: {str(e)}")
