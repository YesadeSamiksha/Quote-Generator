from flask import Flask, render_template, request, jsonify, redirect, url_for
import random

app = Flask(__name__)
import sqlite3

def init_db():
    conn = sqlite3.connect('contact.db')  # Create a database file
    cursor = conn.cursor()
    
    # Create a table for storing contact form submissions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

# Call the function to create the database
init_db()


# Quotes categorized
quotes = {
    "motivational": [
        "Believe in yourself and all that you are.",
        "Work hard in silence, let success make the noise.",
        "Success is the sum of small efforts repeated daily.",
        "Push yourself because no one else will do it for you.",
        "Dream big, work hard, stay focused, and surround yourself with good people.",
        "Do what you have to do until you can do what you want to do.",
        "The harder you work for something, the greater you'll feel when you achieve it.",
        "Great things never come from comfort zones.",
        "Stay patient and trust your journey.",
        "Difficult roads often lead to beautiful destinations.",
        "Do something today that your future self will thank you for.",
        "Your only limit is your mind.",
        "Opportunities don't happen, you create them.",
        "You don’t have to be great to start, but you have to start to be great.",
        "Failure is not the opposite of success, it is part of success."
    ],
    "love": [
        "Love is not about how much you say 'I love you' but how much you prove it's true.",
        "Love is the bridge between two hearts.",
        "The best thing to hold onto in life is each other.",
        "Love is when the other person's happiness is more important than your own.",
        "True love stories never have endings.",
        "Love is a choice you make every day.",
        "You don't love someone for their looks or their clothes, but because they sing a song only you can hear.",
        "The greatest thing you'll ever learn is just to love and be loved in return.",
        "Love is composed of a single soul inhabiting two bodies.",
        "To love and be loved is to feel the sun from both sides.",
        "Love is not finding someone to live with, it is finding someone you can't live without.",
        "Love does not dominate; it cultivates.",
        "We are most alive when we're in love.",
        "Love is the beauty of the soul.",
        "You are my today and all of my tomorrows."
    ],
    "life": [
        "Life is a journey, not a destination.",
        "Do what makes you happy, be with those who make you smile.",
        "Enjoy the little things, for one day you may look back and realize they were the big things.",
        "Live for today, hope for tomorrow.",
        "Happiness depends upon ourselves.",
        "Every moment is a fresh beginning.",
        "Life isn't about finding yourself, it's about creating yourself.",
        "Life is too important to be taken seriously.",
        "Do what you love and you'll never work a day in your life.",
        "Make each day your masterpiece.",
        "You only live once, but if you do it right, once is enough.",
        "Life is what happens when you're busy making other plans.",
        "The best way to predict your future is to create it.",
        "Life is really simple, but we insist on making it complicated.",
        "The purpose of life is not to be happy, but to be useful."
    ],
    "friendship": [
        "A friend is someone who knows all about you and still loves you.",
        "True friendship is never serene.",
        "Friendship is not about who you’ve known the longest, it’s about who came and never left your side.",
        "A real friend is one who walks in when the rest of the world walks out.",
        "A true friend is the greatest of all blessings.",
        "Friendship doubles your joys and divides your sorrows.",
        "Friends are the family we choose for ourselves.",
        "A friend is someone who gives you total freedom to be yourself.",
        "Many people will walk in and out of your life, but only true friends leave footprints in your heart.",
        "Good friends are like stars. You don’t always see them, but you know they’re always there.",
        "One loyal friend is worth ten thousand relatives.",
        "A friend to all is a friend to none.",
        "Friendship isn’t about whom you’ve known the longest, it’s about who came and never left your side.",
        "A true friend accepts who you are but also helps you become who you should be.",
        "A good friend is like a four-leaf clover: hard to find and lucky to have."
    ],
    "happiness": [
        "Happiness is not something ready-made, it comes from your own actions.",
        "Smile, not because life is easy, but because you choose to be happy.",
        "Happiness depends on what you decide to focus on.",
        "You do not find a happy life, you make it.",
        "Happiness is not a goal, it is a by-product of a life well-lived.",
        "The happiest people don’t have the best of everything, they make the best of everything.",
        "Happiness is letting go of what you think your life is supposed to be and celebrating it for everything that it is.",
        "The secret of happiness is freedom, and the secret of freedom is courage.",
        "Happiness is a choice, not a result. Nothing will make you happy until you choose to be happy.",
        "Happiness is like a butterfly; the more you chase it, the more it will elude you.",
        "A happy heart makes a cheerful face.",
        "Happiness is enjoying the simple things in life.",
        "Be so happy that when others look at you, they become happy too.",
        "Happiness is not in things, it is in us.",
        "Happiness is not a destination, it is a way of life."
    ],

    
    "Movie":[
        
        "Mogambo khush hua! – Mogambo",
    "Kitne aadmi the? – Gabbar Singh",
    "Don ko pakadna mushkil hi nahi, naamumkin hai. – Don",
    "Zindagi mein do cheez kabhi mat bhoolna, ek teri maa ka ashirwad, doosra apne desh ka namak. – Babu Moshai",
    "Dilwale Dulhania Le Jayenge. – Raj",
    "Tension lene ka nahi, dene ka. – Jai",
    "Tumse na ho payega. – Chulbul Pandey",
    "Jab tak tumhare paas apne haath hain, tab tak kuch bhi mumkin hai. – Raj",
    "Rishte mein toh hum tumhare baap lagte hain, naam hai Shahenshah. – Shahenshah",
    "Aaj khush toh bahut honge tum. – Gabbar Singh"
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


# Function to insert contact form data into the database
def insert_contact(name, email, message):
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

@app.route('/app')
def app_page():
    return render_template('app.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    insert_contact(name, email, message)  # Store data in the database

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)




