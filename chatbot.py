import random

import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings


from newspaper import Article

warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)


article = Article(
    'https://www.healthline.com/health/top-10-deadliest-diseases')
article.download()
article.parse()
article.nlp
c = article.text


# print(c)

# tokenization
text = c
sentence_list = nltk.sent_tokenize(text)

# print(sentence_list)

# return a random greeting response to a users greeting


def greeting_response(text):
    text = text.lower()
    bot_greetings = ['howdy', 'hi', 'hello', 'hey ', 'hola']
    user_greeting = ['hi', 'hello', 'hey ', 'hola', 'wassup', 'greeting']
    for word in text.split():
        if word in user_greeting:
            return random.choice(bot_greetings)


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index


def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ""
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+' '+sentence_list[index[i]]
            response_flag = 1
            j = j+1
        if j > 2:
            break

    if(response_flag == 0):
        bot_response = bot_response+'i apologise i dont understand '
    sentence_list.remove(user_input)
    return bot_response


# start the chat
print('DocBot: I am Doctor bot,I will answer your queries on kidney type disease')
exit_list = ['exit', 'bye', 'see ya', 'die', 'quit', 'ttyl']
while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('Doc Bot :Chat with ya later!')
        break
    else:
        if greeting_response(user_input) != None:
            print('Doc Bot'+" "+greeting_response(user_input))
        else:
            print("Doc Bot"+bot_response(user_input))
