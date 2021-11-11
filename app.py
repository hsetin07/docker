from flask import Flask
import os 
server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello Flask1"

if __name__ == "__main__":
    server.run(host='0.0.0.0')    

# Set environment variables
os.environ['API_USER'] = 'username'
os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')

    print(os.environ)