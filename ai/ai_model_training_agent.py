import torch
import torch.nn as nn
import torch.optim as optim
from agents.base_agent import NeuralNetworkAgent

class AIModelTrainingAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)
        self.model = None
        self.optimizer = None
        self.criterion = None

    def execute_task(self, user_command):
        if user_command.startswith("train_model"):
            return self.train_model()
        elif user_command.startswith("save_model"):
            _, file_path = user_command.split(maxsplit=1)
            return self.save_model(file_path)
        elif user_command.startswith("load_model"):
            _, file_path = user_command.split(maxsplit=1)
            return self.load_model(file_path)
        return self.respond(f"Unknown command: {user_command}")

    def train_model(self):
        try:
            self.model = nn.Linear(10, 1)
            self.optimizer = optim.SGD(self.model.parameters(), lr=0.01)
            self.criterion = nn.MSELoss()

            # Placeholder training loop
            for epoch in range(10):
                inputs = torch.randn(10)
                targets = torch.randn(1)
                self.optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = self.criterion(outputs, targets)
                loss.backward()
                self.optimizer.step()

            return self.respond("Model training completed successfully.")
        except Exception as e:
            return self.respond(f"Failed to train model. Error: {str(e)}")

    def save_model(self, file_path):
        try:
            torch.save({
                'model_state_dict': self.model.state_dict(),
                'optimizer_state_dict': self.optimizer.state_dict(),
                'criterion': self.criterion
            }, file_path)
            return self.respond(f"Model saved to {file_path}")
        except Exception as e:
            return self.respond(f"Failed to save model. Error: {str(e)}")

    def load_model(self, file_path):
        try:
            checkpoint = torch.load(file_path)
            self.model = nn.Linear(10, 1)
            self.optimizer = optim.SGD(self.model.parameters(), lr=0.01)
            self.criterion = nn.MSELoss()

            self.model.load_state_dict(checkpoint['model_state_dict'])
            self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
            self.criterion = checkpoint['criterion']
            self.model.eval()  # Set the model to evaluation mode
            return self.respond(f"Model loaded from {file_path}")
        except Exception as e:
            return self.respond(f"Failed to load model. Error: {str(e)}")
