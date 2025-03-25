# AI Voice Assistant with Google Search Integration

This project is an AI-powered voice assistant that listens to user queries, performs a Google search using the Programmable Search Engine API, and provides a concise, conversational response. It also includes text-to-speech functionality to make the interaction more natural.

## Features

- **Voice Recognition**: Listens to user queries using the `speech_recognition` library.
- **Google Search Integration**: Fetches search results using the Google Programmable Search Engine API.
- **Web Scraping**: Scrapes webpage content for detailed information using `BeautifulSoup`.
- **Text-to-Speech**: Responds to users with synthesized speech using `pyttsx3`.
- **Summarization**: Provides a medium-length summary of the search results.

## Prerequisites

- Python 3.7 or higher
- Required Python libraries:
  - `google-api-python-client`
  - `requests`
  - `beautifulsoup4`
  - `speechrecognition`
  - `pyttsx3`

Install the dependencies using:
```bash
pip install google-api-python-client requests beautifulsoup4 SpeechRecognition pyttsx3
```

## Setup

1. Clone the repository or copy the project files to your local machine.
2. Obtain your Google API key and Programmable Search Engine ID by following the instructions at [Google Custom Search API Documentation](https://developers.google.com/custom-search/v1/introduction).
3. Replace the placeholders for `API_KEY` and `CSE_ID` in `main.py` with your credentials.

## Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. The assistant will greet you and wait for your voice input.
3. Speak your query, and the assistant will process it, perform a Google search, and provide a summarized response.
4. Say "exit" or "stop" to terminate the assistant.

## Example Interaction

- **User**: "What is the capital of France?"
- **Assistant**: "Here's a summary of **Paris**: Quick Overview: Paris is the capital city of France... Let me know if you'd like more details or have any further questions!"

## Notes

- Ensure your microphone is working properly for voice input.
- A stable internet connection is required for Google Search and web scraping.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [Google API Client Library for Python](https://github.com/googleapis/google-api-python-client)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3 Documentation](https://pyttsx3.readthedocs.io/)