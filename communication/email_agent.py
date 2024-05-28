import smtplib
from email.mime.text import MIMEText
from agents.base_agent import NeuralNetworkAgent

class EmailAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("send_email"):
            _, recipient, subject, body = user_command.split(maxsplit=3)
            return self.send_email(recipient, subject, body)
        return self.respond(f"Unknown command: {user_command}")

    def send_email(self, recipient, subject, body):
        try:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = 'your_email@example.com'
            msg['To'] = recipient

            with smtplib.SMTP('smtp.example.com') as server:
                server.login('your_email@example.com', 'your_password')
                server.sendmail('your_email@example.com', [recipient], msg.as_string())

            return self.respond(f"Email sent to {recipient}.")
        except Exception as e:
            return self.respond(f"Failed to send email to {recipient}. Error: {str(e)}")
