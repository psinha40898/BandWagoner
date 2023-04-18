import praw
import SA_test
reddit = praw.Reddit(client_id='sPNq5pCTFiTsVjiIlYCSmw', 
                     client_secret='LNKS63p0vFfaR896JB5zhTTa7fI8aw', 
                     user_agent='This is a just a test by /u/acamess9298')

subreddit = reddit.subreddit('Dota2')
target_user = 'Stanklord500'

def topSub(x, reddit_var, sub_var):
    print("***Success! Testing Subreddit Top Post API call with limit of ", x, "***")
    for i, post in enumerate(sub_var.top(limit=x)):
        print(i+1, post.title)
    print("***End of Test***")

def recentComments(x, reddit_var, user_var):
    print("***Success! Testing Reddit User Recent Comments API call with limit of", x ,"***")
    comment_history = []
    comment_urls = []
    for i, comment in enumerate(reddit_var.redditor(user_var).comments.new(limit=x)):
        comment_history.append(comment.body)
        comment_urls.append(comment.permalink)
        print(i+1, ")", comment_history[i])
    print("***End of Test***")
    return comment_history, comment_urls


def isWord_sen(word, sentence, i, indices):
    if word in sentence:
        print("The word", word, "was found in comment #", i+1)
        indices.append(i)

def isWord(word, list, indices):
    for i, comment in enumerate(list):
        isWord_sen(word, list[i], i, indices)



topSub(10, reddit, subreddit) # Test 1
comments = recentComments(1500, reddit, target_user)[0] # Test 2
urls = comments = recentComments(1500, reddit, target_user)[1] # Test 2
my_indices = []
isWord("gane", comments, my_indices)
isWord("Gane", comments, my_indices)
print(my_indices)

for i, _ in enumerate(my_indices):
    print( "#", i+1, "overall comment #", my_indices[i], "START",  comments[my_indices[i]], "END")
# print("**Test 3: SEARCHING FOR A PHRASE IN ONE COMMENT**")
# sentence = "Is punch in this sentence?"
# word = "punch"
# if word in sentence:
#     print("The word", word, "was found")
# else:
#    print("The word", word, "was NOT found")
# print("**End of Test 3**")

# print("**Test 4: SEARCHING FOR A PHRASE IN A LIST OF COMMENTS**")
# word = "punch"
# for comment in comments:
#     if word in comment:
#         print(word, "was found in comment #", comments.index(comment)+1)
# print("**End of Test 4**")

print("**Test 5: RUNNING SENTIMENT ANALYSIS ON A COMMENT**")
text = comments[468]
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



for link in urls:
    print(link)