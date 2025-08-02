from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the homepage!"

@app.route("/products")
def products():
    return "Here are some products."

@app.route("/cart")
def cart():
    return "Your cart is empty."

if __name__ == "__main__":
    app.run(port=5000)