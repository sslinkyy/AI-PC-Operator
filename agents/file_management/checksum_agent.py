import hashlib
from agents.base_agent import NeuralNetworkAgent

class ChecksumAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("calculate_checksum"):
            _, file_path = user_command.split(maxsplit=1)
            return self.calculate_checksum(file_path)
        elif user_command.startswith("verify_checksum"):
            _, file_path, expected_checksum = user_command.split(maxsplit=2)
            return self.verify_checksum(file_path, expected_checksum)
        return self.respond(f"Unknown command: {user_command}")

    def calculate_checksum(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256()
                while chunk := f.read(8192):
                    file_hash.update(chunk)
                checksum = file_hash.hexdigest()
            return self.respond(f"Calculated checksum for file: {file_path} is {checksum}")
        except Exception as e:
            return self.respond(f"Failed to calculate checksum for file: {file_path}. Error: {str(e)}")

    def verify_checksum(self, file_path, expected_checksum):
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256()
                while chunk := f.read(8192):
                    file_hash.update(chunk)
                actual_checksum = file_hash.hexdigest()
            if actual_checksum == expected_checksum:
                return self.respond(f"Checksum verification succeeded for file: {file_path}")
            else:
                return self.respond(f"Checksum verification failed for file: {file_path}")
        except Exception as e:
            return self.respond(f"Failed to verify checksum for file: {file_path}. Error: {str(e)}")
