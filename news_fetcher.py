import requests
from datetime import datetime, timedelta
import json

class NewsFetcher:
    def __init__(self):
        self.base_url = "https://api.gdeltproject.org/api/v2/doc/doc"
        
    def get_trending_news(self, max_articles=5):
        """
        Fetch trending news articles from GDELT Project API
        """
        try:
            # Get news from the last 24 hours
            end_date = datetime.now()
            start_date = end_date - timedelta(days=1)
            
            # Format dates for API
            start_str = start_date.strftime("%Y%m%d%H%M%S")
            end_str = end_date.strftime("%Y%m%d%H%M%S")
            
            # Construct API URL
            url = f"{self.base_url}?query=domain:news.com OR domain:reuters.com OR domain:apnews.com&mode=artlist&format=json&startdatetime={start_str}&enddatetime={end_str}&maxrecords={max_articles}"
            
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception(f"GDELT API Error: {response.status_code}")
            
            data = response.json()
            articles = data.get('articles', [])
            processed_articles = []
            
            for article in articles:
                processed_articles.append({
                    'title': article.get('title', ''),
                    'description': article.get('seendesc', ''),
                    'content': article.get('seendesc', ''),  # Using description as content
                    'url': article.get('url', ''),
                    'urlToImage': article.get('imageurl', ''),
                    'publishedAt': article.get('seendate', '')
                })
            
            return processed_articles

        except Exception as e:
            print(f"Error fetching news: {str(e)}")
            return []

    def get_article_content(self, url):
        """
        Fetch the full content of an article using requests
        """
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Basic content extraction (you might want to use beautifulsoup4 for better extraction)
                return response.text[:1000]  # Return first 1000 characters as a simple approach
            return None
        except Exception as e:
            print(f"Error fetching article content: {str(e)}")
            return None 