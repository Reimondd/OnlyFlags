from flask import Flask, render_template, request, redirect, url_for
import os
from auth import login as check_login
import base64

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")


def _x(s, k):
    return "".join(chr(ord(c) ^ ord(k[i % len(k)])) for i, c in enumerate(s))
def _r(s):
    return "".join([chr(((ord(c)-65+13)%26)+65) if 65<=ord(c)<=90 else chr(((ord(c)-97+13)%26)+97) if 97<=ord(c)<=122 else c for c in s])
def _b(d, n=3):
    try:
        curr = d.strip()
        for i in range(n):
            curr = base64.b64decode(curr).decode('utf-8')
        return curr
    except Exception as e:
        return None

def brr(e):
    x = os.getenv(e, "")
    y = os.getenv("FLAG", "default")
    one = _b(x, 3)
    if not one: return "ERR"
    two = _r(one)
    f = _x(two, y)
    return f

@app.route("/studiomaster", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        credentials = f"{username}:{password}"

        if check_login(credentials):
            succes = brr("X")
            return render_template("studiomaster.html", F = succes),200
        else:
            return render_template("acces_denied.html"),401

    return render_template("login.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/blog/shrek")
def blog_shrek():
    return render_template("blog_shrek.html")


@app.route("/blog/po")
def blog_po():
    return render_template("blog_po.html")


@app.route("/blog/alex")
def blog_alex():
    return render_template("blog_alex.html")


@app.route("/blog/bee")
def blog_hiccup():
    return render_template("blog_hiccup.html")


@app.route("/blog/farquaad")
def blog_hidden():
    return render_template("blog_hidden.html")


@app.route("/logout")
def logout():
    return redirect(url_for("home"))

@app.route("/robots.txt")
def robot():
    return render_template("robots.html")

@app.route("/johnpork")
def john():
    return redirect("https://www.youtube.com/shorts/EcsU-9OpNMY")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)