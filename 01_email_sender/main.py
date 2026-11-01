from email.message import EmailMessage
from pathlib import Path

from dotenv import load_dotenv
import os
import ssl
import smtplib

env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")

def generate_email(template, name, additional_details):
    if template == "thank_you":
        subject = "Thank You for Your Support"
        body = (f"Hi {name},\n"
                f"I wanted to thank you for your help.\n"
                f"{additional_details}\n"
                f"I really appreciate your time and support.\n"
                f"Best regards,")
    elif template == "birthday_wishes":
        subject = "Happy Birthday!"
        body = (f"Hi {name},\n"
                f"Happy Birthday! I hope your special day is filled with happiness, laughter, and wonderful moments.\n"
                f"{additional_details}\n"
                f"Wishing you all the best!\n"
                f"Best wishes,")
    elif template == "job_application":
        subject = "Job Application"
        body = (f"Dear Hiring Manager,\n"
                f"I am writing to express my interest in the position.\n"
                f"{additional_details}\n"
                f"Thank you for considering my application. I look forward to hearing from you.\n"
                f"Kind regards,")
    else:
        raise ValueError("Unknown template")
    return subject, body

def send_email(email_receiver, subject, body):
    try:
        context = ssl.create_default_context()
        em = EmailMessage()
        em["From"] = EMAIL_ADDRESS
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.sendmail(EMAIL_ADDRESS,email_receiver, em.as_string())
        return True
    except smtplib.SMTPException as e:
        print(f"Email sending failed: {e}")
        return False

while True:
    print("Choose email template:")
    print(f"1. Thank You\n2. Birthday Wishes\n3. Job Application\n")
    option = input("Your choice: ")
    if option == "1":
        selected_template = "thank_you"
        break
    elif option == "2":
        selected_template = "birthday_wishes"
        break
    elif option == "3":
        selected_template = "job_application"
        break
    else:
        print("Invalid option. Please try again.")
        continue

name = input("Please enter recipient's name: ")
email_receiver = input("Please enter recipient's email address: ")
additional_details = input("Please provide additional details: ")

subject, body = generate_email(selected_template, name, additional_details)



print(f"Your email preview:\n"
      f"Subject: {subject}\n"
      f"\n"
      f"{body}")

while True:

    decided = input("Do you want to send this email? Y/N ").lower()
    if decided == "y":
        is_sent = send_email(email_receiver, subject, body)
        if is_sent:
            print("Email sent successfully!")
        else:
            print("Email was not sent.")
        break
    elif decided == "n":
        print("Email sending cancelled.")
        break
    else:
        print("Invalid option. Please try again.")


