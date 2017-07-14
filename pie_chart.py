from get_comments_list import get_comments_list

#importing matplot library - to plot the interests
import matplotlib.pyplot as plt

from textblob import sentiments

from delete_negative_comment import *

# 13. Function declaration to perform sentiment analysis

def pie_chart(insta_username):

    give_comments = get_comments_list(insta_username)

    for i in give_comments:
        sentiments = sentiments(str(i))
        print sentiments["sentiment"]

        if sentiments["sentiment"] > 0.75 :
            print "Positive sentments"
            global pos_sentiments
            pos_sentiments = pos_sentiments + 1

        elif sentiments["sentiments"] > 0.25 and sentiments["sentiments"] < 0.75 :
            print "Neutral sentments"
            global neut_sentiments
            neut_sentiments = neut_sentiments + 1

        else :
            print "Negative sentiments"
            global neg_sentiments
            neg_sentiments = neg_sentiments + 1

    labels = 'Positive Sentiments', 'Neutral Sentiments', 'Negative Sentiments'
    sizes = [pos_sentiments, neut_sentiments, neg_sentiments]
    explode = (0.1, 0.1, 0.1)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()
