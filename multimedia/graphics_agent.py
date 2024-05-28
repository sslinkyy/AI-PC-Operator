import matplotlib.pyplot as plt
import numpy as np
from agents.base_agent import NeuralNetworkAgent

class GraphicsAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("render_3d"):
            _, object_name = user_command.split(maxsplit=1)
            return self.render_3d_object(object_name)
        elif user_command.startswith("plot_graph"):
            _, equation = user_command.split(maxsplit=1)
            return self.plot_graph(equation)
        return self.respond(f"Unknown command: {user_command}")

    def render_3d_object(self, object_name):
        try:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            x, y = np.random.rand(2, 100) * 4
            z = np.sin(x) + np.cos(y)
            ax.scatter(x, y, z)
            plt.title(f"3D Object: {object_name}")
            plt.show()
            return self.respond(f"Rendered 3D object: {object_name}")
        except Exception as e:
            return self.respond(f"Failed to render 3D object: {object_name}. Error: {str(e)}")

    def plot_graph(self, equation):
        try:
            x = np.linspace(-10, 10, 400)
            y = eval(equation)
            plt.plot(x, y, label=equation)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title(f"Graph of {equation}")
            plt.legend()
            plt.show()
            return self.respond(f"Plotted graph for equation: {equation}")
        except Exception as e:
            return self.respond(f"Failed to plot graph for equation: {equation}. Error: {str(e)}")
