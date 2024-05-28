import tkinter as tk
from agents.base_agent import NeuralNetworkAgent

class UIAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        self.window = tk.Tk()
        self.window.title("AI System UI")
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("create_button"):
            _, text, command = user_command.split(maxsplit=2)
            return self.create_button(text, command)
        return self.respond(f"Unknown command: {user_command}")

    def create_button(self, text, command):
        try:
            button = tk.Button(self.window, text=text, command=lambda: self.supervisor.delegate_task(command))
            button.pack()
            return self.respond(f"Created button with text: {text}")
        except Exception as e:
            return self.respond(f"Failed to create button. Error: {str(e)}")

    def run_ui(self):
        self.window.mainloop()
