import sympy as sp
from agents.base_agent import NeuralNetworkAgent

class MathAgent(NeuralNetworkAgent):
    def __init__(name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("calculate"):
            _, expression = user_command.split(maxsplit=1)
            return self.calculate(expression)
        return self.respond(f"Unknown command: {user_command}")

    def calculate(self, expression):
        try:
            result = sp.sympify(expression)
            return self.respond(f"Calculated result for expression: {expression} is {result}")
        except Exception as e:
            return self.respond(f"Failed to calculate expression: {expression}. Error: {str(e)}")
