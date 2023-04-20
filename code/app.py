import API_test
from flask import Flask, render_template, request

app = Flask(__name__)

text = ""
comments, urls = API_test.recentComments(5, API_test.reddit, API_test.target_user)
@app.route('/') #This is the function that is run when the home page is visited 
def home():
    their_comments = comments
    return render_template('index.html', posts=their_comments)

@app.route('/submit', methods=['POST']) #This is the function that is run when the /submit page is visited
def submit():
    global text
    text = request.form['text']
    return 'Text received!' + text

if __name__ == '__main__':
    app.run(debug=True)