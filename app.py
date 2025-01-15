from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Insecure hardcoded credentials
users = {'admin': 'password123'}

@app.route('/')
def home():
    return 'Welcome to the secure code review tutorial!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('admin'))
        else:
            return 'Invalid credentials', 401
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/admin')
def admin():
    return 'Welcome to the admin page!'

@app.route('/xss', methods=['GET', 'POST'])
def xss():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # Unsafe handling of user input
        return render_template_string(f'<p>{user_input}</p>')
    return '''
        <form method="post">
            Enter text: <input type="text" name="user_input"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

