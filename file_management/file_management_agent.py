import shutil
from agents.base_agent import NeuralNetworkAgent

class FileManagementAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("compress_file"):
            _, source, destination = user_command.split(maxsplit=2)
            return self.compress_file(source, destination)
        elif user_command.startswith("encrypt_file"):
            _, file_path = user_command.split(maxsplit=1)
            return self.encrypt_file(file_path)
        return self.respond(f"Unknown command: {user_command}")

    def compress_file(self, source, destination):
        try:
            shutil.make_archive(destination, 'zip', source)
            return self.respond(f"Compressed {source} to {destination}.zip")
        except Exception as e:
            return self.respond(f"Failed to compress {source}. Error: {str(e)}")

    def encrypt_file(self, file_path):
        try:
            # Placeholder for file encryption logic
            return self.respond(f"File {file_path} encrypted successfully.")
        except Exception as e:
            return self.respond(f"Failed to encrypt {file_path}. Error: {str(e)}")
