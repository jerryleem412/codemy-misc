# an object of WSGI application
from flask import Flask	
app = Flask(__name__) # Flask constructor

#http://localhost:5000

# A decorator used to tell the application
# which URL is associated function
@app.route('/')	
def hello():
	return 'HELLO'

if __name__=='__main__':
    app.run()
