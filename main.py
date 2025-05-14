import os
from news_fetcher import NewsFetcher
from script_generator import ScriptGenerator
from video_generator import VideoGenerator
import time

def main():
    try:
        # Initialize components
        news_fetcher = NewsFetcher()
        script_generator = ScriptGenerator()
        video_generator = VideoGenerator()

        # Fetch trending news
        print("Fetching trending news...")
        articles = news_fetcher.get_trending_news(max_articles=3)
        
        if not articles:
            print("No articles found. Exiting...")
            return

        # Process each article
        for i, article in enumerate(articles, 1):
            print(f"\nProcessing article {i}/{len(articles)}: {article['title']}")
            
            # Generate script
            print("Generating script...")
            script = script_generator.generate_script(article)
            
            if not script:
                print("Failed to generate script. Skipping article...")
                continue

            # Create video
            print("Creating video...")
            video_path = video_generator.create_video(script, article)
            
            if video_path:
                print(f"Video created successfully: {video_path}")
            else:
                print("Failed to create video.")

            # Add a small delay between processing articles
            if i < len(articles):
                time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 