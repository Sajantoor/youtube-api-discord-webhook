# YouTube API Discord Webhook
## Uses the YouTube API and Discord webhook together to send a message when a channel uploads a video!

> This Python Script uses the YouTube API to search for videos (during a certain time span specified in the [JSON file](../master/keys.json)) to send a message, usually in the form of notifying server members that a new video from a certain channel has come out. This Python file is designed to run forever or until the user closes it. This Python script doesn't require access to your Google account, instead it takes publicly avalible information using a YouTube API Key.

## [JSON file](../master/keys.json)
If you don't know much about programming, programming in Python or don't want to mess with the Python file and easily make changes, you can use the JSON file to specifiy the [Channel ID](#Channel--ID), [YouTube Data V3 API Key](#YouTube--Data--V3--API--Key), [Discord Webhook URL](#Discord--Webhook--URL), [Start and End Time](#Start--and--End--Time), and [Delay Time](#Delay--Time). 

```js
{
  "channelID": "your channel id here",
  "APIKey": "your YouTube Data v3 API key here",
  "webhook": "your discord webhook url here",
  "startTime": "your start time here in 24 hour time (eg, 13:15) (make sure minutes are "2" not "02")",
  "endTime": "your end time here in 24 hour time (eg, 13:15) (make sure minutes are "2" not "02")"
  "delay": "your delay must be a whole number (in seconds)"
}
```

### Channel ID 
> This is used to indentify the channel you want to notify your Discord members about. If you want to find your channel ID, [click here](https://support.google.com/youtube/answer/3250431?hl=en). If you want to find another user's channel ID, [click here](https://commentpicker.com/youtube-channel-id.php)

### YouTube Data V3 API Key
> This Python script uses the YouTube Data V3 API to access YouTube. In order to use the YouTube Data V3 API, make sure to create a YouTube Data V3 API key. For more information: [click here](https://developers.google.com/youtube/v3/getting-started) 

### Discord Webhook URL
> The Discord Webhook URL allows the Python script to communicate with your webhook created on your discord server? Want more information about Discord's webhooks and how to create one: [click here](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks) 

### Start and End Time
> As the YouTube API has a quota and each action has a quota cost (100 quota cost in this case). It's important to not waste your precious quota. Therefore there is a start and end time which is used conserve the quota. Make sure your upload time is inbetween this start or stop time. If you want your start and stop time to run for long durations (for example an hour or more) make sure to change the delay time. 

### Delay Time
> The delay time is how long it takes to check if it's within the start and end time. This value is in seconds. Increase this value if you have start and stop time running for long duration to decrease quota usage. Remember you have 10,000 units of quota and each time it checks for a video it uses 100 units of quota. 

