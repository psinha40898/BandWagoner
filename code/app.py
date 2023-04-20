from flask import Flask, render_template, request

app = Flask(__name__)

text = ""

@app.route('/') #This is the function that is run when the home page is visited 
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST']) #This is the function that is run when the /submit page is visited
def submit():
    global text
    text = request.form['text']
    return 'Text received!' + text

if __name__ == '__main__':
    app.run(debug=True)