import smtplib
from email.mime.text import MIMEText
import environ
env = environ.Env()


def send_via_smtp(subject, to_email, email_content):
    """
    subject --> email subject
    to_email --> receivers email id
    email_content --> html content to be sent on mail
    """

    message = MIMEText(email_content, 'html')
    message['From'] = 'your@email.com'
    message['To'] = to_email
    message['Subject'] = subject

    try:
        smtp_server = smtplib.SMTP('smtp.mailgun.org', 587)
        smtp_server.starttls()
        smtp_server.login(
            env('MAILGUN_USER'),
            env('MAILGUN_PASS')
        )
        smtp_server.sendmail(
            message['From'],
            message['To'],
            message.as_string()
        )
        smtp_server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
