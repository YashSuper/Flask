from flask import Flask,render_template,request,session
app = Flask(__name__)
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
app.secret_key='yashb'

#simple sturcture Flask app
@app.route("/")
def index():
    return render_template("index.html")
    # passing data
@app.route("/ren")
def jai():
    names=["yash","vikram","vikal"]
    return render_template("index.html",head12=names)
#using another url {{url_for}}
@app.route("/more")
def more():
     return f"hello"
     # passing data through website to app
@app.route("/hello",methods=["POST","GET"])
def hello():
    if (request.method=="GET") :
        return "plzz submit th e form instead"
    else:
        name=request.form.get("name")

    return render_template("layout.html", name=name)
#sessions
@app.route("/sess",methods=["POST","GET"])
def sess():
    if session.get["notes"] is None:
        session["notes"]=[]
    if request.method=="POST":
        note=request.form.get("note")
        session["notes"].append(note)
        return render_template ("index.html",notes=note)

    else:
        return render_template ("index.html")
