import hashlib
import os

import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env"))

video_id = "3"
quality = "1080p"
file_name = "playlist.m3u8"

combined_key = f"{video_id}{quality}{file_name}"
hashed_key = hashlib.sha256(combined_key.encode()).hexdigest()

print(hashed_key)

url = f"http://127.0.0.1:8003/api/v1/videos/{video_id}/{quality}/{file_name}/signed-url/"

response = requests.post(url, data={"key": hashed_key})

print(response.json())
