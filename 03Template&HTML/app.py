'''
1)How to render HTML files
2)How to work with templates
3)How to redirect
4)How to dynamically get url for specific end points
5)Working with Jinja2 templating engine
6)How to use filter,how to create custom filters
'''
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates') #Giving location of the html template

# To import the html file we use to import a method called render_template
@app.route('/')
def index():
    myvalue = "Neural Nine" # We can dynamically render the custom arguments
    myresult = 10+2
    mylist = [10,20,30,40]
    #here the keyword which we are using is used to access in html file
    # We can access in html by usng {{}} braces
    return render_template('index.html', myvalue=myvalue, myresult=myresult, mylist=mylist) #Here we have to just specify the path because here we already have selected the folder

# redirecting other page use href in html file and using any route url
@app.route('/other')
def other():
    some_text = "Hello World"
    return render_template('index2.html', some_text=some_text)

#Proper way to redirect
@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

# Creating custom filter for jinja
@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
    return s*times

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True) 