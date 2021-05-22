#!/usr/bin/env python
import csv

import tts
from prompt_generator import PromptGenerator
from helpers.cli_args import parser


args = parser.parse_args()

csv_file = args.prompts

with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    prompts = [row for row in reader]

tts_engine = tts.tts_engines.get(args.tts_engine.lower())
if tts_engine:
    prompt_gen = PromptGenerator(tts_engine, args.api_key)
    prompt_gen.file_prefix = f"{args.tts_engine.lower()}-"
    prompt_gen.output_folder = "example_prompts"
    prompt_gen.generate_prompts(prompts)
else:
    print("invalid tts engine")
