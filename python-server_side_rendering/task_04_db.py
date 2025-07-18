from flask import Flask, render_template, request
import json
import csv
import sqlite3


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
    file = open('items.json', 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    items_list = data["items"]
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get("source")
    id = request.args.get("id")

    if source == 'csv':
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            products = []
            if id:
                products = None
                for row in reader:
                    if int(row["id"]) == int(id):
                        products = [row]
                        return render_template('product_display.html', products=products)
                if not products:
                    return render_template('product_display.html', error="Product not found")
            else:
                for row in reader:
                    products.append(row)
                return render_template('product_display.html', products=products)

    elif source == 'json':
        with open('products.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        if id:
            products = None
            for product in data:
                if product["id"] == int(id):
                    products = [product]
                    return render_template('product_display.html', products=products)
            if not products:
                return render_template('product_display.html', error="Product not found")
        else:
            products = data
            return render_template('product_display.html', products=products)
    else:
        return render_template('product_display.html', error="Wrong source")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
