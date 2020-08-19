from flask import render_template, jsonify
from flask_mail import Message

from settings import mail


def send_mail(recipients=None):
    msg = Message("Welcome to InScholaris",recipients=[recipients])
    msg.html = render_template('verification_mail.html',sending_mail=True)
    mail.send(msg)
    # return jsonify({"message": "Mail sent successfully"})
