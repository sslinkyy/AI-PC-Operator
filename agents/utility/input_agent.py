from agents.base_agent import NeuralNetworkAgent

class InputAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=1, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        # Parse and delegate the user command to the correct agent
        return self.supervisor.delegate_task(user_command)
