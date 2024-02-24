from flask import Flask, render_template, url_for, session, request, redirect

app = Flask(__name__)
app.secret_key = "garcode"

@app.route("/")
def home():
    return "HomePage"

@app.route("/profile", methods = ["POST", "GET"])
def profile():
    if request.method == "POST":
        user = request.form["fname"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("profile.html")

@app.route("/user")
def user():
    if 'user' in session:
        usr = session["user"]
        return f"<h1>{usr}</h1>"
    else:
        return redirect("profile")

if __name__ == "__main__":
    app.run(debug=true)