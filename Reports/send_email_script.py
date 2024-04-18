import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# def send_email(username, password, recipient_email):
#     subject = "Selenium Test Execution Report"
#     body = "Please find the attached test execution report."
#
#     sender_email = username
#     receiver_email = recipient_email
#
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = receiver_email
#     msg['Subject'] = subject
#
#     msg.attach(MIMEText(body, 'plain'))
#
#     # Attach the test report file
#     with open('./Reports/homepage.html', 'rb') as f:
#         attach = MIMEApplication(f.read(), _subtype="html")
#         attach.add_header('Content-Disposition', 'attachment', filename=str("homepage.html"))
#         msg.attach(attach)
#
#     # Send the email
#     with smtplib.SMTP('smtp.gmail.com', 587) as server:
#         server.starttls()
#         server.login(username, password)
#         server.sendmail(sender_email, receiver_email, msg.as_string())
#
#
# if __name__ == "__main__":
#     gmail_username = sys.argv[1]
#     gmail_password = sys.argv[2]
#     recipient_email = sys.argv[3]
#
#     send_email(gmail_username, gmail_password, recipient_email)

def send_email(username, password, recipient_email):
    subject = "Selenium Test Execution Report"
    body = "Please find the attached test execution report."

    sender_email = username.decode('utf-8')  # Decode bytes to string
    receiver_email = recipient_email.decode('utf-8')  # Decode bytes to string

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Attach the test report file
    with open('./Reports/report.html', 'rb') as f:
        attach = MIMEApplication(f.read(), _subtype="html")
        attach.add_header('Content-Disposition', 'attachment', filename=str("report.html"))
        msg.attach(attach)

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(username.decode('utf-8'), password.decode('utf-8'))  # Decode bytes to string
        server.sendmail(sender_email, receiver_email, msg.as_string())

