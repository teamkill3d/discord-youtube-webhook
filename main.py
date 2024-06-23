# dependencies
import requests
import re
import time

# config
channel = "put channel here"
webhook = "put webhook link here"

# variables !!!DO NOT EDIT!!!
lastUrl = "osjidfoascdmrosuierpds"

while True:
    time.sleep(900) # cooldown to not exceed rate limits TODO: this is a stupid solution, will fix when i get better at programming (or if someone fixes it for me)
    
    # look up the channel's videos and pick out the most recent one
    html = requests.get(channel + "/videos").text
    url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
    
    # anti-spam system, check the latest video's url, if the bot has already sent a notification about it, restart the loop
    if url == lastUrl:
        continue
    lastUrl = url # update the anti-spam system
    
    # format and post the data
    data = {
        "content" : "video message goes here" + " " + url,
        #"username" : "optional, can be configured directly on discord itself",
        #"avatar_url" : "this is also optional for the same reason"
    }
    result = requests.post(webhook, json = data)

    # check for errors
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(error)
    else:
        print("payload delivered successfully! code {}.".format(result.status_code))
