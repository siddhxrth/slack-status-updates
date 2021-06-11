# slack status updates ⚡️
### updates your slack status based on your discord rich presence using the data from the lanyard service

#### setup:
1)  join the [lanyard discord server](https://discord.gg/WScAm7vNGF) - this will expose your discord presence to a restful api which the bot will use to fetch your activity data
2) create a  new slack application and give it access to the ```users.profile:write``` scope - this will give the bot the permission to update your profile, which includes your status
3) the only changes you will need to make in the code are to the [setup.py](setup.py) file:
    1) update the ```USER_OAUTH_TOKEN``` with your **Bot User OAuth Token** - this is given by Slack when you create a new application
    2) update the ```DISCORD_ID``` field with your discord id (don't confuse this with your username, )
    3) update ```emojis``` with valid slack emoji ids (e.x. `:smile:`) for all of the fields (default, code, music" or it will not work. right now it only supports those three but more will be added soon
    4) update ```default_status_message``` with what you want your status to be when there are no activities in your discord presence
    5) OPTIONAL: you can change ```REFRESH_INTERVAL``` to what you would like (in seconds)
