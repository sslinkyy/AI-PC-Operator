import whisper
from agents.base_agent import NeuralNetworkAgent

class AudioAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=1, supervisor=supervisor)
        self.model = whisper.load_model("base")
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("process_audio"):
            _, audio_path = user_command.split(maxsplit=1)
            return self.process_audio(audio_path)
        return self.respond(f"Unknown command: {user_command}")

    def process_audio(self, audio_path):
        try:
            result = self.model.transcribe(audio_path)
            return self.respond(f"Processed audio. Transcription: {result['text']}")
        except Exception as e:
            return self.respond(f"Failed to process audio: {audio_path}. Error: {str(e)}")
