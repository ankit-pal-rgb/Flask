'''
1) Learning Session Management and Cookie Management
2) Message Flashing
'''
# In session and cookie we store information across multiple request bcz http is stateless meaning it just exchange request and response does not keep information about overall exchange
# we keep session information on server side and cookie on client side
# If we want to keep something for security purpose we keep that in session on server side
# Something that we are not concerned with changing is kept on client side bcz client can change that information
# To make it more secure just share session id in cookie and sign it with a security key this make session more secure
from flask import Flask, render_template, session, make_response, request, flash

app = Flask(__name__, template_folder='templates')
# So first step is if we want to use session than we have to setup a security key to signup for encryption
# For implementation use good security key

app.secret_key='SOME KEY' # Using these scret key we can issue session id and keep track of session and clients

@app.route('/')
def index():
    return render_template('index.html', message='Index')

# We need to import session
@app.route('/set_data')
def set_data():
    session['name'] = 'Ankit'
    session['other'] = 'Hello World'  # The entered data will stored in session and it will be associated with session id
    return render_template('index.html', message='Session data Set')

# If we delete the session id from browser then user can not get session data
@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
        return render_template('index.html', message=f' Name : {name} , other : {other}')
    else:
        return render_template('index.html', message = 'No session found')

# Clear the session
@app.route('/clear_session')
def clear_session():
    session.clear()    
    return render_template('index.html', message='Session Cleared')

# To set cookie we need to sent response to the browser that instruct to set cookie for client
@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message='Cookie Set'))
    response.set_cookie('cookie_name', 'cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index.html', message=f'cookie value : {cookie_value}')

# To remove cookie we need to make response and set expires=0
@app.route('/remove_cookie')
def remove_cookie():
    response=make_response(render_template('index.html', message='cookie_removed'))
    response.set_cookie('cookie_name', expires=0)
    return response

# When the user perform login or some event happens we dislpay a flash message and we write it in html
# We need to import flash module
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
            username = request.form.get('username')
            password = request.form.get('password')
            if username == 'neuralnine' and password == '12345':
                flash('Successful Login!')
                return render_template('index.html')
            else:
                flash('Login Failed!')
                return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
