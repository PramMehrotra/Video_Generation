import os
import json
from datetime import datetime

def save_metadata(article, script, video_path):
    """
    Save metadata about the generated video
    """
    metadata = {
        'article': {
            'title': article['title'],
            'description': article['description'],
            'url': article['url'],
            'publishedAt': article['publishedAt']
        },
        'script': script,
        'video_path': video_path,
        'generated_at': datetime.now().isoformat()
    }

    # Create metadata directory if it doesn't exist
    metadata_dir = 'metadata'
    if not os.path.exists(metadata_dir):
        os.makedirs(metadata_dir)

    # Save metadata to file
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    metadata_path = os.path.join(metadata_dir, f"metadata_{timestamp}.json")
    
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)

    return metadata_path

def format_duration(seconds):
    """
    Format duration in seconds to MM:SS format
    """
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}" 