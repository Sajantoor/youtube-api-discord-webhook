import os
import json
import googleapiclient.discovery
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime, time
from time import sleep
# Variables
previousVideo = False;

# Get secret keys from JSON file
with open('keys.json') as json_file:
    key = json.load(json_file)
# Process secrets
startTime = key["startTime"]
endTime = key["endTime"]

# YouTube API Stuffs
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = key["APIKey"]
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey= DEVELOPER_KEY)

# searches youtube for recent videos
vidRequest = youtube.search().list(
    part="snippet",
    channelId=key["channelID"],
    maxResults=2,
    order="date",
    type="video"
)

# Discord webhook
webhook = DiscordWebhook(url=key["webhook"])

# sends message via webhook on discord
def discordPing(title, description, url):
    webhook.content = "**New video @everyone** \n" + title + "\n" + description + "\n" + url
    webhook.execute()
    print("Successful notified your discord server!")

# Gets your latest video
def intialize():
    data = vidRequest.execute()
    global previousVideo
    previousVideo = data["items"][0]["snippet"]["title"];
    print(previousVideo)

# Checks if there is a new video
def checkVideo():
    global previousVideo
    data = vidRequest.execute()
    workingVideo = data["items"][0]["snippet"]["title"]

    # Checks if the latest video is equal to the working video, video it proccessed right now
    if workingVideo != previousVideo:
        # gets more data, title of the video, description of the video, and url of the video.
        title = data["items"][0]["snippet"]["title"].replace("&#39;", "'");
        # The first "-" is used in my description and this splits it to the first line, you can use something else
        description = data["items"][0]["snippet"]["description"].split("-")[0]
        url = "https://youtu.be/" + data["items"][0]["id"]["videoId"]
        # passes title, description and url for the discord message
        discordPing(title, description, url)
        # sets previous video as working video
        previousVideo = workingVideo

# checks if now is inbetween start and end times
def in_between(now, start, end):
    if start <= end:
        return start <= now < end
    else:
        return start <= now or now < end

# this function is useful as it's more efficent instead of checking for a video every minute
# it also uses up no API quota, increasing efficency
def checkTime():
    # checks if time now is inbetween start and endtimes specified in the json file and returns accordingly
    # this assumes you schedule your videos (if you aren't, you should it's great and really useful!)
    if in_between(datetime.now().time(), time(int(startTime.split(":")[0]), int(startTime.split(":")[1])), time(int(endTime.split(":")[0]), int(endTime.split(":")[1]))):
        return True
    else:
        return False

intialize()

# python script runs forever and checks time every minutes
while True:
    # if this time is true then it checks for videos
    if checkTime():
        print("true")
        checkVideo()
    sleep(60)
