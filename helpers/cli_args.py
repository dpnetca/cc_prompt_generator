import argparse

parser = argparse.ArgumentParser(description="Generate TTS prompts from CSV")
parser.add_argument(
    dest="prompts",
    metavar="prompts.csv",
    help="CSV File to containing prompt name and text",
)
parser.add_argument(
    "-t",
    "--tts-engine",
    default="VoiceRSS",
    dest="tts_engine",
    metavar="TTS Engine",
    help="TTS API Engine to use default=VoiceRSS",
)
parser.add_argument(
    "-a",
    "--api-key",
    required=False,
    help="API Key, requried if not defined as environmental variable",
)
