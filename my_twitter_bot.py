import os
import tweepy

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']

ACCES_KEY = os.environ['ACCES_KEY']
ACCES_SECRET = os.environ['ACCES_SECRET']

# AUTENTICAÇÃO
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCES_KEY, ACCES_SECRET)
api = tweepy.API(auth)

mentions = []
n = 0

mentions.append(api.search(q='eu quero morrer'))
print(mentions)

for mention in mentions[n]:

    texto = " Está se sentindo mal, com pensamentos ruins ou está passando por um momento difícil? Existem muitas pessoas que podem te ajudar, independente de seu problema! Ligue: 188 - É de graça!"
    api.update_status('@'+mention.user.screen_name + texto, mention.id)

    # print(mention)

    n += 1
