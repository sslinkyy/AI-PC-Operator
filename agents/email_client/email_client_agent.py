import imaplib
import smtplib
from email.mime.text import MIMEText
from agents.base_agent import NeuralNetworkAgent

class EmailClientAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("send_email"):
            _, recipient, subject, body = user_command.split(maxsplit=3)
            return self.send_email(recipient, subject, body)
        elif user_command.startswith("fetch_emails"):
            return self.fetch_emails()
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

    def fetch_emails(self):
        try:
            mail = imaplib.IMAP4_SSL('imap.example.com')
            mail.login('your_email@example.com', 'your_password')
            mail.select('inbox')
            result, data = mail.search(None, 'ALL')
            email_ids = data[0].split()
            emails = []
            for e_id in email_ids:
                result, data = mail.fetch(e_id, '(RFC822)')
                emails.append(data[0][1].decode('utf-8'))
            return self.respond(f"Fetched emails: {emails}")
        except Exception as e:
            return self.respond(f"Failed to fetch emails. Error: {str(e)}")
