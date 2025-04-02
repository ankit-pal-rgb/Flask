"""
1) Learning Forms and how to handle forms
2) How to sent post request using javascript using json data and how to handle it
3) How to upload files and how to process them and how to response for download
"""
from flask import Flask, render_template, request, Response, send_from_directory, jsonify
import pandas as pd
import os
import uuid # for random names

app = Flask(__name__, template_folder='templates')

'''So first here we will send get request to get the form and we will fill it
and send it back using post then we will process data for that we need request library'''

# url_for() generates a url for a function
# Create a Simple form in index.html
# T1
@app.route('/', methods = ['GET', 'POST']) # By default get is allowed in methods but if we want to chane it then we have to mention starting with get 
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('Username')     # If we sent request using form then we use request.form and for js request.json
        password = request.form.get('Password')

        if username == 'NeuralNine' and password == 'Password':
            return 'Success'
        else:
            return "Failure"

# T2
# To upload files we need to focus on specific input, change the form and access the file in different way
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files.get('file') # For files we use request.files

    if file.content_type == 'text/plain':
        return file.read().decode() # we use this for plain text file
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()

 # T3   
# Converting a excel file into csv file and making the file available for download
@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files.get('file')
    df = pd.read_excel(file)
    # We return response to use using Response
    # mimetype is content type
    response =  Response(
        df.to_csv(),
        mimetype='text/csv',
        headers = {
            'Content-Disposition' : 'attachment; filename : result.csv'
        }
    )
    return response

# T4
# Basically we first save the file in download directory and the url for download page then give them the file
@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
    file = request.files.get('file')
    df = pd.read_excel(file)

    # Here first we will check does the download directory exist or not if not then we will create
    if not os.path.exists('downloads'):
        os.mkdir('downloads')

    # We will save the file with this filename and return this name to html
    filename = f'{uuid.uuid4()}.csv'    
    df.to_csv(os.path.join('downloads',filename))

    return render_template('download.html', filename=filename)

# to return the download file we use sent_from_directory
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads', filename, download_name='result.csv')

# T5
# We use jsonify to return json object
# Handling javascript json data
@app.route('/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json.get('greeting')
    name  = request.json.get('name')
    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}')

    return jsonify({'message' : 'Successfully Written!'})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True) 