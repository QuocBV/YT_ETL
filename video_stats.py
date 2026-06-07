import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env')
API_KEY = os.getenv('API_KEY')
CHANNEL_HANDLE = "MrBeast"


def get_playist_id():
    try:
        url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}'
        response = requests.get(url=url)
        # print('111')
        # print(response)
        # print('22')
        data = response.json()
        # print(json.dumps(data, indent= 4))
        channel_items = data["items"][0]
        channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
        #print(channel_playlistId)
        return channel_playlistId

    except requests.exceptions.RequestException as e:
        raise e


if __name__ == "__main__":
    playlist_id = get_playist_id()
    print(playlist_id)
