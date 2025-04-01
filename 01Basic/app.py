from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)       #Important parameter host, port and debug=True/False 
# If debug is true then we can continously change the code we will se the changes live