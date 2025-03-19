from flask import Flask, request, redirect
import random, string
import os

app = Flask(__name__)
links = {}

def random_string(length=6):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        url = request.form['url']
        short = random_string()
        links[short] = url
        return f"Here’s your hidden link: https://fn-random-link-generator.onrender.com/{short}"
    return '''
    <h1>Link Hider</h1> 
    <form method="POST">
        Link: <input name="url">
        <input type="submit">
    </form>
    '''

@app.route('/<short>')
def go(short):
    if short in links:
        return redirect(links[short])
    return "Oops! Link not found."

# 🧩 Correct Run Command for Render:
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

