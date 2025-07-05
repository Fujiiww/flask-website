from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('carros.json', 'r', encoding='utf-8') as f:
        carros = json.load(f)
    return render_template('home.html', carros=carros)

if __name__ == '__main__':
    app.run(debug=True)
