import psutil
from agents.base_agent import NeuralNetworkAgent

class PerformanceMonitoringAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("monitor_performance"):
            return self.monitor_performance()
        return self.respond(f"Unknown command: {user_command}")

    def monitor_performance(self):
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            return self.respond(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_info.percent}%")
        except Exception as e:
            return self.respond(f"Failed to monitor performance. Error: {str(e)}")
