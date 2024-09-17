import smtplib, ssl
import imghdr
from email.message import EmailMessage
import os

password = os.getenv("PASSWORD")
sender = "abc@gmail.com"
receiver = sender

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "A person appeared"
    email_message.set_content("Image of the person is attached with this email")

    with open(image_path,"rb") as file:
        content = file.read()
    email_message.add_attachment(content,maintype ="image",subtype=imghdr.what(None,content))

    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender,password)
    gmail.sendmail(sender,receiver,email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email("images/19.png")


