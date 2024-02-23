import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Defina as credenciais e o endereço do servidor SMTP
smtp_server = "smtp.gmail.com"
port = 587
sender_email = ""
password = ""
recipient_emails = [""]  # Lista de e-mails
recipient_names = [""] # Nome dos remetentes

# Crie a mensagem
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(recipient_emails)  # Junta todos os e-mails em uma string separada por vírgulas
message["Subject"] = "Importante"

with open('index_body_mail.html', 'r', encoding='utf-8') as file:
    html = file.read()

message.attach(MIMEText(html, "html"))

try:
    # Crie a conexão com o servidor
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Ative o modo TLS

    # Faça login na conta de e-mail
    server.login(sender_email, password)

    # Envie o e-mail para todos os destinatários
    for email in recipient_emails:
        server.sendmail(sender_email, email, message.as_string())

except Exception as e:
    # Imprime qualquer erro que ocorrer
    print(f"Ocorreu um erro: {e}")

finally:
    # Feche a conexão com o servidor, se possível
    server.quit()
