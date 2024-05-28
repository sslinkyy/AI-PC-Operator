import pandas as pd
from agents.base_agent import NeuralNetworkAgent

class DataProcessingAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("process_data"):
            _, file_path = user_command.split(maxsplit=1)
            return self.process_data(file_path)
        return self.respond(f"Unknown command: {user_command}")

    def process_data(self, file_path):
        try:
            df = pd.read_csv(file_path)
            processed_data = df.describe().to_dict()
            return self.respond(f"Processed data: {processed_data}")
        except Exception as e:
            return self.respond(f"Failed to process data from {file_path}. Error: {str(e)}")
