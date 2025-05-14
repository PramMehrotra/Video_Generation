import os
from moviepy.editor import VideoFileClip, TextClip, ImageClip, CompositeVideoClip
from PIL import Image
import requests
from io import BytesIO
import tempfile
import time

class VideoGenerator:
    def __init__(self):
        self.output_dir = 'output'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def create_video(self, script, article):
        """
        Create a video from the generated script and article
        """
        try:
            # Create a temporary directory for assets
            with tempfile.TemporaryDirectory() as temp_dir:
                # Download and save the article image
                if article['urlToImage']:
                    image_path = self._download_image(article['urlToImage'], temp_dir)
                    if image_path:
                        # Create base video from image
                        base_clip = ImageClip(image_path).set_duration(60)
                    else:
                        # Create a black background if no image
                        base_clip = ColorClip(size=(1920, 1080), color=(0, 0, 0)).set_duration(60)
                else:
                    # Create a black background if no image
                    base_clip = ColorClip(size=(1920, 1080), color=(0, 0, 0)).set_duration(60)

                # Create text overlays
                text_clips = []
                for timestamp, text in script['timestamps']:
                    txt_clip = TextClip(
                        text,
                        fontsize=70,
                        color='white',
                        font='Arial-Bold',
                        stroke_color='black',
                        stroke_width=2
                    )
                    txt_clip = txt_clip.set_position(('center', 'center'))
                    txt_clip = txt_clip.set_start(timestamp)
                    txt_clip = txt_clip.set_duration(5)  # Each text appears for 5 seconds
                    text_clips.append(txt_clip)

                # Combine all clips
                final_clip = CompositeVideoClip([base_clip] + text_clips)

                # Generate output filename
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                output_path = os.path.join(self.output_dir, f"video_{timestamp}.mp4")

                # Write the result to a file
                final_clip.write_videofile(
                    output_path,
                    fps=24,
                    codec='libx264',
                    audio=False
                )

                return output_path

        except Exception as e:
            print(f"Error creating video: {str(e)}")
            return None

    def _download_image(self, url, temp_dir):
        """
        Download an image from URL and save it to a temporary directory
        """
        try:
            response = requests.get(url)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                # Resize image to 1920x1080 while maintaining aspect ratio
                image.thumbnail((1920, 1080), Image.Resampling.LANCZOS)
                # Create a new image with black background
                background = Image.new('RGB', (1920, 1080), (0, 0, 0))
                # Calculate position to center the image
                x = (1920 - image.width) // 2
                y = (1080 - image.height) // 2
                # Paste the image onto the background
                background.paste(image, (x, y))
                # Save the image
                image_path = os.path.join(temp_dir, 'background.jpg')
                background.save(image_path)
                return image_path
        except Exception as e:
            print(f"Error downloading image: {str(e)}")
            return None 