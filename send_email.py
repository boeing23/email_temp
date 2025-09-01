#!/usr/bin/env python3
"""
Super simple SMTP HTML Email Sender
- Reads email-final.html
- Sends it as the HTML body
- No MIME building complexity, just raw RFC 2822 string
"""

import smtplib
import ssl
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT   = 587
SENDER_EMAIL = "yashodhanhakke@gmail.com"
SENDER_NAME  = "Cinemind"
SUBJECT = "Cinemind - AI Powered Analysis Tool"

# set your app password in the environment:
# export GMAIL_APP_PASSWORD="xxxx xxxx xxxx xxxx"
APP_PASSWORD = "tpfqedpxfuafjvua"
TEMPLATE_PATH = "email-final.html"


def send_html(recipient: str, subject: str = SUBJECT):
    # load html file
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # construct raw RFC 2822 message
    message = f"""From: {SENDER_NAME} <{SENDER_EMAIL}>
To: {recipient}
Subject: {subject}
MIME-Version: 1.0
Content-Type: text/html; charset=utf-8

{html}
"""

    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient, message.encode("utf-8"))

    print(f"✅ Sent to {recipient}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python send_email.py recipient@example.com")
        sys.exit(2)
    recipient = sys.argv[1]
    send_html(recipient)
