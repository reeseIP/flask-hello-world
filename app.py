# Flask Hello World

# import the Flask class form the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

app.config['DEBUG'] = True

# define route and controller for URL/
@app.route("/")
def home_page():
    return 'You have reached the home page'

# define route and controller for URL/hello
@app.route("/hello")
def hello_world():
    return "Hello, World!!!!!!"
    
@app.route('/name/<name>')
def handle_name(name):
    if name.lower() == 'alex':
        return 'Hello, {}'.format(name), 200
    else:
        return 'Not Found', 404
    
@app.route("/int/<int:value>")
def convert_int(value):
    print(value + 1)
    return 'correct'
        
@app.route('/float/<float:value>')  
def convert_float(value):
    print(value + 1)
    return 'correct'
        
@app.route('/path/<path:value>')
def handle_path(value):
    print(value)
    return 'correct'
    
# route and controller for URL/test
@app.route("/test/<search_query>")
def search_query(search_query):
    return search_query
    
# start the development server using the run() method
if __name__ == "__main__":
    app.run()