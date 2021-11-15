from flask import Flask
import os
server = Flask(__name__)
# # Set environment variables
os.environ['api_key'] = 'abc'
# os.environ['API_PASSWORD'] = 'secret'

# # Get environment variables
# USER = os.getenv('API_USER')
# PASSWORD = os.environ.get('API_PASSWORD')       
# print(os.getenv('API_USER'))
# print(os.environ.get('API_PASSWORD'))
# print(os.environ)
@server.route("/")
def hello():
    return "abc"

if __name__ == "__main__":
    server.run(host='0.0.0.0')