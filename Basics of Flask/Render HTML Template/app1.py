from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('new_user.html', name=name)

if __name__ == '__main__':
         
        app.run(debug=True)
# The render_template function in this script is the key to rendering templates.
# This function takes a template filename and a variable list of template arguments and returns the same template, but with all the placeholders in it replaced with actual values.

# The templates in this example are stored in a folder called templates in the root of the application package.