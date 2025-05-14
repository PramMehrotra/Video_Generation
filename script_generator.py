import os
from openai import OpenAI
from dotenv import load_dotenv

class ScriptGenerator:
    def __init__(self):
        pass

    def generate_script(self, article):
        """
        Generate a video script from a news article using templates
        """
        try:
            # Extract key information
            title = article['title']
            description = article['description']
            
            # Create a simple script structure
            script = {
                'script': f"""
                Breaking news: {title}
                
                {description}
                
                Stay tuned for more updates on this developing story.
                """,
                'timestamps': [
                    (0, f"Breaking News: {title}"),
                    (5, description[:100] + "..."),
                    (10, "Stay tuned for more updates on this developing story.")
                ],
                'visuals': [
                    (0, "Show breaking news graphic"),
                    (5, "Display article image"),
                    (10, "Show closing graphic")
                ]
            }
            
            return script

        except Exception as e:
            print(f"Error generating script: {str(e)}")
            return None

    def _parse_timestamps(self, timestamps_text):
        """Parse timestamps from the AI response"""
        timestamps = []
        for line in timestamps_text.split('\n'):
            if ':' in line:
                time, text = line.split(':', 1)
                try:
                    time = float(time.strip())
                    timestamps.append((time, text.strip()))
                except ValueError:
                    continue
        return timestamps

    def _parse_visuals(self, visuals_text):
        """Parse visual descriptions from the AI response"""
        visuals = []
        for line in visuals_text.split('\n'):
            if ':' in line:
                time, description = line.split(':', 1)
                try:
                    time = float(time.strip())
                    visuals.append((time, description.strip()))
                except ValueError:
                    continue
        return visuals 