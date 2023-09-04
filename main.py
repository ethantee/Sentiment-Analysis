# Installing the required libraries
!pip install nltk
!pip install matplotlib

# Importing the required libraries
from collections import Counter
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import nltk
import string

# Downloading the nltk packages
nltk.download() # only for the first time

# Opening the text file and reading it
# Link to the Speech by U.S. Rep. John Lewis in 2018: https://news.harvard.edu/gazette/story/2022/05/6-memorable-harvard-commencement-speeches/
text = open('text.txt', encoding = 'utf-8').read()

# Converting the text to lower case
lower_case = text.lower()

# Removing the punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Tokenising the words
tokenised_words = word_tokenize(cleaned_text, "english")

# Create a empty list to store the words after removing the stop words
cleaned_words = []

# Removing the stop words from the tokenised words list
for word in tokenised_words:
    if word not in stopwords.words('english'):
        cleaned_words.append(word)

# Emotion Detection
emotion_list = []

with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '')
        word, emotion = clear_line.split(':')
        
        if word in cleaned_words:
            emotion_list.append(emotion)

# Counting the emotions
emotion_count = Counter(emotion_list)
print(emotion_count)

# Sentiment Analysis
def sentiment_analyser(text):
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    print(score)    
    
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")
        
sentiment_analyser(cleaned_text)

# Plotting the emotions on a bar graph
fig, ax1 = plt.subplots()
ax1.bar(emotion_count.keys(), emotion_count.values())
fig.autofmt_xdate()
plt.savefig('bar_graph.png')
plt.show()