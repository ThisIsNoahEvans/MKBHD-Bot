# MKBHD Bot
### The Twitter Bot **@MKBHDBot**

Here is the code for my Twitter bot, **MKBHD Bot**.
You can view and experiment with the code, but I don't recommend launching a bot similar to mine unless you change key features; Twitter users typically will only follow one account/bot if there are multiple providing the same service.

## Why?

This bot has been created as part of the recent joke around the tech YouTuber MKBHD. He gets some products to review (such as the 2019 Mac Pro) before they are released or even announced.

## Libraries Used

I used **Tweepy** to access Twitter - it's a very simple module to access Twitter through Python. It uses Twitter APIs, so your account will have to be a Twitter developer to get those APIs. Tweepy has a large amount of uses, but I only use the Tweet functionality. 

I used **Random** to choose a random entry - this is pretty simple and I'm sure most people who have used Python have used this at some point. Essentially, it picks a random word from *entries.txt* and then adds it to a variable.

And finally, I used **time** to manage timings and to ensure the bot 'sleeps' for 30 minutes before Tweeting again.

## Entries

**entries.txt** is a text file that I keep updated with submissions from the Google Form (*[here](http://mkbhd-bot.itsnoahevans.co.uk/submit.html)*). Responses are moderated by myself every Saturday, unless the bot is running low on data and may shut down.

## Thank You

A huge thank you to **KaamiDev** (*kaami.ca*) for helping with the API side of the bot, after Twitter rejected my Developer Request. (No, we did not bypass Twitter's developer system unethically.)
