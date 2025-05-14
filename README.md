# AI Video Generation Tool

This tool automatically generates short videos from trending news articles. It follows a pipeline of:
1. Fetching trending news from GDELT Project API
2. Generating a script using templates
3. Creating a video with text overlays and images

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the main script:
```bash
python main.py
```

## Project Structure

- `main.py`: Main entry point of the application
- `news_fetcher.py`: Handles fetching trending news articles from GDELT Project API
- `script_generator.py`: Generates video scripts using templates
- `video_generator.py`: Creates videos with text overlays and images
- `utils.py`: Utility functions

## Output

The generated videos will be saved in the `output` directory with timestamps in their filenames.

## Features

- Fetches trending news from GDELT Project API (free, no API key required)
- Generates simple video scripts using templates
- Creates videos with text overlays and images
- Saves metadata for each generated video 