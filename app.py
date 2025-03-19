from flask import Flask, request, redirect
import random, string

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
        return f"Here’s your hidden link: http://127.0.0.1:5000/{short}"
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

if __name__ == '__main__':
    app.run(debug=True)


