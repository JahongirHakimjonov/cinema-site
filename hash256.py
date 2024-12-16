import hashlib

key = "salom"
video_id = "3"
quality = "1080p"
file_name = "playlist.m3u8"

combined_key = f"{key}{video_id}{quality}{file_name}"
hashed_key = hashlib.sha256(combined_key.encode()).hexdigest()

print(hashed_key)
