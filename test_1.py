# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# '/' URL is bound with hello_world() function.
def hello_world():
	return 'Hello World'  

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
	
    # import the Flask library
from flask import Flask, render_template, request


# Create the Flask instance and pass the Flask
# constructor the path of the correct module
app = Flask(__name__)

# The URL 'localhost:5000/square' is mapped to
# view function 'squarenumber'
# The GET request will display the user to enter
# a number (coming from squarenum.html page)


@app.route('/', methods=['GET'])
def squarenumber():
	# If method is GET, check if number is entered
	# or user has just requested the page.
	# Calculate the square of number and pass it to
	# answermaths method
	if request.method == 'GET':
# If 'num' is None, the user has requested page the first time
		if(request.args.get('num') == None):
			return render_template('squarenum.html')
		# If user clicks on Submit button without
		# entering number display error
		elif(request.args.get('num') == ''):
			return "<html><body> <h1>Invalid number</h1></body></html>"
		else:
		# User has entered a number
		# Fetch the number from args attribute of
		# request accessing its 'id' from HTML
			number = request.args.get('num')
			sq = int(number) * int(number)
			# pass the result to the answer HTML
			# page using Jinja2 template
			return render_template('answer.html',
								squareofnum=sq, num=number)


# Start with flask web app with debug as
# True only if this is the starting page
if(__name__ == "__main__"):
	app.run(debug=True)