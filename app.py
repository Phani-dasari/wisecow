from flask import Flask
import subprocess
import requests

app = Flask(_name_)

@app.route("/")
def wisecow():
    # get a random quote
    try:
        quote = requests.get("https://api.quotable.io/random").json()["content"]
    except:
        quote = "Stay positive, work hard, make it happen."

    # run cowsay with the quote
    cow = subprocess.getoutput(f'echo "{quote}" | cowsay')
    return f"<pre>{cow}</pre>"

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8080)