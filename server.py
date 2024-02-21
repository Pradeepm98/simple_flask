from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route and its corresponding function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application on port 80 and bind it to all available network interfaces
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
