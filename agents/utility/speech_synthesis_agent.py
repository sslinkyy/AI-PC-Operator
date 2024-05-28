import pyttsx3
from agents.base_agent import NeuralNetworkAgent

class SpeechSynthesisAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        self.engine = pyttsx3.init()
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("speak"):
            _, text = user_command.split(maxsplit=1)
            return self.speak(text)
        return self.respond(f"Unknown command: {user_command}")

    def speak(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
            return self.respond(f"Spoke text: {text}")
        except Exception as e:
            return self.respond(f"Failed to speak text: {text}. Error: {str(e)}")
 