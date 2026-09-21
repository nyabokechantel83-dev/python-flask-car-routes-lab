from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


# Displays the welcome message
@app.route("/")
def home():
    return "Welcome to Flatiron Cars"


# Checks whether the requested model exists
@app.route("/<model>")
def car_model(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"

    return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(debug=True)