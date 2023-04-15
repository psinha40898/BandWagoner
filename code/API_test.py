import praw
import SA_test
reddit = praw.Reddit(client_id='sPNq5pCTFiTsVjiIlYCSmw', 
                     client_secret='LNKS63p0vFfaR896JB5zhTTa7fI8aw', 
                     user_agent='This is a just a test by /u/acamess9298')

subreddit = reddit.subreddit('Dota2')
target_user = 'acmess9298'


print("**Test 1: SUBREDDIT TOP POST API CALL with limit of 10**")
for i, post in enumerate(subreddit.top(limit=10)):
    print(i+1, post.title)
print("**End of Test 1**")

print("**Test 2: USER RECENT COMMENTS API CALL with limit of 4**")
comment_history = [] 
for i, comment in enumerate(reddit.redditor(target_user).comments.new(limit=4)):
    comment_history.append(comment.body)
    print(i+1, ")", comment_history[i])
print("**End of Test 2**")

print("**Test 3: SEARCHING FOR A PHRASE IN ONE COMMENT**")
sentence = comment_history[0]
word = "punch"
if word in sentence:
    print("The word", word, "was found")
else:
   print("The word", word, "was NOT found")
print("**End of Test 3**")

print("**Test 4: SEARCHING FOR A PHRASE IN A LIST OF COMMENTS**")
word = "punch"
for comment in comment_history:
    if word in comment:
        print(word, "was found in comment #", comment_history.index(comment)+1)
print("**End of Test 4**")

print("**Test 5: RUNNING SENTIMENT ANALYSIS ON A COMMENT**")
text = "This guy acts like a clown and thinks he's tough for calling out ARIEL HELWANI LOL wtf"
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