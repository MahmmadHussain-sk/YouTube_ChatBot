# extractor.py
# This file is responsible for ONE job: given a YouTube URL, return the
# full transcript text, or None if the video has no subtitles.

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def get_video_id(youtube_url):
    """
    Pulls the 11-character video id out of a full YouTube URL.
    Works for both formats:
      https://www.youtube.com/watch?v=VIDEO_ID
      https://youtu.be/VIDEO_ID
    """
    # Long format URL contains "v=" followed by the id
    if "v=" in youtube_url:
        video_id = youtube_url.split("v=")[1]
        # Remove any extra parameters after the id (e.g. &t=30s)
        video_id = video_id.split("&")[0]
        return video_id

    # Short format URL: the id is just the last part of the path
    video_id = youtube_url.split("/")[-1]
    return video_id


def get_transcript(video_id):
    """
    Fetches the subtitle/transcript text for a video id and joins it
    into one big string.

    Note: the youtube_transcript_api library raises an exception
    (instead of returning an empty result) when a video simply has no
    subtitles. That's the ONE place in this whole project where a
    try/except is genuinely needed - there is no other way to detect
    "no subtitles" without catching that exception.
    """
    try:
        api = YouTubeTranscriptApi()
        transcript_chunks = api.fetch(video_id)

        # Each chunk has a .text field - join them into one full string
        full_text = " ".join([chunk.text for chunk in transcript_chunks])
        return full_text

    except (TranscriptsDisabled, NoTranscriptFound):
        # No subtitles exist for this video
        return None
