import pyperclip
from agents.base_agent import NeuralNetworkAgent

class ClipboardAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("copy_to_clipboard"):
            _, text = user_command.split(maxsplit=1)
            return self.copy_to_clipboard(text)
        elif user_command.startswith("paste_from_clipboard"):
            return self.paste_from_clipboard()
        return self.respond(f"Unknown command: {user_command}")

    def copy_to_clipboard(self, text):
        try:
            pyperclip.copy(text)
            return self.respond(f"Copied to clipboard: {text}")
        except Exception as e:
            return self.respond(f"Failed to copy to clipboard. Error: {str(e)}")

    def paste_from_clipboard(self):
        try:
            text = pyperclip.paste()
            return self.respond(f"Pasted from clipboard: {text}")
        except Exception as e:
            return self.respond(f"Failed to paste from clipboard. Error: {str(e)}")
