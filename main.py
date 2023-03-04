from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip
from pytube import YouTube
import moviepy.editor as mp

from mutagen.mp3 import MP3
from PIL import Image
import imageio
from moviepy import editor
from pathlib import Path
import os

audio_path = os.path.join(os.getcwd(), "my_result.mp3")
video_path = os.path.join(os.getcwd(), "videos")
images_path = os.path.join(os.getcwd(), "images")

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        obj = youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    return obj




def add_static_image_to_audio(image_path, audio_path, output_path):
    """Create and save a video file to `output_path` after
    combining a static image that is located in `image_path`
    with an audio file in `audio_path`"""
    # create the audio clip object
    audio_clip = AudioFileClip(audio_path)
    # create the image clip object
    image_clip = ImageClip(image_path)
    # use set_audio method from image clip to combine the audio with the image
    video_clip = image_clip.set_audio(audio_clip)
    # specify the duration of the new clip to be the duration of the audio clip
    video_clip.duration = audio_clip.duration
    # set the FPS to 1
    video_clip.fps = 1


    # write the resuling video clip
    video_clip.write_videofile(output_path)


if __name__ == "__main__":


    add_static_image_to_audio("my_result.mp3","george_wassouf.png","Youtube-Downloader")