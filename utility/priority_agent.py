import queue
from agents.base_agent import NeuralNetworkAgent

class PriorityAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=1, supervisor=supervisor)
        self.task_queue = queue.PriorityQueue()
        supervisor.add_subordinate(self)

    def add_task(self, priority, task):
        self.task_queue.put((priority, task))

    def execute_task(self, user_command):
        if user_command.startswith("add_task"):
            _, priority, task = user_command.split(maxsplit=2)
            self.add_task(int(priority), task)
            return self.respond(f"Added task with priority {priority}: {task}")
        elif user_command == "process_tasks":
            return self.process_tasks()
        return self.respond(f"Unknown command: {user_command}")

    def process_tasks(self):
        results = []
        while not self.task_queue.empty():
            priority, task = self.task_queue.get()
            result = self.supervisor.delegate_task(task)
            results.append((priority, task, result))
        return self.respond(f"Processed tasks: {results}")
