#Import
import random
import tweepy
import time

#API
auth = tweepy.OAuthHandler("INSERT-YOUR-API", "INSERT-YOUR-API")
auth.set_access_token("INSERT-YOUR-API", "INSERT-YOUR-API")
api = tweepy.API(auth)

#Sets Font For Print
class colour:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

#Define Templates
template1 = 'So I\'ve been using the'
template2 = 'for two weeks now'
template1 = str(template1)
template2 = str(template2)
noChoice = 'I\'ve run out of entries to Tweet. Submit more at MKBHD-Bot.itsnoahevans.co.uk. Until @ThisIsNoahEvans has added the new ones, I\'ll shut down. See you soon!'
noChoice = str(noChoice)

print(colour.BOLD, colour.PURPLE, "Imported Libraries And Connected To The Twitter API", colour.END)

#Open File
entriesFile = open('entries.txt', 'r')
for chosenEntry in entriesFile:
    #Remove line
    chosenEntry = chosenEntry.replace("\n", "")
    # Add Choice To Template2
    tweetWithTemp2 = (chosenEntry + ' ' + template2)
    tweetWithTemp2 = str(tweetWithTemp2)
    # Remove characters
    tweetWithTemp2 = tweetWithTemp2.replace("]", "")
    tweetWithTemp2 = tweetWithTemp2.replace("{", "")
    tweetWithTemp2 = tweetWithTemp2.replace("[", "")
    tweetWithTemp2 = tweetWithTemp2.replace("]", "")
    tweetWithTemp2 = tweetWithTemp2.replace("}", "")
    tweetWithTemp2 = tweetWithTemp2.replace("'", "")
    tweetWithTemp2 = tweetWithTemp2.replace("(", "")
    tweetWithTemp2 = tweetWithTemp2.replace(")", "")
    tweetWithTemp2 = tweetWithTemp2.replace('"', '')
    # Merge All With Template1
    finalTweet = (template1 + ' ' + tweetWithTemp2)
    #Shorten Tweet And Add '[..]' If It Is Too Long
    finalTweet = finalTweet[:276] + (finalTweet[276:] and '[..]')
    # Tweet
    api.update_status(finalTweet)
    print(colour.BOLD, colour.GREEN, 'TWEETED:', finalTweet, colour.END)
    

#ALL ENTRIES TWEETED###
api.update_status(noChoice)
while True:
    print(colour.BOLD, colour.RED, 'SHUT DOWN DUE TO NO MORE ENTRIES', colour.RED)
    print()
