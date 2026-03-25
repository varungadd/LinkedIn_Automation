import smtplib
from email.message import EmailMessage
import config

def send_email(jobs, subject):
    EMAIL = config.EMAIL.strip()
    APP_PASSWORD = config.APP_PASSWORD.strip()

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    content = f"{subject}\n\n"

    for job in jobs[:30]:
        content += f"{job['title']} at {job['company']}\n{job['link']}\n\n"

    msg.set_content(content)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
        print(f"{subject} → Email sent ✅")
    except Exception as e:
        print(f"{subject} → Email failed ❌", e)