from ast import excepthandler
import tweepy



apikey = "W0U3SfDaRU67a6aGH8Q2JljKu"

apisecret = "fMfTenbSSmpAUMXAPbzgiIH7taxK7KUT6jvGWQp5u0JNsb17xC"

auth = tweepy.OAuthHandler(apikey,apisecret)

ACCESSTOK = "1560805940009619457-v4YMtggYrMxVKGRcmtzBeGk2gkWe2N"

TOK_SECRET = "t4WGhJfSBLYcIMwuu2SXeN3q2aF4lB9zv5v2AIejPEP1g"

auth.set_access_token(ACCESSTOK,TOK_SECRET)

client = tweepy.Client("YWEzNnlDOEZGamltdzQ2enVJNkw6MTpjaQ")

oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id="YWEzNnlDOEZGamltdzQ2enVJNkw6MTpjaQ",
    redirect_uri="https://twitter.com/MikesProject1",
    scope=["tweet.write", "tweet.read"],
    # Client Secret is only necessary if using a confidential client
    client_secret="_Pswxz46iyJ0h27muKwE_fGRouEiDCOrf_5vMc8u9ycOfzWQbi"
)

api = tweepy.API(auth);

try:
    api.verify_credentials()
    print("everything works")
except:
        ("Something is wrong, I can feel it.")


#api.update_status("First tweet from my python code!")


#This code allowed for me to follow my best friend on Twitter :)

#user = api.get_user(screen_name = "the_beegy")
#print(user.name)
#print(user.description)
#screen_name = "the_beegy"


#This code follows an account
#  api.create_friendship(screen_name=("the_beegy"))

#Liked and retweeted tweets below by using the tweet ID at the end of the URL

#Commented out code because duplicate actions will throw error

#api.retweet(1562624136324603904)
#api.create_favorite(1562144229593296896)

#This code below pull information of trending topics around New York specifically using NY's WOEID

#api.get_place_trends('2459115')
#print(api.get_place_trends('2459115'))

#Uploaded an image with media.

#api.update_status_with_media(status="This image is uploaded from #tweepy #python #LearnToCode",filename='Colosseum-Rome-Italy.png.webp')

api.get_follower_ids(screen_name='elonmusk')

#Below Code prints User Ids and followers of Elon Musk

#print(api.get_follower_ids(screen_name='elonmusk'))
#print(api.get_followers(screen_name='elonmusk'))

api.get_user(screen_name='Nasa')
print(api.get_user(screen_name='Nasa'))

#api.update_status("The beauty of science", in_reply_to_status_id = '1562314849912119296')
