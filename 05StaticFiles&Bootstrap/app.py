'''
1) How to work with static files meaning how to work with images, css files and javascript files
'''
from flask import Flask, render_template

# To work with images and static files we create static folder and add a url path
# Inside this static folder we have different dirctories depending on the file type
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

# To use the image in html go to the html file and use the img tag
# To work with images and static files we create static folder and add a url path
# After creating the static folder and writing code for it we have mention and use this file directly in html
@app.route('/')
def index():
    return render_template('index.html')

# To inculde bootstrap download the compile filed and extract it and then move the js and css in static folder within css and js and mention it in html
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)