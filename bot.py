import requests, setup, json, time

headers = {
    'Host': 'slack.com',
    'Content-type': 'application/json; charset=utf-8',
    'Authorization': 'Bearer ' + setup.USER_OAUTH_TOKEN
}

def getStatus(discord_presence_data):
    if(discord_presence_data['data']['listening_to_spotify']):
        return ["music", "Listening to " + discord_presence_data['data']['spotify']['song'] + " by " + discord_presence_data['data']['spotify']['artist']]
    else:
        for activity in discord_presence_data['data']['activities']:
            if (activity["name"] == "Visual Studio Code"):
                return ["code", activity["details"] + " in " + activity["state"]]
        return ["default", setup.default_status_message]
    
while True:
    status = getStatus(requests.get("https://api.lanyard.rest/v1/users/" + setup.DISCORD_ID).json())

    data = {
        'profile': {
            "status_text": status[1],
            "status_emoji": setup.emojis[status[0]],
            "status_expiration": 0 # never expire
        }   
    }

    requests.post(setup.REQUEST_URL, headers=headers, data=json.dumps(data))

    time.sleep(setup.REFRESH_INTERVAL)
