import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

class EmailService:
    _instance = None

    def __init__(self):
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.smtp_username = 'novasoftwareorganization@gmail.com'
        self.smtp_password = 'vymrasjjxjbnfczm'

        if not all([self.smtp_server, self.smtp_port, self.smtp_username, self.smtp_password]):
            raise ValueError("Por favor, defina todas as variáveis de ambiente necessárias para configurar o serviço de e-mail.")

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def send_email(self, recipient_email, subject, content):
        message = MIMEMultipart()
        message['From'] = self.smtp_username
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(content, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.sendmail(self.smtp_username, recipient_email, message.as_string())
                print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Falha ao enviar e-mail: {e}")
