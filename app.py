from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/flask")
def flask():
    return render_template("flask.html")

@app.route("/python")
def python():
    return render_template("python.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/html")
def html():
    return render_template("html.html")

@app.route("/c++")
def c():
    return render_template("c++.html")

@app.route("/sql")
def sql():
    return render_template("sql.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)