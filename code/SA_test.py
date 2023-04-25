from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request

# Preprocess text (username and link placeholders)
# Replaces usernames with just "user" and replaces links with just "http"



# Tasks:
# emoji, emotion, hate, irony, offensive, sentiment
# stance/abortion, stance/atheism, stance/climate, stance/feminist, stance/hillary

# 1 Makes the code more portable
# 2 Stores String that will be cache directory and also specifies a location in the Transformers Library from Huggingface
task='sentiment' 
MODEL = f"cardiffnlp/twitter-roberta-base-{task}" 

# Loads tokenizer from Huggingface Transformers Library into tokenizer
# MODEL specifies a location in the Transformers Library from Huggingface
tokenizer = AutoTokenizer.from_pretrained(MODEL) 


# 1 Creates an empty list named labels
# 2 Creates a StringURL that holds the sentiment mapping URL (0 negative, 1 neutral, 2 positive)
# 3 The contents of the URL are loaded into f which is a file type object
# 4 The contents of the URL are split by new lines and put into html which is a list of those strings
# 5 The contents of html are put into a CSV table called csvreader
# 6 The second column of the table is put into labels (negative, neutral, positive)
labels=[] # 1
mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt" 
with urllib.request.urlopen(mapping_link) as f: 
    html = f.read().decode('utf-8').split("\n") 
    csvreader = csv.reader(html, delimiter='\t') 
labels = [row[1] for row in csvreader if len(row) > 1] # 6



# Loads a model from the Huggingface Transformers Models Hub Library into the variable model
# Saves it to disk as cache 
# Saves the tokenizer to disk as cache
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
model.save_pretrained(MODEL)
tokenizer.save_pretrained(MODEL)

# text = "Really good night!"
# text = preprocess(text)
# encoded_input = tokenizer(text, return_tensors='pt')
# output = model(**encoded_input)
# scores = output[0][0].detach().numpy()
# scores = softmax(scores)
def preprocess(text):
    new_text = []
 
 
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)


def sentiment_AnalysisPT(text):
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    for i in range(scores.shape[0]):
        l = labels[ranking[i]]
        s = scores[ranking[i]]
        print(f"{i+1}) {l} {np.round(float(s), 4)}")

# sentiment_AnalysisPT("Really good night!")
# sentiment_AnalysisPT("You suck. I hate you.")
# sentiment_AnalysisPT("Really good night!")




# print("Second text start")
# text = "Bad night!"
# text = preprocess(text)
# encoded_input = tokenizer(text, return_tensors='pt')
# output = model(**encoded_input)
# scores = output[0][0].detach().numpy()
# scores = softmax(scores)

# # TF
# model = TFAutoModelForSequenceClassification.from_pretrained(MODEL)
# model.save_pretrained(MODEL)

# text = "Good night 😊"
# encoded_input = tokenizer(text, return_tensors='tf')
# output = model(encoded_input)
# scores = output[0][0].numpy()
# scores = softmax(scores)

# ranking = np.argsort(scores)
# ranking = ranking[::-1]
# for i in range(scores.shape[0]):
#     l = labels[ranking[i]]
#     s = scores[ranking[i]]
#     print(f"{i+1}) {l} {np.round(float(s), 4)}")