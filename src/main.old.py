# Get  LRC format lyrics from spotify song
# 1. Get song info from spotify (artist and song name)
# 2. Get lyrics from lyrics.ovh
# 3. Convert lyrics to LRC format
# 4. Save lyrics to file

import json, base64, requests, re


# Read the Spotify Web API client - from config.json
with open("config.json") as f:
    config = json.load(f)[0]["spotifyWebApi"]
    clientId = config["clientId"]
    clientSecret = config["clientSecret"]

auth_header = base64.b64encode(f"{clientId}:{clientSecret}".encode("utf-8")).decode(
    "utf-8"
)

auth_response = requests.post(
    "https://accounts.spotify.com/api/token",
    data={"grant_type": "client_credentials"},
    headers={"Authorization": f"Basic {auth_header}"},
)
auth_response.raise_for_status()
access_token = auth_response.json()["access_token"]
# print(access_token)

# Look up the lyrics for a song
# track_id = "spotify:track:your_track_id"
artist = ""
song = "mean"
search_response = requests.get(
    f"https://api.spotify.com/v1/search?q=track:{song}+artist:{artist}&type=track",
    headers={"Authorization": f"Bearer {access_token}"},
)

if search_response.raise_for_status() == None:
    track_id = search_response.json()["tracks"]["items"][0]["id"]
    track_response = requests.get(
        f"https://api.spotify.com/v1/tracks/{track_id}",
        headers={"Authorization": f"Bearer {access_token}"},
    )
# print(json.dumps(track_response.json(), indent=4))

if track_response.raise_for_status() == None:
    lyrics_url = track_response.json()["external_urls"]["lyricwiki"]
# lyrics_url = track_response.json()["external_urls"]["lyricwiki"]
print(lyrics_url)
# # Retrieve the lyrics from the lyrics website
# lyrics_response = requests.get(lyrics_url)
# lyrics_response.raise_for_status()
# lyrics_html = lyrics_response.text

# # Extract the lyrics from the HTML
# lyrics_match = re.search(r"<lyrics>(.+?)</lyrics>", lyrics_html, re.DOTALL)
# if lyrics_match:
#     lyrics = lyrics_match.group(1)
# else:
#     lyrics = "Sorry, could not find lyrics for this song."

# # Convert the lyrics to LRC format
# lrc_lines = []
# for line in lyrics.split("\n"):
#     line = line.strip()
#     if not line:
#         continue
#     timestamp_match = re.match(r"\[(\d+:\d+\.\d+)\]", line)
#     if timestamp_match:
#         timestamp = timestamp_match.group(1)
#         line = line[len(timestamp) + 2:]
#     else:
#         timestamp = "0:00.00"
#     lrc_lines.append(f"{timestamp} {line}")
# lrc_lyrics = "\n".join(lrc_lines)

# print(lrc_lyrics)

#     return  lyrics
