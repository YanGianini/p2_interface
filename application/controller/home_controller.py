from flask import Flask, render_template, redirect
from application import app
@app.route("/")
def index():
    return render_template("index.html")