from flask import Flask,render_template,request
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yashbharadwajsuper@gmail.com'
app.config['MAIL_PASSWORD'] = 'yash@1998'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

user=["yashbharadwajsuper@gmail.com","2016pceceyash120@poornima.org","2016pcecevikram116@poornima.org"]
@app.route("/",methods=["GET"])
def y():
    return render_template ("index.html")

@app.route("/sent",methods=["GET","POST"])
def index1() :
    if (request.method=="POST"):
        name=request.form.get("name")
        email=request.form.get("email")
        

            msg = Message('Hello', sender = 'yourId@gmail.com', recipients = [u])
            msg.body = note
            mail.send(msg)

    return "Sent"
