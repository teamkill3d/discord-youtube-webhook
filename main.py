# dependencies
import requests;
import re;
import time;

# config
channel = ""; # place channel url here
webhook = ""; # place webhook url here

lastUrl = "null";

while True:
    time.sleep(900); # cooldown to not exceed rate limits
    
    # look up the channel's videos and pick out the most recent one
    html = requests.get(channel + "/videos").text;
    url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group();
    
    # anti-spam
    if url == lastUrl:
        continue;
    lastUrl = url;
    
    # format and post the data
    data = {
        "content" : "video message goes here" + " " + url,
        # "username" : "", both of these options can be configured on discord itself
        # "avatar_url" : ""
    }
    result = requests.post(webhook, json = data);

    # check for errors
    try:
        result.raise_for_status();
    except requests.exceptions.HTTPError as error:
        print(error);
    else:
        print("payload delivered successfully! code {}.".format(result.status_code));
