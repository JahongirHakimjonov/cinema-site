import os
import subprocess
import time
from shutil import which

from celery import shared_task
from django.conf import settings

from apps.hidaya.models import Video


@shared_task
def process_video(video_id):
    try:
        if which("ffmpeg") is None:
            raise FileNotFoundError("ffmpeg is not installed or not found in PATH")

        time.sleep(2)
        video = Video.objects.get(id=video_id)
        input_file = video.original_file.path
        resolutions = {
            "1080p": "1920x1080",
            "720p": "1280x720",
            "480p": "854x480",
        }

        hls_playlist = None  # Initialize hls_playlist

        for res, size in resolutions.items():
            hls_output_dir = os.path.join(
                settings.MEDIA_ROOT, f"hls_videos/{video.id}/{res}"
            )
            dash_output_dir = os.path.join(
                settings.MEDIA_ROOT, f"dash_videos/{video.id}/{res}"
            )
            os.makedirs(hls_output_dir, exist_ok=True)
            os.makedirs(dash_output_dir, exist_ok=True)

            # HLS conversion
            hls_playlist = os.path.join(hls_output_dir, "playlist.m3u8")
            subprocess.run(
                [
                    "ffmpeg",
                    "-i",
                    input_file,
                    "-vf",
                    f"scale={size}",
                    "-c:v",
                    "libx264",
                    "-start_number",
                    "0",
                    "-hls_time",
                    "10",
                    "-hls_list_size",
                    "0",
                    "-f",
                    "hls",
                    hls_playlist,
                ],
                check=True,
            )

            # DASH conversion
            dash_manifest = os.path.join(dash_output_dir, "manifest.mpd")
            subprocess.run(
                [
                    "ffmpeg",
                    "-i",
                    input_file,
                    "-vf",
                    f"scale={size}",
                    "-c:v",
                    "libx264",
                    "-f",
                    "dash",
                    dash_manifest,
                ],
                check=True,
            )

        if hls_playlist:
            print(f"Video {video_id} processing completed successfully.")
            os.remove(input_file)
            video.hls_playlist = hls_playlist.replace("app/assets/media/", "")
            video.original_file = None
            video.save()
            print(f"Original file for video {video_id} removed.")

    except Video.DoesNotExist:
        print(f"Video with id {video_id} does not exist.")
    except FileNotFoundError as e:
        print(e)
    except subprocess.CalledProcessError as e:
        print(f"Error during video processing: {e}")
