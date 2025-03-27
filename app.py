from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Quotes categorized
quotes = {
    "motivational": [
        "Believe in yourself! 💪",
        "Work hard, stay humble. ✨",
        "Success is no accident. 🚀",
        "Push yourself, because no one else will do it for you. 🏆"
    ],
    "love": [
        "Love is not about how much you say ‘I love you,’ but how much you prove it’s true. 💕",
        "Love is the greatest refreshment in life. 🍷",
        "You are my today and all of my tomorrows. ❤",
        "Love is like the wind, you can’t see it but you can feel it. 🌬"
    ],
    "life": [
        "Life is a journey, not a race. 🚶‍♂",
        "Enjoy the little things. 🌼",
        "Live for today, plan for tomorrow, and party tonight. 🎉",
        "Happiness depends upon ourselves. 😊"
    ],
    "friendship": [
        "A friend is someone who knows all about you and still loves you. 👫",
        "Friendship is born at that moment when one person says to another: ‘What! You too?’ 🤩",
        "A true friend is the greatest of all blessings. 🌸",
        "Good friends are like stars. You don’t always see them, but you know they’re always there. ⭐"
    ],
    "happiness": [
        "Happiness is not something ready-made. It comes from your own actions. 🌈",
        "Smile, because it confuses people. 😆",
        "Happiness is like a butterfly, the more you chase it, the more it eludes you. 🦋",
        "You do not find a happy life. You make it. 💖"
    ]
}

@app.route("/history")
def history():
    return render_template("app.html")

@app.route("/quote")
def quote():
    return render_template("quote.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/")
def home():
    category = request.args.get("category", "motivational")
    random_quotes = random.choice(quotes[category])
    return render_template("app.html", quotes=random_quotes)

@app.route("/quotes", methods=["GET"])
def get_quotes():
    category = request.args.get("category", "motivational")
    random_quotes = random.choice(quotes[category])
    return jsonify({"quotes": random_quotes})



if __name__ == "__main__":
    app.run(debug=True)


