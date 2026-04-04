from flask import Flask, request, render_template
import requests

app = Flask(__name__)

BACKEND = "http://localhost:8000"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        query = request.form["query"]
        res = requests.post(f"{BACKEND}/query", json={"query": query})
        result = res.json()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)