from flask import Flask, request, redirect, render_template
import random, string
import os

app = Flask(__name__)
links = {}

def random_string(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def home():
    masked_link = None
    if request.method == 'POST':
        url = request.form['url']
        short = random_string()
        links[short] = url
        masked_link = f"https://fn-random-link-generator.onrender.com/{short}"
        return render_template('index.html', masked_link=masked_link)
    return render_template('index.html', masked_link=masked_link)

@app.route('/<short>')
def go(short):
    if short in links:
        return redirect(links[short])
    return "Oops! Link not found."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

