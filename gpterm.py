import os
import time
import random
import pyttsx3
import asyncio
import platform
import tempfile
import argparse
import threading
import subprocess
import configparser
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.filters import Condition
from prompt_toolkit.application import run_in_terminal

from dotenv import load_dotenv
from openai import OpenAI
from gtts import gTTS

class OpenAIChat:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="A script to interact with OpenAI's API with optional TTS.")
        self.parser.add_argument('--typing-speed', '-s', type=float, default=0.05,
                                 help='Typing speed for the chatbot response (default: 0.05).')
        self.parser.add_argument('--tts', '-t', choices=['off', 'gtts', 'espeak'], default='off',
                                 help='Select the text-to-speech system to use: off (default), gtts, or espeak.')
        self.parser.add_argument('--config', '-c', default=None)
        self.args = self.parser.parse_args()

        config_path = self.args.config
        if config_path is None:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(script_dir, 'config.ini')

        config = configparser.ConfigParser()
        if os.path.exists(config_path):
            config.read(config_path)
        else:
            # Set default values if config file is not found
            config['DEFAULT'] = {
                'Instructions': "You are a helpful AI assistant",
                'FullPrompt': "Remembering that I said: '{last_prompt}', and that you responded with this: '{last_response}', and being mindful of the potential for me to abrubtly change topics, please respond to what I have said next, which is this: {prompt}"
            }

        load_dotenv()
        API_KEY = os.getenv("API_KEY")
        if API_KEY is None:
            raise ValueError("API_KEY not found in environment variables")

        self.client = OpenAI(api_key=API_KEY)
        self.last_prompt = None
        self.last_response = None
        self.instructions = config.get('DEFAULT', 'Instructions')
        self.full_prompt_template = config.get('DEFAULT', 'FullPrompt')

    def generate_response(self, prompt):
        full_prompt = prompt    
        
        if self.last_prompt and self.last_response:
            full_prompt = self.full_prompt_template.format(last_prompt=self.last_prompt, last_response=self.last_response, prompt=prompt)
        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": self.instructions + full_prompt}])
        return response.choices[0].message.content.strip()

    def speak_response(self, text, lang='en'):
        if self.args.tts == 'gtts':
         
            tts = gTTS(text=text, lang='en')
            tts.save("response.mp3")
            dir_path = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(dir_path, "response.mp3")   
            if platform.system() == 'Darwin':
                # macOS
                os.popen('afplay response.mp3')
            elif platform.system() == 'Linux':
                # Linux
                os.popen('mpg123 response.mp3')
            elif platform.system() == 'Windows':
                # Windows
                os.popen('start response.mp3')

        elif self.args.tts == 'espeak':
            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate + 20)  # Adjust speech rate
            engine.setProperty('voice', 16) 
            engine.say(text)
            engine.runAndWait()

    async def main(self):
        session = PromptSession()
        bindings = KeyBindings()

        @bindings.add('c-l')
        def _(event):
            event.app.output.clear_buffer()
            print(event.app.output.flush())

        while True:
            try:
                user_input = await session.prompt_async('> ', key_bindings=bindings)
            except KeyboardInterrupt:
                break

            if user_input.lower() in ["quit", "exit"]:
                break

            self.last_response = self.generate_response(user_input)
            self.last_prompt = user_input
            self.speak_response(self.last_response)

            print('» ', end='', flush=True)
            await self.type_to_screen_async(self.last_response)
            print('\n')

    async def type_to_screen_async(self, input_text):
        typing_speed = self.args.typing_speed
        for char in input_text:
            print(char, end='', flush=True)  # Print character without adding a newline
            if char == ' ':
                await asyncio.sleep(typing_speed * 2)  # Longer pause for space between words
            else:
                await asyncio.sleep(typing_speed)  # Pause between letters

if __name__ == "__main__":
    chat = OpenAIChat()
    asyncio.run(chat.main())
