#Import Libraries
import random
import tweepy
import time

#Connect To Twitter API
auth = tweepy.OAuthHandler("INSERT-YOUR-API", "INSERT-YOUR-API")
auth.set_access_token("INSERT-YOUR-API", "INSERT-YOUR-API")
api = tweepy.API(auth)

#Set Font For Print
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
#Template1 - Beginning of Sentence
#Template2 - Beginning of Sentence
template1 = 'So I\'ve been using the'
template2 = 'for two weeks now'
template1 = str(template1)
template2 = str(template2)
#noChoice - Tweet When Finished
noChoice = 'I\'ve run out of entries to Tweet. Submit more at MKBHD-Bot.itsnoahevans.co.uk. Until @ThisIsNoahEvans has added the new ones, I\'ll shut down. See you soon!'
noChoice = str(noChoice)

#Print Status Update
print(colour.BOLD, colour.PURPLE, "Imported Libraries And Connected To The Twitter API", colour.END)

#Open File
entriesFile = open('entries.txt', 'r')
#Run for every entry in file
for chosenEntry in entriesFile:
    #Remove line
    chosenEntry = chosenEntry.replace("\n", "")
    #Add Choice To Template2
    tweetWithTemp2 = (chosenEntry + ' ' + template2)
    tweetWithTemp2 = str(tweetWithTemp2)
    #Remove characters
    tweetWithTemp2 = tweetWithTemp2.replace("]", "")
    tweetWithTemp2 = tweetWithTemp2.replace("{", "")
    tweetWithTemp2 = tweetWithTemp2.replace("[", "")
    tweetWithTemp2 = tweetWithTemp2.replace("]", "")
    tweetWithTemp2 = tweetWithTemp2.replace("}", "")
    tweetWithTemp2 = tweetWithTemp2.replace("'", "")
    tweetWithTemp2 = tweetWithTemp2.replace("(", "")
    tweetWithTemp2 = tweetWithTemp2.replace(")", "")
    tweetWithTemp2 = tweetWithTemp2.replace('"', '')
    #Merge All With Template1
    finalTweet = (template1 + ' ' + tweetWithTemp2)
    #Tweet
    api.update_status(finalTweet)
    #Print Status Update
    print(colour.BOLD, colour.GREEN, 'TWEETED:', finalTweet, colour.END)
    # Wait 30 minutes
    time.sleep(1800)



#ALL ENTRIES TWEETED#
#Tweet noChoice
api.update_status(noChoice)
#Print Error Message Forever
while True:
    print(colour.BOLD, colour.RED, 'SHUT DOWN DUE TO NO MORE ENTRIES', colour.RED)
    print()
