from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
       return render_template("login.html")
    elif request.method=="POST":
         return redirect(url_for("processing"))
    
@app.route("/processing",methods=["GET","POST"])
def processing():
    name=request.form["nm"]
    email=request.form["em"]
    passwd=request.form["ps"]
    file=open("info.txt","w")
    file.write(name)
    file.write(email)
    file.write(passwd)
    file.close()
    return redirect(url_for("msg"))

@app.route("/msg")
def msg():
    return render_template("msg.html")
    
if __name__=="__main__":
    app.run()