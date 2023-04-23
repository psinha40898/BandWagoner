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
    text = request.form['text']
    text2 = request.form['text2']
    their_comments, urls = API_test.recentComments(None, API_test.reddit, text)
    API_test.isWord(text2, their_comments, indices)
    for i in range(len(indices)):
        matches.append(their_comments[indices[i]])
    
    print("**Test 5: RUNNING SENTIMENT ANALYSIS ON A COMMENT**")
    text = matches[0]
    text = SA_test.preprocess(text)
    encoded_input = SA_test.tokenizer(text, return_tensors='pt')
    output = SA_test.model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = SA_test.softmax(scores)
    ranking = SA_test.np.argsort(scores)
    ranking = ranking[::-1]
    for i in range(scores.shape[0]):
        l = SA_test.labels[ranking[i]]
        s = scores[ranking[i]]
        print(f"{i+1}) {l} {SA_test.np.round(float(s), 4)}")
    print("**End of Test 5 **")
    return render_template('demo.html', posts=matches) + text2


if __name__ == '__main__':
    app.run(debug=True)