from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
        flash("¡Hola team SRE!")
        return render_template("index.html")

@app.route('/about')
def info():
    return '<h1>Esta web fue creada por rgermani</h1>'
