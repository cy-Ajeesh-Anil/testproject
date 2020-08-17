from flask import Flask
from settings import app,mail
from apis import api
from models import *
from flask_mail import Mail, Message
from flask import Flask,request,jsonify,render_template

# app = Flask(__name__)
api.init_app(app)

@app.route('/send_mail',methods=['GET','POST'])
def send_mail():
    msg = Message("Welcome to InScholaris", recipients=['arunyajayan96@gmail.com'])
    msg.html = render_template('verification_mail.html',sending_mail=True)
    mail.send(msg)
    return jsonify({"message": "Mail sent successfully"})
    # msg = Message("Welcome to InScholaris", recipients=['arunyajayan96@gmail.com'])
    # msg.body = "You have received a welcome mail from InScholaris"
    # mail.send(msg)
    # return jsonify({"message":"Mail sent successfully"})


if __name__ == '__main__':
    app.run(debug=False)
