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
   git clone https://github.com/yourusername/gpterm.git
   ```
2. Navigate to the project directory and install the dependencies:
   ```bash
   cd gpterm
   pip install -r requirements.txt
   ```
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

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

`GPTerm` is licensed under the Apache License 2.0. See the `LICENSE` file for more details.
