from transformers import pipeline
from agents.base_agent import NeuralNetworkAgent

class NaturalLanguageAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)
        self.nlp_pipeline = pipeline('sentiment-analysis')

    def execute_task(self, user_command):
        if user_command.startswith("process_text"):
            _, text = user_command.split(maxsplit=1)
            return self.process_text(text)
        return self.respond(f"Unknown command: {user_command}")

    def process_text(self, text):
        try:
            analysis = self.nlp_pipeline(text)
            return self.respond(f"Processed text: {text}. Analysis: {analysis}")
        except Exception as e:
            return self.respond(f"Failed to process text: {text}. Error: {str(e)}")
