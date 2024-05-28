import shutil
from agents.base_agent import NeuralNetworkAgent

class BackupRestoreAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("backup"):
            _, source, destination = user_command.split(maxsplit=2)
            return self.backup(source, destination)
        elif user_command.startswith("restore"):
            _, source, destination = user_command.split(maxsplit=2)
            return self.restore(source, destination)
        return self.respond(f"Unknown command: {user_command}")

    def backup(self, source, destination):
        try:
            shutil.copytree(source, destination)
            return self.respond(f"Backup from {source} to {destination} completed successfully.")
        except Exception as e:
            return self.respond(f"Failed to backup from {source} to {destination}. Error: {str(e)}")

    def restore(self, source, destination):
        try:
            shutil.copytree(source, destination)
            return self.respond(f"Restore from {source} to {destination} completed successfully.")
        except Exception as e:
            return self.respond(f"Failed to restore from {source} to {destination}. Error: {str(e)}")
