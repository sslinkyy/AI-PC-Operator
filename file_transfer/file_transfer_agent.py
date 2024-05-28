import paramiko
from agents.base_agent import NeuralNetworkAgent

class FileTransferAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("upload_file"):
            _, local_path, remote_path = user_command.split(maxsplit=2)
            return self.upload_file(local_path, remote_path)
        elif user_command.startswith("download_file"):
            _, remote_path, local_path = user_command.split(maxsplit=2)
            return self.download_file(remote_path, local_path)
        return self.respond(f"Unknown command: {user_command}")

    def upload_file(self, local_path, remote_path):
        try:
            transport = paramiko.Transport(("hostname", 22))
            transport.connect(username="username", password="password")
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.put(local_path, remote_path)
            sftp.close()
            transport.close()
            return self.respond(f"Uploaded file from {local_path} to {remote_path}")
        except Exception as e:
            return self.respond(f"Failed to upload file. Error: {str(e)}")

    def download_file(self, remote_path, local_path):
        try:
            transport = paramiko.Transport(("hostname", 22))
            transport.connect(username="username", password="password")
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.get(remote_path, local_path)
            sftp.close()
            transport.close()
            return self.respond(f"Downloaded file from {remote_path} to {local_path}")
        except Exception as e:
            return self.respond(f"Failed to download file. Error: {str(e)}")
