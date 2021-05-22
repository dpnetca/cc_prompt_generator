import os

import requests
from dotenv import load_dotenv

load_dotenv()


def voice_rss(
    text,
    api_key,
    lang="en-ca",
    voice="Clara",
    rate=0,
    codec="WAV",
    format="ulaw_8khz_mono",
    ssml=False,
    b64=False,
):
    if not api_key:
        api_key = os.getenv("VOICE_RSS_API_KEY")
    url = "http://api.voicerss.org/"
    params = {
        "key": api_key,
        "src": text,
        "hl": lang,
        "v": voice,
        "r": rate,
        "c": codec,
        "f": format,
        "ssml": ssml,
        "b64": b64,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.content
