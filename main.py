# dependencies
import requests;
import re;
import time;

# config
channel = "put channel here";
webhook = "put webhook link here";

lastUrl = "null";

# TODO: actually learn how to use youtube's api and other apis in general
while True:
    time.sleep(900); # cooldown to not exceed rate limits
    
    # look up the channel's videos and pick out the most recent one
    html = requests.get(channel + "/videos").text;
    url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group();
    
    # anti-spam system, check the latest video's url, if the bot has already sent a notification about it, restart the loop
    if url == lastUrl:
        continue;
    lastUrl = url;
    
    # format and post the data
    data = {
        "content" : "video message goes here" + " " + url,
        # "username" : "optional, can be configured directly on discord itself",
        # "avatar_url" : "this is also optional for the same reason"
    }
    result = requests.post(webhook, json = data);

    # check for errors
    try:
        result.raise_for_status();
    except requests.exceptions.HTTPError as error:
        print(error);
    else:
        print("payload delivered successfully! code {}.".format(result.status_code));
