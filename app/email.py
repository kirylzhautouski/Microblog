from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body,
               attachments=None, sync=False):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    if attachments:
        for attachment in attachments:
            msg.attach(*attachment)
    if sync:
            if mail.app is None:
                mail.init_app(current_app)
            print(current_app.config['MAIL_SERVER'])
            mail.send(msg)
    else:
        Thread(target=send_async_email,
            args=(current_app._get_current_object(), msg)).start()