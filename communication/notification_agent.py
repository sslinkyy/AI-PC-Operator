import smtplib
from email.mime.text import MIMEText
from agents.base_agent import NeuralNetworkAgent

class NotificationAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("send_notification"):
            _, email, message = user_command.split(maxsplit=2)
            return self.send_notification(email, message)
        return self.respond(f"Unknown command: {user_command}")

    def send_notification(self, email, message):
        try:
            msg = MIMEText(message)
            msg['Subject'] = 'Notification'
            msg['From'] = 'your_email@example.com'
            msg['To'] = email

            with smtplib.SMTP('smtp.example.com') as server:
                server.login('your_email@example.com', 'your_password')
                server.sendmail('your_email@example.com', [email], msg.as_string())

            return self.respond(f"Notification sent to {email}.")
        except Exception as e:
            return self.respond(f"Failed to send notification to {email}. Error: {str(e)}")
