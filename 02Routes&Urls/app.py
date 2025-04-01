from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

#Handling multiple methods and returning status code
@app.route('/hello', methods=['GET', 'POST', 'PUT']) #Here we can pass methods list
def hello():
    if request.method == 'GET':
        return "You made a GET request", 200 #It is by default 200 we can change it
    elif request.method == 'POST':
        return 'You made a POST request', 200
    return "You will never see this message"

# Basically when we send a GET request then we get a HTML form to fill out and after filling that form we send POST reuqest
@app.route('/greet/<name>') #here <name> means it's a variable and whatever I will write in browser at name it will use that
def greet(name):            # <name> is also called URL processor
    return f"Hello {name}"

# We can make custom responses using make_response
@app.route('/add/<int:number1>/<int:number2>')  #Here deault parameters are in string and we can specify the type also
def add(number1, number2):
    response = make_response(f'{number1} + {number2} = {number2+number1}')
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response

# Handling URL paramters
@app.route('/handle_url_params')
def handle_params():
    if 'greetings' in request.args.keys() and 'name' in request.args.keys():  #We should always check whether the key is present or not otherwise it will give errors
        greeting = request.args["greeting"]
        name = request.args["name"]
        return f'{greeting} {name}'      #If we import request then the params are store in dictionary in request.args
    else:
        return 'some parameters'         # It's an empty immutable dictionary
                                         # Use http://127.0.0.1:5555/handle_url_params?name=mike
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)