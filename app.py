from flask import Flask,redirect
from auth import auth
app=Flask(__name__)
app.secret_key="secret123"
app.register_blueprint(auth)
@app.route("/")
def home():
    return redirect("/login")
if __name__=="__main__":
    app.run(debug=True)
    