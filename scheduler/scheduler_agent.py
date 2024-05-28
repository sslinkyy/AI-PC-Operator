import schedule
import time
import threading
from agents.base_agent import NeuralNetworkAgent

class SchedulerAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)
        self.scheduler = schedule.Scheduler()
        self.thread = threading.Thread(target=self.run_pending, daemon=True)
        self.thread.start()

    def execute_task(self, user_command):
        if user_command.startswith("schedule_task"):
            _, time_str, task = user_command.split(maxsplit=2)
            return self.schedule_task(time_str, task)
        return self.respond(f"Unknown command: {user_command}")

    def schedule_task(self, time_str, task):
        try:
            self.scheduler.every().day.at(time_str).do(lambda: self.supervisor.delegate_task(task))
            return self.respond(f"Scheduled task '{task}' at {time_str}")
        except Exception as e:
            return self.respond(f"Failed to schedule task '{task}' at {time_str}. Error: {str(e)}")

    def run_pending(self):
        while True:
            self.scheduler.run_pending()
            time.sleep(1)
