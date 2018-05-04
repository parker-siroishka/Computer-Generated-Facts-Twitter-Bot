from markovbot import MarkovBot
import time

tweetbot = MarkovBot()
# Get the current directory's path
dirname = r"C:\Users\parke\Desktop\Projects\Python Projects\Twitter bot\tweetBot-MarkovBot"
# Construct the path to the text
text = r"C:\Users\parke\Desktop\Projects\Python Projects\Twitter bot\tweetBot-MarkovBot\facts.txt"
# Make your bot read the book
tweetbot.read(text)

# API Key
cons_key = ''
# API Secret
cons_secret = ''
# Access Token
access_token = ''
# Access Token Secret
access_token_secret = ''

tweetbot.twitter_login(cons_key,cons_secret,access_token,access_token_secret)

prefixes=None

suffix="#ComputerGeneratedFacts"
# Start periodically tweeting
tweetbot.twitter_tweeting_start(days=0, hours=1, minutes=30, keywords=None,prefix=prefixes, suffix=suffix)
# DO SOMETHING HERE TO ALLOW YOUR BOT TO BE ACTIVE IN THE BACKGROUND
secsinweek = 7*24*60*60
time.sleep(secsinweek)
