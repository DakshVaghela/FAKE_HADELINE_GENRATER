from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

subjects = [
    "SRK", "VIRAT KOHLI", "MODI JI", "DAKSH",
    "ELON MUSK", "BILL GATES", "SALMAN KHAN", "ALIA BHATT", "RAHUL GANDHI"
]

actions = [
    "DANCING", "EATING", "SLEEPING", "DECLARE WAR",
    "SINGING", "CRYING", "JUMPING", "BUYING TWITTER", "GIVING SPEECH"
]

places = [
    "AT RED FORT", "IN LOCAL TRAIN", "AT NIRMA", "IN COUNTRY",
    "IN SPACE", "ON MOON", "AT IPL FINAL", "IN A CAVE", "AT G20 SUMMIT"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_news():
    sub = random.choice(subjects)
    act = random.choice(actions)
    pla = random.choice(places)

    headline = f"--BREAKING NEWS--: {sub} {act} {pla}"
    return jsonify({"headline": headline})

if __name__ == "__main__":
    app.run(debug=True)
