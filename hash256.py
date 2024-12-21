import hashlib

import requests

video_id = "1"
quality = "1080p"
file_name = "playlist.m3u8"

combined_key = f"{video_id}{quality}{file_name}"
hashed_key = hashlib.sha256(combined_key.encode()).hexdigest()

print(hashed_key)

url = (
    f"http://127.0.0.1:8003/api/v1/videos/{video_id}/{quality}/{file_name}/signed-url/"
)

for _ in range(10):
    response = requests.post(url, data={"key": hashed_key})

    print(response.json())
