import os


class PromptGenerator:
    def __init__(
        self,
        tts_engine,
        api_key,
        output_folder="prompts",
        file_prefix="",
        file_type="wav",
    ):
        self.output_folder = output_folder
        self.file_prefix = file_prefix
        self.file_type = file_type
        self.tts_engine = tts_engine
        self.api_key = api_key

    def generate_prompts(self, prompts):
        for prompt in prompts:
            content = self.tts_engine(prompt["prompt_text"], self.api_key)
            filename = (
                f"{self.file_prefix}"
                f"{prompt['prompt_name'].replace(' ', '_')}"
                f".{self.file_type}"
            )
            filepath = os.path.join(self.output_folder, filename)
            with open(filepath, "wb") as f:
                f.write(content)
