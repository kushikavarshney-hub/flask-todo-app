from flask import Blueprint,render_template,request,redirect,session,flash
auth=Blueprint("auth",__name__)
@auth.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if username=="admin" and password=="1234":
            session["user"]=username
            return redirect("/dashboard")
        else:
            flash("Invalid username or password")
        return redirect("/login")
    return render_template("login.html")
@auth.route("/dashboard")
def dashboard():
    if "user" in session:
        name=session["user"]
        return render_template("dashboard.html",name=name)
    return redirect("/login")
@auth.route("/logout")
def logout():
    session.pop("user",None)
    return redirect("/login")
