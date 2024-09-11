from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # Read data from JSON file
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return "Error: items.json file not found.", 404
    except json.JSONDecodeError:
        return "Error: items.json file is not a valid JSON.", 500

    # Extract items from JSON data
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
