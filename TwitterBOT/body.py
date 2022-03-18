import tweepy
import logging
import time
import random
from datetime import datetime, timedelta
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from config import create_api
api = create_api()


def check_for_followers(api,accounts,followers):
    print(accounts)
    print(followers)

    while True:


        time.sleep(23)
        for i in range(len(accounts)):
            for user in tweepy.Cursor(api.friends, screen_name=accounts[i]).items(5):
                time.sleep(10)
                print("checking for new followings of "+accounts[i])
                latest_following = str(user.screen_name)
                if (latest_following not in followers[i]):
                    followers[i].append(latest_following)
                    print(latest_following + " is followed by " + accounts[i])
                    message=accounts[i]+" just followed " + latest_following +" \nClick on this link to view the profile : https://twitter.com/"+latest_following
                    print(message)
                    base_url='https://api.telegram.org/bot5164911526:AAG9Z8Nxm72MoGCc3jkHrwzb52J0TP7ZUrs/sendMessage?chat_id=-654257019&text={}'.format(message)
                    requests.get(base_url)
                    time.sleep(5)


        

        
        

        ran=[10,15,13,15,9,16,5,7,9]
        choice=random.choice(ran)
        #time.sleep(choice*60)
            
    

#initial adding of followers to the array

accounts=["@Theyozz_"]
followers=[]
for user in accounts:
    followers.append([])

for i in range(len(accounts)):
    for user in tweepy.Cursor(api.friends, screen_name=accounts[i]).items(10):
        new_follower=str(user.screen_name)
        followers[i].append(new_follower)
    

print(followers)


#first 20





#calling main function

while True:
    print("collected initial datas")
    time.sleep(119)
    check_for_followers(api,accounts,followers)
    time.sleep(10*5)
print('\n\n\n                   finished following all                           ')

