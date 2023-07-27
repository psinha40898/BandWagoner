import API_test
import SA_test
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='website/templates', static_folder='website/static')

print("starting")
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
    matchURLs = []
    toplabels = []
    # SAword = str()
    SAlistoflists = []
    text = request.form['text']
    text2 = request.form['text2']
    found = True
    #Searches for phrase in comment history of a username
    their_comments, urls, indices = API_test.search(API_test.reddit, text, text2)
    for i in range(len(indices)):
        matches.append(their_comments[indices[i]])
        matchURLs.append("https://reddit.com" + urls[indices[i]])
    #If invalid username or no matching comments
    if not matches:
        found = False
        if their_comments[0] == "No comments for invalid username":
            matches.append(their_comments[0])
            matchURLs.append(urls[0])
        else:
            matches.append("No matching comments found")
            matchURLs.append("#!")
    #Run SA on all matching comments
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
    return render_template('demo2.html', posts=matches, SAlist = SAlistoflists, labels = toplabels, hyperlinks = matchURLs) + text2


if __name__ == '__main__':
    app.run(debug=True)