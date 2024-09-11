from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(filename):
    """Read data from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

def read_csv(filename):
    """Read data from a CSV file."""
    products = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['price'] = float(row['price'])  # Convert price to float
            row['id'] = int(row['id'])           # Convert id to int
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source == 'json':
        try:
            products = read_json('products.json')
        except FileNotFoundError:
            return render_template('product_display.html', error="JSON file not found.")
        except json.JSONDecodeError:
            return render_template('product_display.html', error="Error decoding JSON file.")
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
        except FileNotFoundError:
            return render_template('product_display.html', error="CSV file not found.")
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filter products by id if provided
    if product_id:
        product_id = int(product_id)  # Ensure id is an integer
        filtered_products = [p for p in products if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found.")
        products = filtered_products

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
