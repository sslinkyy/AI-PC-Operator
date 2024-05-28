class NeuralNetworkAgent:
    def __init__(self, name, level, supervisor):
        self.name = name
        self.level = level
        self.supervisor = supervisor

    def respond(self, message):
        return f"{self.name}: {message}"

    def execute_task(self, user_command):
        raise NotImplementedError("Each agent must implement the execute_task method.")
