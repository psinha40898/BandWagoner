import API_test
import SA_test
from flask import Flask, render_template, request

app = Flask(__name__)

text = ""
@app.route('/') #This is the function that is run when the home page is visited 
def home():
    return render_template('demo2.html') 

@app.route('/submit', methods=['POST']) #This is the function that is run when the /submit page is visited
def submit():
    global text
    indices = []
    matches = []
    urls = []
    toplabels = []
    # SAword = str()
    SAlistoflists = []
    text = request.form['text']
    text2 = request.form['text2']
    found = True
    their_comments, urls, indices = API_test.search(API_test.reddit, text, text2)
    for i in range(len(indices)):
        matches.append(their_comments[indices[i]])
    
    if not matches:
        found = False
        matches.append(their_comments[0])
    
    if found:
        print("**Test 5: RUNNING SENTIMENT ANALYSIS ON A COMMENT**")
        for i, _ in enumerate(matches):
            print("Sentiment for Comment #", i, ": ")
            entirethinglist, justthelabel = SA_test.sentiment_AnalysisPT(matches[i])
            SAlistoflists.append(entirethinglist)
            toplabels.append(justthelabel)
            # SAword = SA_test.sentiment_AnalysisPT(matches[i])
            # SAlistoflists.append(SAword)

    print(SAlistoflists)
    return render_template('demo2.html', posts=matches, SAlist = SAlistoflists, labels = toplabels) + text2


if __name__ == '__main__':
    app.run(debug=True)