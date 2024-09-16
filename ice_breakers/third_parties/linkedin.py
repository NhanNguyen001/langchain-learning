import os
import requests

from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape the linkedin profile
    """
    response = requests.get(linkedin_profile_url)
    print(response.text)