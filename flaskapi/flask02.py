#!/usr/bin/env python3
import re
import json

from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename

## start a flask app
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "Welcome to API automation"

@app.route("/upload")
def upload_file():
    return render_template("upload.html")

@app.route("/uploader", methods = ["GET", "POST"])
def uploader():
    if request.method == "POST":
        flippy = request.files["file"]
        flippy.save(secure_filename(flippy.filename))
        return redirect(url_for("success"))
        #return "File successfully uploaded!"

@app.route("/success")
def success():
    siplist = []
    sipdict = {}
    with open("fakesip.log") as siplog:
        for line in siplog:
            sipobj = re.search(r"sip:\+(\d+)@\[(.*)]:?(\d+)?", line)
            if sipobj:
                sipdict['msisdn'] = sipobj.group(1)
                sipdict['ipv6'] = sipobj.group(2)
                sipdict['port'] = sipobj.group(3)
                siplist.append(sipdict.copy())

    return json.dumps(siplist)



if __name__ == "__main__":
    app.run(port=5006)

