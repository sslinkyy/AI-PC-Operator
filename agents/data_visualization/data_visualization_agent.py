import matplotlib.pyplot as plt
from agents.base_agent import NeuralNetworkAgent

class DataVisualizationAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("plot_data"):
            _, data = user_command.split(maxsplit=1)
            return self.plot_data(eval(data))
        return self.respond(f"Unknown command: {user_command}")

    def plot_data(self, data):
        try:
            plt.plot(data)
            plt.title('Data Visualization')
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.show()
            return self.respond("Plotted data successfully")
        except Exception as e:
            return self.respond(f"Failed to plot data. Error: {str(e)}")
