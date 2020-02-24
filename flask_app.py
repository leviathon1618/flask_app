import webscraper
import jinja2
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    productlist = webscraper.work()
    return render_template("home.html", productlist = productlist)

if __name__ == "__main__":
    app.run(debug=True)