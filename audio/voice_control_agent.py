import speech_recognition as sr
from agents.base_agent import NeuralNetworkAgent

class VoiceControlAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        self.recognizer = sr.Recognizer()
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("voice_command"):
            return self.voice_command()
        return self.respond(f"Unknown command: {user_command}")

    def voice_command(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return self.supervisor.delegate_task(command)
        except Exception as e:
            return self.respond(f"Failed to process voice command. Error: {str(e)}")
