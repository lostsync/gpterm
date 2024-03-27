import os, time, random, tempfile, threading, subprocess, argparse

from dotenv import load_dotenv
from openai import OpenAI

from gtts import gTTS
import pyttsx3

parser = argparse.ArgumentParser(description="A script to interact with OpenAI's API with optional TTS.")
parser.add_argument('--tts', '-t', choices=['off', 'gtts', 'espeak'], default='off',
                    help='Select the text-to-speech system to use: off (default), gtts, or espeak.')

args = parser.parse_args()

load_dotenv()
API_KEY = os.getenv("API_KEY")
client = OpenAI(api_key=API_KEY)


last_prompt = None
last_response = None

def speak_response(text, lang='en', tts_option=args.tts):
    if tts_option == 'gtts':
        # gTTS functionality here
        tts = gTTS(text=text, lang='en')
        tts.save("response.mp3")
        os.popen("mpg321 response.mp3 > /dev/null 2>&1")
        pass  # Placeholder for gTTS code
    elif tts_option == 'espeak':
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        def _speak(rate_increase=20):
            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate + rate_increase)  # Adjust speech rate
            engine.setProperty('voice', 16) 
            engine.say(text)
            engine.runAndWait()
        
        thread = threading.Thread(target=_speak)
        thread.start()

def type_to_screen(input_text):
    for char in input_text:
        print(char, end='', flush=True)  # Print character without adding a newline
        if char == ' ':
            time.sleep(random.uniform(0.1, 0.25))  # Longer pause for space between words
        else:
            time.sleep(random.uniform(0.01, 0.05))  # Shorter random pause between letters

# def speak_response(response):
#    subprocess.Popen(['espeak-ng', response])

instructions = "Respond to the following dryly, with the emotional tone of an AI that is not particularly impressed with the dystopia humanity is creating: "

def generate_response(prompt):
    global last_prompt, last_response
    full_prompt = prompt    
    # print("last_prompt: " + last_prompt)
    if last_prompt and last_response:
        full_prompt = f"Remembering that I said: '{last_prompt}', and that you responded with this: '{last_response}', and being mindful of the potential to change topics, please respond to what I have said next, which is this: {prompt}"
        # print("prompt modified " + full_prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": instructions + full_prompt}])
    return response.choices[0].message.content.strip()

def main():
    global last_prompt, last_response
    while True:
        user_input = input("> ")
        if user_input.lower() in ["quit", "exit"]:
            break

        last_response = generate_response(user_input)
        last_prompt = user_input
        speak_response(last_response)

        print('» ', end='')

        type_to_screen(last_response)
        print('\n')

if __name__ == "__main__":
    main()
