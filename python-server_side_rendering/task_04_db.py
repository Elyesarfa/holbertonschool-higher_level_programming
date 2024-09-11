from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

def read_sql():
    """Read data from an SQLite database."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except sqlite3.Error as e:
        return f"Database error: {e}", 500
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
    elif source == 'sql':
        products = read_sql()
        if isinstance(products, str):  # Handle database errors
            return render_template('product_display.html', error=products)
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
