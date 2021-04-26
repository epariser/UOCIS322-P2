"""
Evan PAriser's Flask API.
"""

from flask import Flask, render_template, abort, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo\n"

@app.rout(</path:fileName>)
def requesthandler(fileName):
    forbidden = ['//','..','~']

    if any(x in fileName for x in forbidden):
        abort(403)
    
    if not (fileName.endswith('.html') or fileName.endswith('.css')):
        abort(404)


    

@app.errorhandler(404)  #file not found error
def error_404():
    return render_template('templates', '404.html'), 404

@app.errorhandler(403)  #forbidden error
def error_403(e):
    return render_template('templates', '403.htm'), 403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
