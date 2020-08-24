from flask import render_template, jsonify
from flask_mail import Message
from settings import mail, app


def send_mail(recipients=None,token=None):
    link = app.config['FRONT_END_URL'] + '?token=' + str(token)
    print ( 'link\n', link )
    msg = Message("Welcome to InScholaris",recipients=[recipients])
    msg.html = render_template('verification_mail.html',sending_mail=True,verify_link=link)
    mail.send(msg)
