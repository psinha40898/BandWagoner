import API_test
import SA_test
from flask import Flask, render_template, request

app = Flask(__name__)

text = ""
@app.route('/') #This is the function that is run when the home page is visited 
def home():
    return render_template('demo.html') 

@app.route('/submit', methods=['POST']) #This is the function that is run when the /submit page is visited
def submit():
    global text
    indices = []
    matches = []
    urls = []
    text = request.form['text']
    text2 = request.form['text2']
    their_comments, urls, indices = API_test.search(API_test.reddit, text, text2)
    for i in range(len(indices)):
        matches.append(their_comments[indices[i]])
    
    print("**Test 5: RUNNING SENTIMENT ANALYSIS ON A COMMENT**")
    for i, _ in enumerate(matches):
        print("Sentiment for Comment #", i, ": ")
        SA_test.sentiment_AnalysisPT(matches[i])
    return render_template('demo.html', posts=matches) + text2


if __name__ == '__main__':
    app.run(debug=True)