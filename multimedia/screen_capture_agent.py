import pyautogui
from agents.base_agent import NeuralNetworkAgent

class ScreenCaptureAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("capture_screen"):
            _, file_path = user_command.split(maxsplit=1)
            return self.capture_screen(file_path)
        return self.respond(f"Unknown command: {user_command}")

    def capture_screen(self, file_path):
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save(file_path)
            return self.respond(f"Captured screen and saved to: {file_path}")
        except Exception as e:
            return self.respond(f"Failed to capture screen. Error: {str(e)}")
