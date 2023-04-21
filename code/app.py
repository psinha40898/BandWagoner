import API_test
from flask import Flask, render_template, request

app = Flask(__name__)

text = ""
@app.route('/') #This is the function that is run when the home page is visited 
def home():
    return render_template('index.html') 

@app.route('/submit', methods=['POST']) #This is the function that is run when the /submit page is visited
def submit():
    global text
    indices = []
    matches = []
    text = request.form['text']
    text2 = request.form['text2']
    their_comments, urls = API_test.recentComments(None, API_test.reddit, text)
    API_test.isWord(text2, their_comments, indices)
    for i in range(len(indices)):
        matches.append(their_comments[indices[i]])
    return render_template('index.html', posts=matches) + text2


if __name__ == '__main__':
    app.run(debug=True)