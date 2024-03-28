# GPTerm

`GPTerm` is a command-line interface tool designed to provide a seamless interaction with OpenAI's API, incorporating optional Text-to-Speech (TTS) functionality. It allows users to interact with OpenAI models and receive audible responses, making it a versatile tool for developers, researchers, and enthusiasts interested in AI and machine learning.

## Features

- **Command-Line Interface**: Easy-to-use CLI for interacting with OpenAI's API.
- **Text-to-Speech Support**: Optional TTS support with `gTTS` and `espeak`, enhancing the interactive experience.
- **Customizable Settings**: Users can customize TTS options via command-line arguments.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- OpenAI API key
- Additional Python libraries: `dotenv`, `openai`, `gtts`, `pyttsx3`
- OS Packages: `mpg123` for `gTTS` support

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lostsync/gpterm.git
   ```
2. Navigate to the project directory and install the dependencies:
   ```bash
   cd gpterm
   pip install -r requirements.txt
   ```
   or: 

   ```bash
   pip install pyttsx3 argparse configparser python-dotenv openai gTTS
   ```

   * This list is likely incomplete at any given time, as well as requirements.txt *

3. Add your API key:
   ```bash
   echo "API_KEY=<YOURAPIKEY>" >> .env
   ```

## Usage

To use `GPTerm`, run the script with Python and select your preferred TTS option:

```bash
python gpterm.py --tts [off|gtts|espeak]
```

- `--tts off`: Disables TTS (default).
- `--tts gtts`: Uses Google's Text-to-Speech engine.
- `--tts espeak`: Uses the eSpeak TTS engine.

Type `quit` or `exit` to quit or exit. You can use `quit` to exit or `exit` to quit. You have options.

## Customization

This script is simple and two lines in `config.ini` can be updated to customize the behavior of the model. 

This sets the vibe. It's the same functionality as the instructions box in your OpenAI profile:
```python
Instructions = "Respond to the following dryly, with the emotional tone of an AI that is not particularly impressed with the dystopia humanity is creating: "
```

This handles context, by creating a longer prompt containing the context. Without this, the script has no way of remember who you are or what was said between prompts:
```ini
FullPrompt = Remembering that I said: '{last_prompt}', and that you responded with this: '{last_response}', and being mindful of the potential to change topics, please respond to what I have said next, which is this: {prompt}
```

## Roadmap

In the near future:

- [ ] Expose options for
   - [x] Instructions
   - [x] Context Prompt
   - [ ] Temperature

- [x] Config file support for exposed options.
   - [ ] Full assistant params in config file
   - [ ] Stop calling them config files when they're assistant definitions

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

`GPTerm` is licensed under the Apache License 2.0. See the `LICENSE` file for more details.
