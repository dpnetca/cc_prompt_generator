# Contact Centre IVR Prompt Generator

Generate Contact Centre IVR prompts from CSV file input. Each row in the csv file will be generated as a 8Khz Mono uLaw encoded wav file and saves ad the prompt name. Spaces in the prompt name will be converted to underscores in the output file name.

```
usage: generate.py [-h] [-t TTS Engine] [-a API_KEY] prompts.csv

Generate TTS prompts from CSV

positional arguments:
  prompts.csv           CSV File to containing prompt name and text

optional arguments:
  -h, --help            show this help message and exit
  -t TTS Engine, --tts-engine TTS Engine
                        TTS API Engine to use default=VoiceRSS
  -a API_KEY, --api-key API_KEY
                        API Key, requried if not defined as environmental variable
```

Sample CSV File:

```
prompt_name,prompt_text
welcome,Thank you for calling Acme Corporation
main menu,"Please select from the following menu options. Press 1 for sales, Press 2 for support"
sales_busy,"All of our sales representatives are busy serving other customers, please hold on the line and your call will be answered in the order it was received"
```

## Current Supported TTS API's:

- VoiceRSS: http://www.voicerss.org
